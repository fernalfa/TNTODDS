# Define the variable, multiplier, and values
a = 898999
b = 900999
c = 902999

# Specify GAME ROTATION NUMBER

ROT = 7

# Multiply the variable by the multiplier and add the three values
result = (ROT * 2) + a
result2 = (ROT * 2) + a + 2
result3 = (ROT * 2) + b
result4 = (ROT * 2) + b + 2
result5 = (ROT * 2) + c
result6 = (ROT * 2) + c + 2

# Print the result to the console
print("FG Rotation")
print("Away FG - " + str(result) + " / Home FG - " + str(result2))
print("Away 1st - " + str(result3) + " / Home 1st - " + str(result4))
print("Away 2nd - " + str(result5) + " / Home 2nd - " + str(result6))