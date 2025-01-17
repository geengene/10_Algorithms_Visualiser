def make_change_1(coin_denoms, change): 
    if change in coin_denoms: 
        return 1 
    
    min_coins = float("inf") 
    for i in [c for c in coin_denoms if c <= change]: 
        num_coins = 1 + make_change_1( coin_denoms, change - i ) 
        min_coins = min(num_coins, min_coins) 
    return min_coins 

print(make_change_1([1, 5, 10, 25], 63))

# In line 3 we are checking our base case; that is, we are trying to make change in the exact amount of one of our coins. If we do not have a coin equal to the amount of change, we make recursive calls for each different coin value less than the amount of change we are trying to make. Line 6 shows how we filter the list of coins to those less than the current value of change using a list comprehension. The recursive call also reduces the total amount of change we need to make by the value of the coin selected. The recursive call is made in line 7. Notice that on that same line we add 1 to our number of coins to account for the fact that we are using a coin. Just adding 1 is the same as if we had made a recursive call asking where we satisfy the base case condition immediately.

def make_change_2(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins

print(make_change_2([1, 5, 10, 25], 63, [0] * 64))

# line 6 we have added a test to see if our table contains the minimum number of coins for a certain amount of change. If it does not, we compute the minimum recursively and store the computed minimum in the table(caching).

def make_change_3(coin_value_list, change, min_coins): 
    for cents in range(change + 1): 
        coin_count = cents 
        for j in [c for c in coin_value_list if c <= cents]: # In this loop we consider using all possible coins to make change for the amount specified by cents.
            if min_coins[cents - j] + 1 < coin_count: 
                coin_count = min_coins[cents - j] + 1 
        min_coins[cents] = coin_count 
    return min_coins[change]

# make_change_3 takes three parameters: a list of valid coin values, the amount of change we want to make, and a list of the minimum number of coins needed to make each value. When the function is done, min_coins will contain the solution for all values from 0 to the value of change.


def make_change_4(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]

def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)

    print("Making change for {} requires the following {} coins: ".format(amnt, make_change_4(clist, amnt, coin_count, coins_used)),end="",)
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)

main()

# The first two lines of main set the amount to be converted and create the list of coins used. The next two lines create the lists we need to store the results. coins_used is a list of the coins used to make change, and coin_count is the minimum number of coins used to make change for the amount corresponding to the position in the list.

# Notice that the coins we print out come directly from the coins_used array. For the first call we start at array position 63 and print 21. Then we take 63 - 21 = 42 and look at the 42nd element of the list. Once again we find a 21 stored there. Finally, element 21 of the array also contains 21, giving us the three 21 cent pieces.