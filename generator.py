class Iterable:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        for item in self.collection:
            yield item

collection = (4, 5, 6)
iterable = Iterable(collection)
for item in iterable:
    print(item)
