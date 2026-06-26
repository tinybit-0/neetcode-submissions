def add_two_numbers() -> int:
    stringg = input()
    stringg_list = stringg.split(",")
    int_list = []
    for i in stringg_list:
        int_list.append(int(i))
    countt = 0
    for j in int_list:
        countt += j
    return countt
# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
