from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_index = 0

    def __next__(self):
        item = self.data[self.current_index]

        if not item:
            raise StopIteration()

        self.current_index += 1
        return item
