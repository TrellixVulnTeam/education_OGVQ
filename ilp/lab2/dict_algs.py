def get_parent_names(arr, age):
    persons = []
    for person in arr:
        have = False
        for child in person['children']:
            if child['age'] >= 18:
                have = True
        if have:
            persons.append(person['name'])
    return  persons

ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name" : "uasya",
        "age" : 12,
    }],
}

kate = {
    "name": "kate",
    "age": 34,
    "children": [{
        "name" : "lisa",
        "age" : 18,
    }, {
        "name" : "volk",
        "age" : 21,
    }],
}

lil = {
    "name": "lil",
    "age": 34,
    "children": [{
        "name" : "erk",
        "age" : 13,
    }, {
        "name" : "kol",
        "age" : 55,
    }],
}

print(get_parent_names([ivan, kate, lil], 18))