def productivity_score(tasks):

    if not tasks:
        return 0

    done = len([t for t in tasks if t["done"]])
    total = len(tasks)

    return round((done / total) * 100, 2)


def completed(tasks):
    return len([t for t in tasks if t["done"]])


def pending(tasks):
    return len([t for t in tasks if not t["done"]])