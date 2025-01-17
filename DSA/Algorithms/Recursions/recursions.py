# All recursive algorithms must obey three important laws:
    # 1. A recursive algorithm must have a base case--> allows the algorithm to stop recursing
    # 2. A recursive algorithm must change its state and move toward the base case --> data is modified with each recusion and gets smaller to the base case. 
    # 3. A recursive algorithm must call itself recursively.


def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:]) #function calls itself! This is the reason that we call the list_sum algorithm recursive. A recursive function is a function that calls itself.
    #sum_list([1,2,3,4,5]) calls sum_list([2,3,4,5]) --> to calculate the sum of [1,2,3,4,5], it needs to calculate the sum of [2,3,4,5] and add 1... sum([5]) calls sum([])--> calculate the sum of sum([]) and add 5(base case reached, recrsion breaks). 


print(list_sum([1, 3, 5, 7, 9]))

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base] #returns n = n//base

print(to_str(1453, 16))


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
print(reverse_string("reverse"))


def palindrome_checker(string):
    for char in ["!",",",".",":",";","?","'"," "]: # removing special characters and spaces from string
        if char in string:
            string = string.replace(char,"")
    string = string.lower()
    if len(string) <= 1: #base case
        return True
    if string[0]==string[-1]:
        return palindrome_checker(string[1:-1]) #the string returned gets smaller till len(string)==1
    else:
        return False
        
print(palindrome_checker("radar"))
print(palindrome_checker("Reviled did I live, said I, as evil I did deliver"))



#Tower of Hanoi - With 3 poles, transfer all disks from one pole containing h disks to another, moving only 1 disk at a time and no smaller disk can be below a lerger disk.

# 1. Move a tower of height h-1 from the starting pole to an intermediate pole via the goal pole.
# 2. Move the remaining disk from the starting pole to the final pole.
# 3. Move the tower of height h-1 from the intermediate pole to the goal pole via the starting pole.



def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1: # A tower of one disk will be our base case.
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

# we move all but the bottom disk on the initial tower to an intermediate pole. The next line moves the bottom disk to its final resting place. Then we move the tower from the intermediate pole to the top of the largest disk. The base case is the tower of height 0; in this case there is nothing to do, so the move_tower function returns.

def move_disk(from_p, to_p):
    print("moving disk from", from_p, "to", to_p)

move_tower(6, "A", "B", "C")

# Python provides the stacks that we need implicitly through the call stack.


















    
