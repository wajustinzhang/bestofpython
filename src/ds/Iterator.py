class MyIterator():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.x = self.start
        return self

    def next(self):
        x = self.x
        if x > self.end:
            raise StopIteration

        self.x = x + 1 #iterator logic
        return x


if __name__ == '__main__':
    for i in MyIterator(10,20):
        print(i)
