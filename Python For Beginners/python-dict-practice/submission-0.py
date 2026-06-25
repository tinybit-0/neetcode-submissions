from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    countt = {}
    for i in word:
        if i not in countt:
            countt[i] = 1
        elif i in countt:
            countt[i] += 1 
    return countt



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
