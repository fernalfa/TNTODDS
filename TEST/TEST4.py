import re

def remove_lines_with_at_symbol_and_dates(text):
    lines = text.split("\n")
    modified_lines = [line for line in lines if "@" not in line and not re.search(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", line)]
    return "\n".join(modified_lines)

def remove_expression_from_text(text, expression):
    return text.replace(expression, "")
def extract_second_text_line_after_team(text):
    lines = text.split("\n")
    extracted_lines = []
    for i in range(len(lines) - 1):
            extracted_lines.append(lines[i + 1])
    return "\n".join(extracted_lines)

# Example usage
input_text = '''
CLE Guardians @ CHI Cubs
Fri 30 Jun 14:21

2
3
4
5
6
7
CLE Guardians
+115
+130
+170
+225
+320
+450
CHI Cubs
-145
-150
-120
+115
+165
+240
Neither
+5000
+1200
+425
+200
+105
-175

SD Padres @ CIN Reds
Fri 30 Jun 17:10

2
3
4
5
6
7
SD Padres
-175
-160
-145
-115
+115
+160
CIN Reds
+145
+130
+135
+160
+210
+280
Neither
+5000
+3500
+1100
+425
+210
+115
'''

expression_to_remove = '''
2
3
4
5
6
7
'''

# Removing lines with "@" symbol, dates, and the specified expression
text_without_at_and_dates = remove_lines_with_at_symbol_and_dates(input_text)
final_text = remove_expression_from_text(text_without_at_and_dates, expression_to_remove)
ODDS = extract_second_text_line_after_team(final_text)

print(ODDS)
