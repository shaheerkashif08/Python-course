import re

text = "This is a brown fluufy dog there bites are powerful that make people suffer from anti rabies"

match = re.search("brown", text)
print(match)

if match:
    print("Match found!")
    print("Start index", match.start())
    print("End index", match.end())

# Find All Occurence of patterrrn
matches = re.findall("the", text, re.IGNORECASE) # case sensitive search
print("Matches:", matches)

new_text = re.sub("fox","cat", text)
print("ew_text")