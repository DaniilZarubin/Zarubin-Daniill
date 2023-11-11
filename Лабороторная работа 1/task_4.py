users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visit_statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

visit_statistics["Общее количество"] = len(users)

unique_visits = set(users)
visit_statistics["Уникальные посещения"] = len(unique_visits)

print(visit_statistics)
