def add_two_numbers() -> int:
    stringg = input()
    stringg_list = stringg.split(",")
    countt = 0
    for j in stringg_list:
        countt += int(j)
    return countt
# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
