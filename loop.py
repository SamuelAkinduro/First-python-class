#loop control statement 
# for i in range(3):
#     if i==4:
#         pass (break, continue)
#     print(i)
    #coin counter: flip a coin 10 times and count the number of heads  you get.
# import random
# for i in range(10):
#     count=random.randint(0,1)
    
 #coin counter: flip a coin 10 times and count the number of heads  you get.  
import random

# heads = 0

# for i in range(10):
#     coin = random.randint(0, 1)
#     if coin == 1:
#         heads += 1
#         print(coin)
# print("Total heads:", heads)
# #accumulator
# pink_bag=0
# for i in range(5):
#     pink_bag=pink_bag + 100
#     print(pink_bag)
    #now combine both ideas: roll a die 5 times and add up all the rolls
import random
# die_roll = 0
# for i in range(5):
#         die_rolls = random.randint(1, 6)
#         die_roll += die_rolls
# print("Total rolls:", die_roll)
      #two dice: roll two dice 3 times and print the total of each pair.
# two_dice=0
# for i in range(3):
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     two_dice = die1 + die2
#     two_dice += two_dice
# print(two_dice)

#how often does a gambler go broke? 
Money=50
broke_count = 0
happy_count = 0
for i in range(100):
        coin = random.randint(0, 1)
        if coin == 1:
         Money += 1
         happy_count += 1
         print (happy_count)
        else:
          Money -= 1
          broke_count+=1
          if Money <= 0:
              print (f"Gambler went broke after {i+1} tosses!")
              break
          print(f"won: {happy_count} times")
          print(f"Lost: {broke_count} times")
          print (f"final money: {Money}")
          print (f"Broke percentage:{broke_count}%")

     

