"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!, It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

dic={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}

if b == 'plus':
    for i in dic.keys():
        for j in dic.keys():
            if i == a and j==c:
                res=dic[i]+dic[j]

if b == 'minus':
    for i in dic.keys():
        for j in dic.keys():
            if i == a and j==c:
                res=dic[i]-dic[j]   

print('the result is ',res)




if (not a == 'zero' and not a == 'one' and not a == 'two' and not a == 'three' and not a == 'four' and not a == 'five') or (not c == 'zero' and not c == 'one' and not c == 'two' and not c == 'three' and not c == 'four' and not c == 'five') or (not b == 'plus' and not b == 'minus'):
    print("I am not able to answer this question. Check your input.")

print("Thanks for using this calculator, goodbye :)")
