# Week 1.3, Session 1: Task 2b

print("This program will repeat everything you type.")
print("To exit the program type quit")

while True:
    user_input = input("Say something: ")
    if user_input.lower() == "quit":
        break
    print(f"You said: {user_input}")

# The loop exits when the user enters 'quit'.