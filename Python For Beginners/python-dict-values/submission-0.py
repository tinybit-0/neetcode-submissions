from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    age_value_list = []
    for ages in age_dict.values():
        age_value_list.append(ages)
    return age_value_list
# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
