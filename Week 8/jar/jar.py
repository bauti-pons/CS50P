import emoji

class Jar():
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        cookie = emoji.emojize(":cookie:", language="alias")
        return f"{cookie * self.size}"


    def deposit(self, n):
        if n < 0:
            raise ValueError("Incorrect amount")
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Insufficient space")


    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Insufficient cookies")


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or type(capacity) != int:
            raise ValueError("Incorrect capacity")
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 :
            raise ValueError("Not enough cookies")
        self._size = size


