from tensorflow.python.ops.variable_scope import set_variable_v1


class Partition:
    def __init__(self, n):
        self.particies = [{i} for i in range(n)]
        self.universe_size = n

    def __str__(self):
        return str(self.particies)

    def __len__(self):
        return self.universe_size

    def get_partitions(self):
        return self.particies

    def find_set(self, vertex):
        if type(vertex) != set:
            vertex = {vertex}
        for partition in self.particies:
            if partition.issuperset(vertex):
                return partition
        return set()

    def size(self):
        return len(self.particies)

    def join(self, set1: set, set2: set):
        for i,set in enumerate(self.particies):
            if set == set1:
                self.particies.pop(i)
        for i, set in enumerate(self.particies):
            if set == set2:
                self.particies.pop(i)
        self.particies.append(set1.union(set2))