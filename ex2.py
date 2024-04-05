import random
import string
import matplotlib.pyplot as plt

# WORK FROM EX1
class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.left_table = [{} for _ in range(entries * buckets)]
        self.right_table = [{} for _ in range(entries * buckets)]
  
    def _hash(self, key, table_index):
        return hash(key) % (self.entries * self.buckets) + table_index * self.buckets
    
    def insert(self, key, value):
        left_index = self._hash(key, 0)
        right_index = self._hash(key, 1)
        
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

# Function to generate a random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

# Generate a list of 1,000,000 random strings
random_strings = [generate_random_string(random.randint(1, 10)) for _ in range(1000000)]



# 2. Generate index values for a table of 1,000 elements, using both hash functions from exercise 1 [1 pt]

def hash_function(key, entries, buckets, table_index):
    return hash(key) % (entries * buckets) + table_index * buckets

indices_left_table = [hash_function(string, 1000, 1, 0) for string in random_strings]
indices_right_table = [hash_function(string, 1000, 1, 1) for string in random_strings]


# 3. For each function, generate a plot with index value on the X axis, and #collisions for that value on the Y axis [1 pt]
    # Note: #collisions here is simply how many strings hash to that particular value

def calculate_collisions(indices):
    collision_count = {}
    for index in indices:
        if index in collision_count:
            collision_count[index] += 1
        else:
            collision_count[index] = 1
    return collision_count

left_collisions = calculate_collisions(indices_left_table)
right_collisions = calculate_collisions(indices_right_table)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(left_collisions.keys(), left_collisions.values())
plt.title('Left Table Collisions')
plt.xlabel('Index Value')
plt.ylabel('# Collisions')

plt.subplot(1, 2, 2)
plt.bar(right_collisions.keys(), right_collisions.values())
plt.title('Right Table Collisions')
plt.xlabel('Index Value')
plt.ylabel('# Collisions')

plt.tight_layout()
plt.show()


# 4. Comment on the results: do the plot shows any “hot spots”? Where? [0.5 pts]
'''
"Hot spots" in this context would refer to index values where the number of collisions is significantly higher than the surrounding values, which would show as spikes in the plot.
Both plots exhibit a pattern of periodic spikes, indicating that there are indeed "hot spots" where collisions are notably more frequent. 
These are visible as vertical lines where the number of collisions sharply peaks. For instance, on both the left and right plots, 
there are spikes at regular intervals across the index values.
These "hot spots" could be indicative of a hash function that does not distribute values evenly, 
or of some pattern in the data that is causing more frequent collisions at specific points. The regularity of the spikes suggests 
a systematic issue rather than random chance. Identifying and addressing the cause of these "hot spots" could be important 
for improving the performance of whatever system or algorithm is being analyzed here.

he hotspots in these plots, representing "Left Table Collisions" and "Right Table Collisions," are the index values where there are significantly more collisions than the rest. In both plots, these hotspots are depicted as tall spikes which are much higher than the majority of the data points.

Upon close inspection, these spikes appear to occur at regular intervals. To identify the exact index values of the hotspots, we would ideally use the data from which these plots are generated. However, even without the raw data, it's noticeable that the spikes occur roughly every 50 to 100 index values. If patterns are consistent, they might be occurring at multiples of a specific number. For a more precise analysis, the data used to generate these plots would be needed, as would a closer examination of the x-axis labels to pinpoint the exact index values of the spikes.
'''