# O(log n) complexity as the maximum number of comparisons is logarithmic with respect to number of items in the list.

#Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# Problem
#     We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
# Input
#     cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
#     query: A number, whose position in the array is to be determined. E.g. 7
# Output
#     position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 1

def find_card(cards, query):
	low, high = 0, len(cards) - 1

	while low<=high:  
		mid = (low + high)//2
		mid_no = cards[mid]
		if mid_no == query:
			return(mid)
		elif mid_no < query:
			high = mid - 1
		elif mid_no > query:
			low = mid + 1
	return False

print(find_card(cards, query))



# Recursive binary search
def binary_search_rec(a_list, item):
	if len(a_list) == 0:
		return False
	
	midpoint = len(a_list) // 2
	if a_list[midpoint] == item:
		return True
	elif item < a_list[midpoint]:	
		return binary_search_rec(a_list[:midpoint], item)
	else:
		return binary_search_rec(a_list[midpoint + 1 :], item)
	
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_rec(test_list, 3))
print(binary_search_rec(test_list, 13))




