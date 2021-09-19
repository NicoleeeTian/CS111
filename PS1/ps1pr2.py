# 
# ps1pr2.py - Problem Set 1, Problem 2
#
# Indexing and slicing puzzles
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:]
# Put your solutions to the remaining list puzzles below.
answer1 = e[0:2]
answer2 = pi[-2::-2]
answer3 = e[-1::-2]+pi[0:5:2]
print( answer1 )


#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 4)
# Creating the string 'bossy'
answer4 = b[:3] + t[-1] + u[-1]
answer5 = u[:7]+t[1]
answer6 = u[-5]+b[-2]+u[-4]+t[0:3]
answer7 = 3*(u[-1]+t[-3::2])
answer8 = t[0]+t[3:5]+t[-1]+t[0]

# Put your solutions to the remaining string puzzles below.



# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 9):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))
            
            
