print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

#combine both names in order to easily obtain the count of the specific letter
true_score = name1.lower() + name2.lower()
love_score = name1.lower() + name2.lower()

t_count = true_score.count('t')
r_count = true_score.count('r')
u_count = true_score.count('u')
e_count = true_score.count('e')

true_total = t_count + r_count + u_count + e_count

l_count = love_score.count('l')
o_count = love_score.count('o')
v_count = love_score.count('v')
ee_count = love_score.count('e')

love_total = l_count + o_count + v_count + ee_count

true_love_score = str(true_total) + str(love_total)
true_love_total = int(true_love_score)


if true_love_total < 10 or true_love_total > 90:
    print(f"Your score is {true_love_total}, you go together like coke and mentos.")
elif true_love_total >40 and true_love_total < 50:
    print(f"Your score is {true_love_total}, you are alright together.")
else:
    print(f"Your score is {true_love_total}")

