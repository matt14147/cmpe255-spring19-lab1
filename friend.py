users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0
    for friendships in friendship:
        if user in friendships:
            count +=1
    return count


def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''

    
    #Add all user with friend_count to list
    num_friends_list = []
    for user in users:
        friends_count = num_friends(user["id"])
        num_friends_list.append({"name": user["name"], "num_friends": friends_count})

    #Sort lists according to num_friends, from most to least
    sorted_list = sorted(
        num_friends_list, key=lambda k: k["num_friends"], reverse=True)
    
    #Print list
    for user in sorted_list:
        print("%s has %d friends" % (user["name"], user["num_friends"]))


sort_by_num_friends()