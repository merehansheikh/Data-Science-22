def filter_names(lst):
    filtered = []
    for i in lst:
        if i[2]>30 and i[3] in ('USA','Canada'):
            filtered.append(i[1])
    return filtered

#Sample Run
users = [
  (1, 'Alice', 25, 'USA'),
  (2, 'Bob', 35, 'Canada'),
  (3, 'Charlie', 28, 'UK'),
  (4, 'David', 40, 'USA'),
  (5, 'Eve', 32, 'Canada'),
  (6, 'Frank', 20, 'France'),
]

filtered_names = filter_names(users)
print(filtered_names)

def top_10(lst):
    sorts = sorted(lst, key = lambda lst: lst[2])
    tops = sorts[-10:]
    dicts = dict()
    for i in tops:
        if i not in dicts.keys():
            dicts[i[1]] = 1
        else:
            dicts[i[1]] += 1
    for key,value in dicts.items():
        if value==1:
            print(key)
    return tops

#Sample Run
users = [
    (1, 'Alice', 25),
    (2, 'Bob', 35),
    (3, 'Charlie', 28),
    (4, 'David', 40),
    (5, 'Eve', 32),
    (6, 'Frank', 20),
    (7, 'Alice', 27),
    (8, 'Bob', 25),
    (9, 'Chris', 65),
    (10, 'Black', 34),
    (11, 'Harry', 51)
]
print(top_10(users))