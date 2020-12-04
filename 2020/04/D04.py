from typing import List, Dict
import re


PATTERN_hgt = re.compile(r"^([0-9]{2,3})(cm|in)$")
PATTERN_hcl = re.compile(r"^#[0-9a-f]{6}$")
PATTERN_pid = re.compile(r"^[0-9]{9}$")


def string_to_dict(string, key_val_del=':', items_del=' '):
    items = string.split(items_del)
    # print(items)
    # for k in items:
    #     print(k)
    kvs_list = [kv.split(key_val_del) for kv in items] # if kv
    # for k in kvs_list:
    #     print(k)
    return dict(kvs_list)


def passdata_as_dict(seq: List[str]) -> List[dict]:
    result = []
    while seq:
        record = seq.pop()
        print(record)
        result.append(string_to_dict(record))

    return result


def passdata_validation(passport: Dict) -> bool:
    n_keys = len(passport)

    if n_keys == 8 or (n_keys == 7 and not 'cid' in passport):
        return fields_validation(passport)

    return False


def fields_validation(passport: Dict) -> bool:
    def birth_valid(byr):
        return byr.isdigit() and 1920 <= int(byr) <= 2020

    def issue_valid(iyr):
        return iyr.isdigit() and 2010 <= int(iyr) <= 2020

    def expire_valid(eyr):
        return eyr.isdigit() and 2020 <= int(eyr) <= 2030

    def height_valid(hgt):
        if match := re.match(PATTERN_hgt, hgt):
            num = match.group(1)
            unit = match.group(2)

            if unit == 'cm':
                return 150 <= int(num) <= 193

            if unit == 'in':
                return 59 <= int(num) <= 76

        return False

    def hair_valid(hcl):
        return bool(re.match(PATTERN_hcl, hcl))

    def eye_valid(ecl):
        return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    def pid_valid(pid):
        return bool(re.match(PATTERN_pid, pid))


    return all(
        (
            birth_valid(passport['byr']),
            issue_valid(passport['iyr']),
            expire_valid(passport['eyr']),
            height_valid(passport['hgt']),
            hair_valid(passport['hcl']),
            eye_valid(passport['ecl']),
            pid_valid(passport['pid']),
            )
        )


def n_valid_passports(passports: List[str]) -> int:
    passports = passdata_as_dict(passports)
    count = 0
    for passport in passports:
        count += passdata_validation(passport)

    return count




# for r in records:
#     print(r)
with open('input') as f:
    passports = [
        data.strip().replace('\n', ' ') for data in f.read().split('\n\n')
        ]

print(n_valid_passports(passports))
