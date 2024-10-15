def filter_names(lst):
    filtered = []
    for i in lst:
        if i[2]>30 and i[3] in ('USA','Canada'):
            filtered.append(i[1])
    return filtered

def top_10(lst):
    sorts = sorted(lst, key = lambda lst: lst[2])
    return sorts[-10:]

def disp_dup(lst):
    for i in lst:
        if lst.count(i)>1:
            print(i)


