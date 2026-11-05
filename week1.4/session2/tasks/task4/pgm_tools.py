
# PGM functions that we write

def readPGM(filename):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''
    with open(filename, "r", encoding="utf-8") as f:
        tokens = []
        for line in f:
            if line.strip().startswith('#'):
                continue
            tokens.extend(line.split())

    if not tokens or tokens[0] != 'P2':
        raise ValueError("This function expects a P2 PGM file.")

    width = int(tokens[1])
    height = int(tokens[2])
    max_gray = int(tokens[3])
    pixels = []
    index = 4

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(int(tokens[index]))
            index += 1
        pixels.append(row)

    return width, height, max_gray, pixels


def writePGM(filename, image):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width, height, max_gray, pixels = image

    with open(filename, "w", encoding="utf-8") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")

        for row in pixels:
            f.write(" ".join(str(pixel) for pixel in row) + "\n")

    return


def invertPGM(image):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width, height, max_gray, pixels = image
    inverted = [[max_gray - value for value in row] for row in pixels]
    return width, height, max_gray, inverted


# code to test the PGM functions

image = readPGM("images/feep.pgm")
print(f"Image with width {image[0]} and height {image[1]}")
print(f"First pixel row: {image[3][0]}")

inverted = invertPGM(image)
writePGM("images/inverted_feep.pgm", inverted)
print("Inverted image written to images/inverted_feep.pgm")

# write further code to test your own functions
