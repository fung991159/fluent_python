class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


r = Record(a='1', b='2')
print(r.a)