import random
# this below is an empty list which will store 6 random numbers
lotteryNumbers = []
# for loop will generate lottery numbers
for i in range (0,6):
# randint will print a random integer between 1 and 50
  number = random.randint(1,50)
# the while loop will run until the condition of printing 6 random numbers is met
  while number in lotteryNumbers:
# if random number meets the condition then it is added to the list
    number = random.randint(1,50)
  lotteryNumbers.append(number)
# once we have the six numbers, the list is sorted
lotteryNumbers.sort()
print(">>>Today's lottery numbers are: ")
print(lotteryNumbers)








