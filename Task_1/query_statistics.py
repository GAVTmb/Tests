# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
#
# ]
queries = [
    'Как управлять миром',
    'Как стать самым умным',
    'Что посмотреть вечером',
    'Топ сериалов',
    'Онлайн курсы',
    'Что происходит зарубежом'
]

def query_statistics(queries):
    total_num_of_req = len(queries)
    query_dict = {}
    res = []
    for query in queries:
        count = len(query.split())
        query_dict[count] = query_dict.get(count, 0) +1
    for key in query_dict:
        percentage = round(query_dict[key]/total_num_of_req*100)
        res.append(f'Запросов из {key} слов - {percentage}%')
    return res

# print(query_statistics(queries))