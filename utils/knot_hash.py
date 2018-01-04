def knot_hash(seed):
    lengths = [ord(c) for c in seed] + [17, 31, 73, 47, 23]

    sparse_hash, current, skip = range(256), 0, 0
    for _ in range(64):
        sparse_hash, current, skip = single_round(sparse_hash, lengths, current, skip)

    dense_hash = [reduce(lambda x, y: x ^ y, sparse_hash[(i * 16):((i + 1) * 16)]) for i in range(16)]

    return ''.join(['{:02x}'.format(c) for c in dense_hash])


def get_sections(sparse_hash, current, length):
    if current + length < len(sparse_hash):
        return (current, current + length), (0, 0)
    else:
        return (current, len(sparse_hash)), (0, current + length - len(sparse_hash))


def single_round(sparse_hash, lengths, current=0, skip=0):
    for length in lengths:
        (s1_s, s1_e), (s2_s, s2_e) = get_sections(sparse_hash, current, length)

        reverse = (sparse_hash[s1_s:s1_e] + sparse_hash[s2_s:s2_e])[::-1]

        sparse_hash[s1_s:s1_e] = reverse[:s1_e - s1_s]
        sparse_hash[s2_s:s2_e] = reverse[s1_e - s1_s:]

        current = (current + length + skip) % len(sparse_hash)
        skip += 1

    return sparse_hash, current, skip
