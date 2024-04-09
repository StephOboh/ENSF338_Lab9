
import random
import string
import matplotlib.pyplot as plt

# AI USED FOR CREATION OF PLOTS

# EX1 Hash functions
def _hash(key, entries, buckets, table_index):
    return hash(key) % (entries * buckets) + table_index * buckets

def left_table_hash(key, entries, buckets):
    return _hash(key, entries, buckets, 0)

def right_table_hash(key, entries, buckets):
    return _hash(key, entries, buckets, 1)


# 1. Generate a list of 1,000,000 random strings (length between 1 and 10; use only uppercase letters, lowercase letters, or digits) [1 pt]

# Function to generate a random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

# Generate a list of 1,000,000 random strings
random_strings = [generate_random_string(random.randint(1, 10)) for _ in range(1000000)]

# 2. Generate index values for a table of 1,000 elements, using both hash functions from exercise 1 [1 pt]

# Generate index values for both hash functions
left_indices = [left_table_hash(s, entries=10, buckets=100) for s in random_strings]
right_indices = [right_table_hash(s, entries=10, buckets=100) for s in random_strings]

# 3. For each function, generate a plot with index value on the X axis, and #collisions for that value on the Y axis [1 pt]
    # Note: #collisions here is simply how many strings hash to that particular value


# Calculate collision counts
left_collision_counts = [left_indices.count(i) for i in range(1000)]
right_collision_counts = [right_indices.count(i) for i in range(1000)]

# Plotting
plt.figure(figsize=(10, 5))

# Left Table Hash
plt.subplot(1, 2, 1)
plt.plot(range(1000), left_collision_counts)
plt.title('Left Table Hash')
plt.xlabel('Index Value')
plt.ylabel('Number of Collisions')

# Right Table Hash
plt.subplot(1, 2, 2)
plt.plot(range(1000), right_collision_counts)
plt.title('Right Table Hash')
plt.xlabel('Index Value')
plt.ylabel('Number of Collisions')

plt.tight_layout()
plt.show()


# 4. Comment on the results: do the plot shows any “hot spots”? Where? [0.5 pts]

'''
"Hot spots" in this context would refer to index values where the number of collisions is significantly higher than the surrounding values, which would show as spikes in the plot.
Both plots exhibit a pattern of periodic spikes, indicating that there are indeed "hot spots" where collisions are notably more frequent. 


'''










