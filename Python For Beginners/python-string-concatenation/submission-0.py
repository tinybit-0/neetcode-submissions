def concatenate(s1: str, s2: str) -> str:
    xtr3=s1+s2
    if len(xtr3)>10:
        return "Too long!"
    else:
        return xtr3
    
# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
