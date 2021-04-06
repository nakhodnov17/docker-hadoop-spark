#!/usr/bin/python3

import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, current_count))

# #!/usr/bin/python
#
# import sys
#
# # current_key, current_count = None, 0
# # for line in sys.stdin:
# #     key, value = line.strip().split(' ')
# #     if current_key != key:
# #         if current_key is not None:
# #             sys.stdout.write(f'{current_key} {current_count}\n')
# #         current_key, current_count = key, 0
# #     current_count += 1
