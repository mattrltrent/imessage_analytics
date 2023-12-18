import re
import os
from dotenv import load_dotenv

load_dotenv()

match = os.environ.get('MATCH')
chars = 0

def count_lines_and_pattern(file_path):
    global chars
    line_count = 0
    matched_count = 0
    pattern = re.compile(r'{}'.format(match))

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            chars += len(line)
            line_count += 1
            if pattern.search(line):
                matched_count += 1

    return line_count, matched_count

file_path = 'data.txt'
total_lines, total_matched = count_lines_and_pattern(file_path)

print(f"Total lines: {total_lines}")
print(f"Total chars: {chars}")
print(f"Total matched: {total_matched}")
percentage = (total_matched / total_lines * 100) if total_lines > 0 else 0
print(f"Percentage: {percentage:.2f}%")
