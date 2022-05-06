def getValue(list, idx, default=""):
    if indexExistInList(list, idx):
        return list[idx]
    else:
        return default


def indexExistInList(list, idx):
    try:
        list[idx]
        return True
    except IndexError:
        return False
