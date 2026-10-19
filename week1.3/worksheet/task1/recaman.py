# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = [0] if L > 0 else []
seen = set(sequence)

for k in range(1, L):
	previous = sequence[-1]
	candidate = previous - k

	if candidate > 0 and candidate not in seen:
		next_value = candidate
	else:
		next_value = previous + k

	sequence.append(next_value)
	seen.add(next_value)


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence