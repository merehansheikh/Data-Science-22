def unique_users(lst):
    unq = set()
    for user in lst:
        unq.add(user[1])
    return unq

def highest_amount(lst):
    mx = 0
    usr = None
    for user  in lst:
        if  user[2] > mx:
            mx = user[2]
            usr = user
    return usr

def separate(lst):
    trans_id = []
    user_id = []
    for user in lst:
        trans_id.append(user[0])
        user_id.append(user[1])
    return trans_id, user_id

