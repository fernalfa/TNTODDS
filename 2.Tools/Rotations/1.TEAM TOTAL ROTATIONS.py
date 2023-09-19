# Define the variable, multiplier, and values
a = 898999
b = 900999
c = 902999

# Specify GAME ROTATION NUMBER

ROT = 309035


# CALCULATE PERIODS ROTATION NUMBERS
halftime1st = (ROT + 1000)
halftime2nd = (ROT + 2000)
qtr1st = (ROT + 3000)
qtr2nd = (ROT + 4000)
qtr3rd = (ROT + 5000)
qtr4th = (ROT + 6000)

# CALCULATE TEAM TOTALS ROTATION NUMBERS
result = (ROT * 2) + a
result2 = (ROT * 2) + a + 2
result3 = (ROT * 2) + b
result4 = (ROT * 2) + b + 2
result5 = (ROT * 2) + c
result6 = (ROT * 2) + c + 2



# Print the result to the console
print("CALCULATED ROTATION NUMBERS")
print("1ST HALF")
print(halftime1st)
print("2ND HALF")
print(halftime2nd)
print("QUARTERS ROTATION NUMBERS")
print("1ST QTR")
print(qtr1st)
print("2ND QTR")
print(qtr2nd)
print("3RD QTR")
print(qtr3rd)
print("4TH QTR")
print(qtr4th)
print("\n")

print("FG TEAM TOTALS ROTATION")
print(f"{result} / {result2}")


print("1ST HALF TEAM TOTALS ROTATION")
print(f"{result3} / {result4}")

print("2ND HALF TEAM TOTALS ROTATION")
print(f"{result5} / {result6}")
