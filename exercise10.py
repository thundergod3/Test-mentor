class Counter:
    def __init__(self):
        self.count = 0
    
    def tick(self):
        self.count = self.count + 1
    
    def reset(self):
        self.count = 0


test = Counter()
print(test.count)
test.tick()
print(test.count)
test.reset()
print(test.count)

