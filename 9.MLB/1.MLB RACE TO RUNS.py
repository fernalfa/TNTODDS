import re


def remove_lines_with_at_symbol_and_dates(text):
    lines = text.split("\n")
    modified_lines = [line for line in lines if
                      "@" not in line and not re.search(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", line)]
    return "\n".join(modified_lines)


def remove_expression_from_text(text, expression):
    return text.replace(expression, "")


with open('../0.INFO', 'r') as file:
    input_text = file.read()

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

print(final_text)

lines = final_text.strip().split('\n')

second_values = []
for i in range(1, len(lines), 1):  # Change the step to 3 to only process one option per text
    try:
        second_value = int(lines[i])
        second_values.append(second_value)
    except ValueError:
        pass  # Ignore non-numerical lines


print(second_values)

extracted_values = []

for i in range(0, len(second_values), 1):  # Change the step to 3 to only process one option per text
    try:
        extracted_value = int(second_values[i])
        extracted_values.append(extracted_value)
    except ValueError:
        pass

print(extracted_values)
