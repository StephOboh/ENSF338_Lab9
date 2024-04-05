import random
import string
import matplotlib.pyplot as plt

# Function to create hash functions from Exercise 1
def hash_function_1(s):
    # Your hash function 1 implementation
    pass

def hash_function_2(s):
    # Your hash function 2 implementation
    pass



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
    index = hash_function_1(s) % 1000
    collisions_1[index] = collisions_1.get(index, 0) + 1

for s in random_strings:
    index = hash_function_2(s) % 1000
    collisions_2[index] = collisions_2.get(index, 0) + 1


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
'''