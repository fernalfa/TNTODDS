import re
import time
import pyautogui

time.sleep(3)


with open('DATA IBET', 'r') as file:
    lines = file.readlines()

names = []

for line in lines:
    if line.strip().isdigit():
        continue
    if line.strip():
        names.append(line.strip())

print(names)

