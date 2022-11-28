class Array:
    def __init__(self):
        self.length: int = 0
        self.data: dict = {}

    @property
    def len(self):
        return self.length

    @property
    def show_list(self):
        return self.data

    def get(self, index: int):
        return self.data[str(index)] if str(index) in self.data.keys() else None

    def push(self, item):
        _next = self.len
        self.data[str(_next)] = item
        self.length += 1

    def extend(self, items: list):
        for item in items:
            self.data[str(self.len)] = item
            self.length += 1

    def pop(self):
        last_item = self.data[str(self.len - 1)]
        del self.data[str(self.len - 1)]
        self.length -= 1
        return last_item

    def shift_items(self, index: int):
        for i in range(index, self.len - 1):
            self.data[str(i)] = self.data[str(i+1)]

        del self.data[str(self.len - 1)]
        self.length -= 1

    def delete(self, index: int):
        item = self.data[str(index)]
        self.shift_items(index)
        return item


new_arr = Array()
new_arr.push('hi')
new_arr.push('yes!!')
new_arr.push('this is conquered')
# print(new_arr.pop())
new_arr.extend(['wow', 'this', 'is', 'cool'])
# print(new_arr.pop())

# print(new_arr.get(0))
print(new_arr.show_list)
print(new_arr.len)

new_arr.delete(1)
print(new_arr.len)
