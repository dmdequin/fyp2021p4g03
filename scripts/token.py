#Using Christian's code as a base

import re
import sys

line = sys.stdin.readline()

# Initialise lists
tokens = []
unmatchable = []

# Compile patterns for speedup
token_pat = re.compile(r"\w+|#|'")
skippable_pat = re.compile(r'[.,]+')  # typically spaces



# As long as there's any material left...
while line:
    # Try finding a skippable token delimiter first.
    skippable_match = re.search(skippable_pat, line)
    if skippable_match and skippable_match.start() == 0:
        # If there is one at the beginning of the line, just skip it.
        line = line[skippable_match.end():]
    else:
        # Else try finding a real token.
        token_match = re.search(token_pat, line)
        #print(token_match)
        if token_match and token_match.start() == 0:
            #print(line[token_match.start():token_match.end()])
            if line[token_match.start():token_match.end()] == '#':
                token_match2 = re.search(token_pat, line[1:])
                tokens.append(line[:token_match2.end()+1])
                line = line[token_match2.end()+1:]

            elif line[token_match.start():token_match.end()] == "'":
                token_match2 = re.search(token_pat, line[1:])
                tokens.append(line[:token_match2.end()+1])
                line = line[token_match2.end()+1:]
            # If there is one at the beginning of the line, tokenise it.
            else:
                tokens.append(line[:token_match.end()])
                line = line[token_match.end():]
        else:
            # Else there is unmatchable material here.
            # It ends where a skippable or token match starts, or at the end of the line.
            unmatchable_end = len(line)
            if skippable_match:
                unmatchable_end = skippable_match.start()
            if token_match:
                unmatchable_end = min(unmatchable_end, token_match.start())
            # Add it to unmatchable and discard from line.
            unmatchable.append(line[:unmatchable_end])
            line = line[unmatchable_end:]

final_tokens = []
while len(tokens) > 0:
    temp1 = tokens.pop(0)
    try:
        temp2 = tokens.pop(0)
        if temp2[0] == "'":
            temp1 += temp2
            final_tokens.insert(0, temp1)
            print('a', temp1)
        else:
            final_tokens.insert(0, temp1)
            final_tokens.insert(0, temp2)
            print('b', temp1, temp2)
    except:
        final_tokens.insert(0, temp1)
        print('d', temp1)
    
final_tokens = final_tokens[::-1]

print(final_tokens)
print(unmatchable)