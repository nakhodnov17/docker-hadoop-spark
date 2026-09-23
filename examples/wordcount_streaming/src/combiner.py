#!/usr/bin/python3

import sys

current_word = None
current_count = 0

sys.stderr.write(f'Run the combiner\n')

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        sys.stderr.write(f'Illegal value: {count}\n')
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f'{current_word}\t{current_count}')
        current_word = word
        current_count = count

# output the last word
if current_word == word:
    print(f'{current_word}\t{current_count}')
