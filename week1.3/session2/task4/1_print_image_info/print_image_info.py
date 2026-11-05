# Week 1.3, Session 2: Print PGM image info

from pathlib import Path

image_path = Path(__file__).resolve().parent.parent / "images" / "feep.pgm"

try:
    with image_path.open("r", encoding="utf-8") as file:
        tokens = []
        for line in file:
            if line.startswith("#"):
                continue
            tokens.extend(line.split())

    if len(tokens) < 4:
        raise ValueError("Invalid PGM file: missing header information.")

    magic_number = tokens[0]
    if magic_number != "P2":
        raise ValueError(f"Unsupported PGM format: {magic_number}")

    width = int(tokens[1])
    height = int(tokens[2])
    max_gray_value = int(tokens[3])

    pixel_values = [int(value) for value in tokens[4:]]

    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Gray Value: {max_gray_value}")

except FileNotFoundError:
    print(f"Error: file not found at {image_path}")
except ValueError as error:
    print(f"Error: {error}")