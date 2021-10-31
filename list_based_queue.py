class ListQueue:
    """Constructor de la clase"""
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        """Agregar un nuevo elemento"""
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        """Borrar un elemento"""
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        """Recorrer la lista"""
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])