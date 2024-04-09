
#ex 1 by svara 


#AI delcalration - used AI to fix up the code 
class DLeftHashTable:
    
    #initialize 
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.left_table = [{} for _ in range(entries * buckets)]  # Initialize left table
        self.right_table = [{} for _ in range(entries * buckets)]  # Initialize right table

     #wasnt sure if you wanted the built in one or to make our own so i just made mine    
    def _hash(self, key, table_index):
        return hash(key) % (self.entries * self.buckets) + table_index * self.buckets
    

    #realized we needed two hash tables 
    def left_table_hash(self, key):
        return self._hash(key, 0)

    def right_table_hash(self, key):
        return self._hash(key, 1)
    
    #decide wbere to put the key, value pairs 
    def insert(self, key, value):
        left_index = self._hash(key, 0)
        right_index = self._hash(key, 1)
        
        left_occupancy = len(self.left_table[left_index])
        right_occupancy = len(self.right_table[right_index])
        
        if left_occupancy <= right_occupancy:
            self.left_table[left_index][key] = value
        else:
            self.right_table[right_index][key] = value
    
    #searchs for the keys
    def lookup(self, key):
        left_index = self.left_table_hash(key)
        right_index = self.right_table_hash(key)
    
        if key in self.left_table[left_index]:
            return self.left_table[left_index][key]
        elif key in self.right_table[right_index]:
            return self.right_table[right_index][key]
        else:
            return None


#me testing it 
hash_table = DLeftHashTable(10, 100)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

print(hash_table.lookup("apple"))  # Output: 1, 2, 3, None 
print(hash_table.lookup("banana"))  
print(hash_table.lookup("orange"))  
print(hash_table.lookup("grape"))   

