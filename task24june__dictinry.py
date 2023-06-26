'''user_input = input("Enter a string: ")
MD= {}

# Count the occurrences of each character
for i in user_input:
    if i in MD:
        MD[i] += 1
    else:
        MD[i] = 1

# Print the dictionary
for i, count in MD.items():
    print(f"character '{i}': Count {count}")


user_input = input("Enter a string: ")


valid_chars = set('0123456789ABCDEFGHIJKLMNOPcdefghijklmnopqrstuvwxyz@#$')


contains_all_chars = all(char in valid_chars for char in user_input)

if contains_all_chars:
    print("Input contains all the valid characters.")
else:
    print("Input does not contain all the valid characters.")'''

print("\n\n\  .   ..........................................................n\n")
for i in range(6, 0, -1):
        for j in range(6 - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()
