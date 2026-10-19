"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
state_order = list(states)
state_index = 0
elapsed = 0

for systime in range(1, maxtime + 1):
	elapsed += 1

	if elapsed == states[state]:
		state_index = (state_index + 1) % len(state_order)
		state = state_order[state_index]
		elapsed = 0

	print(f"Time {systime:03} State {state}")