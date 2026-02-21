import hashlib

# --------------------------
# Functions
# --------------------------
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()[:8]  # short hash for display

def build_merkle_tree(hashes):
    """Return the final root and a list of tree levels for visualization"""
    tree_levels = [hashes]  # bottom level (leaves)
    while len(hashes) > 1:
        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i] if i + 1 == len(hashes) else hashes[i + 1]
            new_level.append(hash_data(left + right))
        hashes = new_level
        tree_levels.append(hashes)
    return hashes[0], tree_levels

def print_tree(tree_levels):
    """Print ASCII style tree"""
    for level in reversed(tree_levels):
        print("   ".join(level))
    print()

# --------------------------
# Input dataset
# --------------------------
rows = []
print("Enter 4 rows of data (e.g., 'user1,25,approved'):")
for i in range(4):
    r = input(f"Row {i+1}: ")
    rows.append(r)

# --------------------------
# Hash each row
# --------------------------
leaf_hashes = [hash_data(row) for row in rows]

# Print table
print("\nRow Data          | Hash")
print("-----------------|--------")
for r, h in zip(rows, leaf_hashes):
    print(f"{r:<16} | {h}")

# --------------------------
# Build Merkle tree
# --------------------------
root, tree_levels = build_merkle_tree(leaf_hashes)
print("\nMerkle Tree (root at top):")
print_tree(tree_levels)

print(f"Final Merkle Root: {root}")

# --------------------------
# Tampering demo
# --------------------------
print("\n--- Tampering Test ---")
tamper_index = int(input("Enter row number to change (1-4): ")) - 1
new_value = input("Enter new value: ")
rows[tamper_index] = new_value

# Recompute hashes
leaf_hashes = [hash_data(row) for row in rows]
root, tree_levels = build_merkle_tree(leaf_hashes)

print("\nUpdated Table:")
print("Row Data          | Hash")
print("-----------------|--------")
for r, h in zip(rows, leaf_hashes):
    print(f"{r:<16} | {h}")

print("\nUpdated Merkle Tree (root at top):")
print_tree(tree_levels)
print(f"New Merkle Root: {root}")M
