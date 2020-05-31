class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        for i in a:
            self.buffer.append(i)
            if len(self.buffer) == 5:
                result = 0
                for x in self.buffer:
                    result += x
                print(result)
                self.buffer.clear()

    def get_current_part(self):
        return self.buffer
