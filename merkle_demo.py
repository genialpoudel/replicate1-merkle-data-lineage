import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_root(hashes):
    if len(hashes) == 1:
        return hashes[0]

    new_level = []

    for i in range(0, len(hashes), 2):
        left = hashes[i]
        right = hashes[i] if i + 1 == len(hashes) else hashes[i + 1]
        new_level.append(hash_data(left + right))

    return build_merkle_root(new_level)


rows = [
    "user1,25,approved",
    "user2,40,approved",
    "user3,31,approved",
    "user4,29,approved"
]

leaf_hashes = [hash_data(row) for row in rows]

root = build_merkle_root(leaf_hashes)

print("Merkle root:")
print(root)
