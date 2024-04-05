import random
import string
import matplotlib.pyplot as plt

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



# 1. Generate a list of 1,000,000 random strings (length between 1 and 10; use only uppercase letters, lowercase letters, or digits) [1 pt]

# Function to generate random strings
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

random_strings = [generate_random_string(random.randint(1, 10)) for _ in range(1000000)]



# 2. Generate index values for a table of 1,000 elements, using both hash functions from exercise 1 [1 pt]

# Initialize dictionaries to count collisions
collisions_1 = {}
collisions_2 = {}

for s in random_strings:
    hash_table = DLeftHashTable(10, 1000)  # Creating an instance of the class
    index_1 = hash_table._hash(s, 0)  # Using hash function 1
    index_2 = hash_table._hash(s, 1)  # Using hash function 2
    
    # Count collisions for hash function 1
    collisions_1[index_1] = collisions_1.get(index_1, 0) + 1
    
    # Count collisions for hash function 2
    collisions_2[index_2] = collisions_2.get(index_2, 0) + 1


# 3. For each function, generate a plot with index value on the X axis, and #collisions for that value on the Y axis [1 pt]
    # Note: #collisions here is simply how many strings hash to that particular value
plt.bar(collisions_1.keys(), collisions_1.values())
plt.xlabel('Index Value')
plt.ylabel('# Collisions')
plt.title('Hash Function 1 Collisions')
plt.show()

plt.bar(collisions_2.keys(), collisions_2.values())
plt.xlabel('Index Value')
plt.ylabel('# Collisions')
plt.title('Hash Function 2 Collisions')
plt.show()


# 4. Comment on the results: do the plot shows any “hot spots”? Where? [0.5 pts]
'''
Hot spots are areas where the number of collisions is significantly higher than average.
It might indicate weaknesses in the hash functions.
'''