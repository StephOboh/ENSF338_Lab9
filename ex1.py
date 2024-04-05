class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.left_table = [{} for _ in range(entries * buckets)]
        self.right_table = [{} for _ in range(entries * buckets)]
        
    def _hash(self, key, table_index):
        # Simple hash function
        return hash(key) % (self.entries * self.buckets) + table_index * self.buckets
    
    def insert(self, key, value):
        left_index = self._hash(key, 0)
        right_index = self._hash(key, 1)
        
        # Find the occupancy of the corresponding buckets
        left_occupancy = len(self.left_table[left_index])
        right_occupancy = len(self.right_table[right_index])
        
        if left_occupancy <= right_occupancy:
            self.left_table[left_index][key] = value
        else:
            self.right_table[right_index][key] = value
    
    def lookup(self, key):
        left_index = self._hash(key, 0)
        right_index = self._hash(key, 1)
        
        if key in self.left_table[left_index]:
            return self.left_table[left_index][key]
        elif key in self.right_table[right_index]:
            return self.right_table[right_index][key]
        else:
            return None

# Example usage
hash_table = DLeftHashTable(10, 100)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

print(hash_table.lookup("apple"))  # Output: 10
print(hash_table.lookup("banana"))  # Output: 20
print(hash_table.lookup("orange"))  # Output: 30
print(hash_table.lookup("grape"))   # Output: None
