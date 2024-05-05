def dicts() -> None:
    districts = {"brand": "Ford", "model": "Mustang", "year": 1964}
    for x in districts:
        print(districts[x])
    districts.pop("model")


def dict1() -> None:
    thisdict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}

    for x in thisdict1.values():  # noqa
        print(x)
    del thisdict1["model"]
    print(thisdict1)

    thisdict2 = {"brand": "Ford", "model": "Mustang", "year": 1964}
    thisdict2.pop("model")
    print(thisdict2)

    thisdict3 = {"brand": "Ford", "model": "Mustang", "year": 1964}
    for x in thisdict3.keys():
        print(x)
    thisdict3.popitem()
    print(thisdict3)

    thisdict4 = {"brand": "Ford", "model": "Mustang", "year": 1964}
    for x, y in thisdict4.items():
        print(x, y)
    thisdict4.clear()
    print(thisdict4)

    thisdict5 = {"brand": "Ford", "model": "Mustang", "year": 1964}
    x = thisdict5["model"]  # noqa
    for x in thisdict5:
        print(x)
    print(x)

    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    mydict = thisdict.copy()
    print(mydict)

    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    mydict = dict(thisdict)
    print(mydict)


def nested_dict() -> None:
    myfamily = {
        "child1": {"name": "Emil", "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
        "child3": {"name": "Linus", "year": 2011},
    }

    print(myfamily)

    child1 = {"name": "Emil", "year": 2004}
    child2 = {"name": "Tobias", "year": 2007}
    child3 = {"name": "Linus", "year": 2011}

    myfamily = {"child1": child1, "child2": child2, "child3": child3}

    print(myfamily["child2"]["name"])
