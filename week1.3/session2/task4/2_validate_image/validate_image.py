# Week 1.3, Session 2: Validate image

from pathlib import Path

image_path = Path(__file__).resolve().parent.parent / "images" / "plus.pgm"

try:
    with image_path.open("r", encoding="utf-8") as file:
        lines = []
        for line in file:
            if line.startswith("#"):
                continue
            lines.append(line)

    if len(lines) < 4:
        raise ValueError("Invalid PGM file: missing header information.")

    tokens = []
    for line in lines:
        tokens.extend(line.split())

    magic_number = tokens[0]
    if magic_number != "P2":
        raise ValueError(f"Unsupported PGM format: {magic_number}")

    width = int(tokens[1])
    height = int(tokens[2])
    max_gray_value = int(tokens[3])

    pixel_rows = []
    index = 4
    while index < len(tokens):
        pixel_rows.append([int(value) for value in tokens[index:index + width]])
        index += width

    if len(pixel_rows) != height:
        print("Invalid height")
    elif any(len(row) != width for row in pixel_rows):
        print("Invalid width")
    elif any(pixel < 0 or pixel > max_gray_value for row in pixel_rows for pixel in row):
        print("Invalid pixel values")
    else:
        print("Valid image")

except FileNotFoundError:
    print(f"Error: file not found at {image_path}")
except ValueError as error:
    print(f"Error: {error}")