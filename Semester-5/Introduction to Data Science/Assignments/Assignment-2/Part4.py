def feedback(dicts):
    fourplus = dict()
    for key,value in dicts.items():
        if value['rating']>=4:
            fourplus[key] = value['rating']
    return fourplus

def top5(dicts):
    tops  = dict()

    sorts = sorted(dicts,key=lambda x:dicts[x]['rating'],reverse=True)
    for  i in range(5):
        tops[sorts[i]] = dicts[sorts[i]]['rating']
    return tops



        