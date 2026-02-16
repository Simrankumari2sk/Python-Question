'''Q. Write a program to calculate the total amount in the piggybank, given the coins of Rs 10, Rs 5 and Rs 1.'''
num_of_10_coins = int(input("Enter the number of 10 coins in the Piggy Bank : "))
num_of_5_coins = int(input("Enter the number of 5 coins in the Piggy Bank : "))
num_of_2_coins = int(input("Enter the number of 2 coins in the Piggy Bank : "))
num_of_1_coins = int(input("Enter the number of 1 coins in the Piggy Bank : "))
total_amount = num_of_10_coins * 10 + num_of_5_coins * 5 +num_of_2_coins * 2 + num_of_1_coins * 1
print("Total amount in the piggybank =", total_amount)