text = """
CLE Guardians
+120
+135
+175
+230
+325
+450
CHI Cubs
-150
-150
-115
+120
+180
+260
Neither
+4000
+1100
+400
+180
-105
-190
"""

lines = text.strip().split("\n")
expressions = []

for i in range(0, len(lines), 3):
    if i + 2 < len(lines):
        expression = lines[i + 2].strip()
        expressions.append(expression)

print(expressions)
