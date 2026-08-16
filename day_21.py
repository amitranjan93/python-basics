class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def set(self, key, value):
        index = key % 10
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = key % 10
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = key % 10
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.remove(pair)
                return

        return None

    def contains(self,key):
        index = key % 10
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return True
        return False

ht = HashTable()

ht.set(1234, "Simran")
ht.set(5674, "Rahul")
ht.set(9999, "Amit")
print(ht.table)
ht.delete(9999)
print(ht.contains(1234))