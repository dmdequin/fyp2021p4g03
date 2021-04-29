import re

#line = 'A cat sat on the mat. His name was Måns.'
#line = 'friendship at its finest. ....#pixar #toystory #buzz #woody #friends #friendship #bff…'
line = "No I don't have any carrots!! #seattlepoloclub #horse #horses @ Seattle Polo &amp; Equestrian Club"

# Initialise lists
tokens = []
unmatchable = []

# Compile patterns for speedup
token_pat = re.compile(r'#*[a-zA-Z0-9_]+')
skippable_pat = re.compile(r'\s+')  # typically spaces

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
        if token_match and token_match.start() == 0:
            # If there is one at the beginning of the line, tokenise it.
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

print(tokens)
print(unmatchable)