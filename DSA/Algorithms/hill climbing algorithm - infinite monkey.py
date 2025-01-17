#  The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

# write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

# See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.


import random
import string


def genstr(strlen):
  alphabets = "abcdefghijklmnopqrstuvwxyz ,.!"
  result = ""
  for i in range(strlen):
    ranCh = random.choice(list(alphabets))
    result += ranCh
  return result

def score(goal,teststring):
  score = 0
  fullmarks = len(goal)
  for i in range(fullmarks):
    if teststring[i] == goal[i]:
      score += 1 
  return score/fullmarks

def main():
  goalstring = input("input string: ")
  best_string = genstr(len(goalstring))
  best_score = score(goalstring,best_string)
  
  generation = 0

  while best_score < 1:
    new_string = list(best_string)
    index = random.randint(0,len(goalstring)-1)
    new_string[index] = random.choice(string.ascii_lowercase + ' ,.!')
    new_string = ''.join(new_string)

    new_score = score(goalstring,new_string)

    if new_score > best_score:
      best_string = new_string
      best_score = new_score

    if generation % 1000 == 0:
      print(f"generation: {generation}, best string: {best_string}, best score: {round(best_score,5)}")
    
    generation += 1

  print(f"generation: {generation}, best string: {best_string}, best score: {best_score}")

main()

    
    


