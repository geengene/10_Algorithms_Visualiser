class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data): # adds new key-value pair to the map. If key is already in the map, replace it with new value
        hash_value = self.hash_function(key, len(self.slots))
        # assumes that there will eventually be an empty slot unless the key is already present in self.slots. It computes original hash value and if that slot is not empty, iterates the rehash function until an empty slot. If non-empty slot already contains the key, the old data value is replaced with the new data value. 
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (self.slots[next_slot] is not None and self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots))
                
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key%size
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def get(self, key): # takes a key and returns the matching value
        start_slot = self.hash_function(key, len(self.slots))
        # computes intial hash value. If value is not in intial slot, rehash is used to locate next possible slot. 
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot: # guarentees that search is terminated by checking to make sure we have not returned to original slot.
                    return None
                
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
print(h.slots)
print(h.data)
print(h[20])
print(h[17])
h[20] = "duck"
print(h[20])
print(h[99])
        
# We stated earlier that in the best case hashing would provide an o(1) , constant time search technique. However, due to collisions, the number of comparisons is typically not so simple. Even though a complete analysis of hashing is beyond the scope of this text, we can state some well-known results that approximate the number of comparisons necessary to search for an item. The most important piece of information we need to analyze the use of a hash table is the load factor, ⋋.

# Conceptually, if ⋋ is small, then there is a lower chance of collisions, meaning that items are more likely to be in the slots where they belong. If ⋋ is large, meaning that the table is filling up, then there are more and more collisions. This means that collision resolution is more difficult, requiring more comparisons to find an empty slot. With chaining, increased collisions means an increased number of items on each chain.

# As before, we will have a result for both a successful and an unsuccessful search. For a successful search using open addressing with linear probing, the average number of comparisons is approximately 1/2*(1 + 1/(1-⋋)) and an unsuccessful search gives 1/2*(1 + 1/(1-⋋)^2). If we are using chaining, the average number of comparisons is 1 + ⋋/2  for the successful case, and simply ⋋ comparisons if the search is unsuccessful.






