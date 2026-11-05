# Week 1.3, Session 2: Invert PGM image

from pathlib import Path

source_path = Path(__file__).resolve().parent.parent / "images" / "plus.pgm"
out_path = Path(__file__).with_name("inverted_plus.pgm")

try:
    with source_path.open("r", encoding="utf-8") as file:
        lines = []
        for line in file:
            if line.startswith("#"):
                continue
            lines.append(line)

    tokens = []
    for line in lines:
        tokens.extend(line.split())

    if len(tokens) < 4:
        raise ValueError("Invalid PGM file: missing header information.")

    magic_number = tokens[0]
    if magic_number != "P2":
        raise ValueError(f"Unsupported PGM format: {magic_number}")

    width = int(tokens[1])
    height = int(tokens[2])
    max_gray = int(tokens[3])
    pixel_values = [int(value) for value in tokens[4:]]

    inverted = [max_gray - value for value in pixel_values]

    with out_path.open("w", encoding="utf-8") as output:
        output.write("P2\n")
        output.write(f"{width} {height}\n")
        output.write(f"{max_gray}\n")

        for row_index in range(height):
            row = inverted[row_index * width:(row_index + 1) * width]
            output.write(" ".join(str(value) for value in row) + "\n")

    print(f"Inverted image written to {out_path.name}")

except FileNotFoundError:
    print(f"Error: file not found at {source_path}")
except ValueError as error:
    print(f"Error: {error}")