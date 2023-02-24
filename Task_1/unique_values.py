ids = {"user1": [213, 213, 213, 15, 213],
       "user2": [54, 54, 119, 119, 119],
       "user3": [213, 98, 98, 35]}


def unique_values(dict_id):
    uniq_values = []
    for key, value in dict_id.items():
        for k in value:
            if k in uniq_values:
                ...
            else:
                uniq_values.append(k)
    return uniq_values
