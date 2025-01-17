# A hash table can be searched in O(1) time. each position of the hash table is a slot, which can hold an item and is named by an integer. eg. a hash table of 11 slots are named 0 -10.

# The mapping between an item and the slot is called the hash function. 

# Remainder method: takes an item and divides it by the table size, returning the remainder as its hash value.           --> (h(item)) = item%11). eg for items [54, 26, 93, 17, 77, 31], the remainder method returns hash values [10, 4, 5, 6, 0, 9]. so slot 9 would contain item 31. 

hash_value = [ 0,    1,    2,    3,  4,  5,  6,    7,    8,  9,  10]
items =      [77, None, None, None, 26, 93, 17, None, None, 31,  54]

# load factor, ⋋, is no_of_items/table_size

# A perfect hash function maps each item to a unique slot. one way is to increase the table size so each possible value can be accommodated, but this is not feasible when number of items is large, eg. mapping 9 digit social security numbers requires almost 1 billion slots.

# Our goal is to create a hash function that minimizes the number of collisions(more than 1 item is hasehd to the same slot), is easy to compute, and evenly distributes the items in the hash table. it has to be effecient so that it does not become the dominant part of the storage and search process.

# Folding method: divide the item into equal sized pieces and then added together to give the resulting hash value. eg. the phone number 436-555-4601 divided into groups of 2(43, 65, 55, 46, 01) and added together gives 210. Assuming our hash table has 11 slots, we implement the remainder method, 210%11 = 1. so the phone number hashes to slot 1.

# Mid-square method: square the item, and extract a portion of the resulting digits. eg. 44^2 = 1936, extracting the middle two digits, 93, we perform remainder method, 93%11 = 5. 

# Hash functions for character based items like strings: each character in a word is a sequence of oridnal values, eg. "cat"--> ord("c") = 99. we can add them and use remainder method to get a hash value. 

def hash_str(a_string, table_size):
    return sum([ord(ch) for ch in a_string]) % table_size

print(hash_str("tac", 11))
print(hash_str("cat", 11))

# however, anagrams will always return the same hash value, thus a modificated could be to use the positional value as a weighting factor. 

def hash_str_mod(a_string, table_size):
    return sum([ord(ch) * (a_string.index(ch)+1) for ch in a_string]) % table_size


print(hash_str_mod("tac", 11))
print(hash_str_mod("cat", 11))



# COLLISION RESOLUTION a perfevt hash function is often not possible, thus we need ways to resolve a collision.
# open addressing: start at the original hash value position and move in a sequantial manner(circularly) through the slots until the first slot that is empty. 

# Linear probing: systematically visiting each slot at a time. for items [54, 26, 93, 17, 77, 31, 44, 55, 20], a collision occurrs when attempting to place 44 at slot 0, and the next empty slot is 1. 55 is placed in slot 2, and 20 is placed in slot 3 as slot 9, 10, 0, 1 and 2 are occupied. A hash table built using linear probing must utilise the same method to search for items--> when looking for 20, slot 9 is occupied by 30, thus we must do a sequential search starting at slot 10, until we find 20 at slot 3, or an empty slot(in the case 20 is not an item in the hash table). A disadvantage of linear probing is clustering, where many collisions occur at the same hash value, thus surrounding slots will be filled by linear probe resolutions, as we see when slotting in 20(cluster of slot 0 items 77, 44, 55).

# new_hash = rehash(old_hash)
# rehash(pos) = (pos+1)%size

hash_value = [0,  1,  2,  3,  4,  5,  6,  7,    8,    9,  10]
items =      [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]

# to prevent this we can skip slots to potentially reduce clustering. eg. using a "plus 'skip'" probe where we look at every 3rd slot when resolving a collision until we find an empty slot. rehash(pos) = (pos+skip)%size. The size of the skip must be such that all slots of the table will eventually be visited, thus table size is recommended to be prime number

# Quadratic probing: rehash(pos) = (h + i^2)%size

# Inserting 44:
# Initial hash: ( h(44) = 44 % 11 = 0 ) (collision with 77)
# We'll use quadratic probing to find the next available position.
# ( h(44) + 1^2 ) = 0 + 1 = 1
# Place 44 at index 1 in the hash table.

# Inserting 55:
# Initial hash: ( h(55) = 55 % 11 = 0 ) (collision with 77)
# We'll use quadratic probing to find the next available position.
# ( h(55) + 1^2 ) = 0 + 1 = 1 (collision with 44)
# ( h(55) + 2^2 ) = 0 + 4 = 4 (collision with 26)
# ( h(55) + 3^2 ) = 0 + 9 = 9 (collision with 31)
# ( h(55) + 4^2 ) = 0 + 16 = 16 (16 % 11 = 5) (collision with 93)
# We wrap around: ( h(55) + 5^2 ) = 0 + 25 = 25 (25 % 11 = 3)
# Place 55 at index 3 in the hash table.

# Inserting 20:
# Initial hash: ( h(20) = 20 % 11 = 9 ) (collision with 31)
# We'll use quadratic probing to find the next available position.
# ( h(20) + 1^2 ) = 9 + 1 = 10 (collision with 54)
# ( h(20) + 2^2 ) = 9 + 4 = 13 (13 % 11 = 2) 
# Place 20 at index 2 in the hash table.

# Now, the final hash table looks like this:
hash_value = [ 0,  1,  2,  3,  4,  5,  6,    7,    8,  9, 10]
items =      [77, 44, 20, 55, 26, 93, 17, None, None, 31, 54]


# Chaining: allow each slot to hold a reference to a collection of items, allowing many items to occupy the same slot. When searching for an item, we use the hash function to generate the slot where it should reside. The advantage of chaining is that on average there are likely to be fewer items in each slot, so the search is more effecient.

# Let's say we have a hash table of size 5, and we want to insert the following key-value pairs:

# 1. (Key: 10, Value: "apple")
# 2. (Key: 7, Value: "banana")
# 3. (Key: 18, Value: "orange")
# 4. (Key: 23, Value: "grape")
# 5. (Key: 5, Value: "pineapple")
# 6. (Key: 32, Value: "watermelon")

# We'll use a hash function to determine the index in the hash table. For simplicity, let's use the modulo operator with the key.

# 1. Inserting (10, "apple"):
# - ( h(10) = 10 % 5 = 0 )
# - Place ("apple") in the slot 0.

# 2. Inserting (7, "banana"):
# - ( h(7) = 7 % 5 = 2 )
# - Place ("banana") in the slot 2.

# 3. Inserting (18, "orange"):
# - ( h(18) = 18 % 5 = 3 )
# - Place ("orange") in the slot 3.

# 4. Inserting (23, "grape"):
# - ( h(23) = 23 % 5 = 3 ) (collision with "orange")
# - Instead of replacing "orange", we'll use chaining.
# - Create a linked list at slot 3 and add ("grape") to it.

# 5. Inserting (5, "pineapple"):
# - ( h(5) = 5 % 5 = 0 ) (collision with "apple")
# - Create linked list at slot 0 and add ("pineapple") to it.

# 6. Inserting (32, "watermelon"):
# - ( h(32) = 32 % 5 = 2 ) (collision with "banana")
# - Add ("watermelon") to the linked list at slot 2.

# Now, the hash table with chaining looks like this:

Index = [0 , 1 , 2 , 3 , 4]
Value: [("apple") -> ("pineapple"), ("banana") -> ("watermelon") , ("orange") -> ("grape") ] # type: ignore

# In this example, chaining handles collisions by allowing multiple values to be stored at the same slot in the hash table. Each slot contains either a single value or a linked list of values for keys that hash to the same index.

