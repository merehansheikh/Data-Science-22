def feedback(dicts):
    fourplus = dict()
    for key,value in dicts.items():
        if value['rating']>=4:
            fourplus[key] = value['rating']
    return fourplus

#Sample Run
user_feedback = {
    1: {'rating': 5, 'comments': 'Excellent product!'},
    2: {'rating': 3, 'comments': 'Could be better.'},
    3: {'rating': 4, 'comments': 'Good overall, but some minor issues.'},
    4: {'rating': 2, 'comments': 'Not satisfied with the purchase.'},
    5: {'rating': 5, 'comments': 'Highly recommend this product!'},
    6: {'rating': 1, 'comments': 'Terrible product, avoid it.'},
    7: {'rating': 4, 'comments': 'Great value for the price.'},
    8: {'rating': 3, 'comments': 'Could use some improvements.'},
    9: {'rating': 5, 'comments': 'Best product I\'ve ever bought!'},
    10: {'rating': 2, 'comments': 'Not worth the money.'}
}

print(feedback(user_feedback))

def top5(dicts):
    tops  = dict()

    sorts = sorted(dicts,key=lambda x:dicts[x]['rating'],reverse=True)
    for  i in range(5):
        tops[sorts[i]] = dicts[sorts[i]]['rating']
    return tops

#Sample Run
user_feedback = {
    1: {'rating': 5, 'comments': 'Excellent product!'},
    2: {'rating': 3, 'comments': 'Could be better.'},
    3: {'rating': 4, 'comments': 'Good overall, but some minor issues.'},
    4: {'rating': 2, 'comments': 'Not satisfied with the purchase.'},
    5: {'rating': 5, 'comments': 'Highly recommend this product!'},
    6: {'rating': 1, 'comments': 'Terrible product, avoid it.'},
    7: {'rating': 4, 'comments': 'Great value for the price.'},
    8: {'rating': 3, 'comments': 'Could use some improvements.'},
    9: {'rating': 5, 'comments': 'Best product I\'ve ever bought!'},
    10: {'rating': 2, 'comments': 'Not worth the money.'}
}

print(top5(user_feedback))

def combine_feedback(dicts1, dicts2):
    combined_fb = {}
    keys1 = list(dicts1.keys())
    keys2 = list(dicts2.keys())
    all_keys = set(keys1+keys2)
    for usr in all_keys:
        if usr in keys1:
            rat1 = dicts1[usr]['rating']
            com1 = dicts1[usr]['comments']
        else:
            rat1 = 0
            com1 = ''
        if usr in keys2:
            rat2 = dicts2[usr]['rating']
            com2 = dicts2[usr]['comments']
        else:
            rat2 = 0
            com2 = ''
        combined_rat = max(rat1, rat2)
        combined_coms = com1 + com2
        combined_fb[usr] = {'rating': combined_rat, 'comments': combined_coms}
    return combined_fb

#Sample Run
user_feedback_1 = {
    1: {'rating': 5, 'comments': 'Excellent product!'},
    2: {'rating': 3, 'comments': 'Could be better.'},
    3: {'rating': 4, 'comments': 'Good overall, but some minor issues.'},
    4: {'rating': 2, 'comments': 'Not satisfied with the purchase.'},
    5: {'rating': 5, 'comments': 'Highly recommend this product!'},
    6: {'rating': 1, 'comments': 'Terrible product, avoid it.'},
    7: {'rating': 4, 'comments': 'Great value for the price.'},
    8: {'rating': 3, 'comments': 'Could use some improvements.'},
    9: {'rating': 5, 'comments': 'Best product I\'ve ever bought!'},
    10: {'rating': 2, 'comments': 'Not worth the money.'}}
user_feedback_2 = {
    1: {'rating': 4, 'comments': 'Great product, but a bit expensive.'},
    11: {'rating': 3, 'comments': 'Could be better, but overall satisfied.'},
    13: {'rating': 5, 'comments': 'Excellent product!'},
    3: {'rating': 2, 'comments': 'Not satisfied with the purchase.'},
    4: {'rating': 4, 'comments': 'Good overall, but some minor issues.'},
}

print(combine_feedback(user_feedback_1,user_feedback_2))