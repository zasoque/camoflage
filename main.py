import random
from PIL import Image

colors = [
    (0x46, 0x50, 0x46),
    (0x3A, 0x4D, 0x58),
    (0x72, 0x75, 0x61),
    (0x96, 0x85, 0x69),
    (0x4D, 0x5E, 0x56),
]


def main(seed=42, seed_rate=0.001, mutation_rate=0.07, size=256):
    random.seed(seed)

    board = [[0 for _ in range(size)] for _ in range(size)]

    image = Image.new("RGB", (size, size), color="white")

    leaves = list()
    for i in range(size):
        for j in range(size):
            if random.random() < seed_rate:
                board[i][j] = random.randint(1, len(colors))
                leaves.append((i, j))

    pixels = 0
    while leaves:
        random.shuffle(leaves)
        new_leaves = []
        for i, j in leaves:
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < size and 0 <= nj < size and board[ni][nj] == 0:
                    if random.random() < mutation_rate:
                        board[ni][nj] = random.randint(1, len(colors))
                    else:
                        board[ni][nj] = board[i][j]
                    new_leaves.append((ni, nj))
                    pixels += 1
        leaves = new_leaves
        print(pixels / (size * size) * 100, "%")

    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                image.putpixel((j, i), colors[board[i][j] - 1])

    image.save(f"output/output_{size}@{seed}.png")


if __name__ == "__main__":
    main(size=1024)
