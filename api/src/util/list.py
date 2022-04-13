class UtilList:
    @classmethod
    def getValue(cls, list, idx, default=""):
        if cls.indexExistInList(list, idx):
            return list[idx]
        else:
            return default

    @classmethod
    def indexExistInList(cls, list, idx):
        try:
            list[idx]
            return True
        except IndexError:
            return False
