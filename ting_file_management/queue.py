class Queue:
    def __init__(self):
        self.queue_list = []

    def __len__(self):
        return len(self.queue_list)

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        return self.queue_list.pop(0)

    def search(self, index):
        if index >= 0:
            return self.queue_list[index]
        else:
            raise IndexError('Invalid index')
