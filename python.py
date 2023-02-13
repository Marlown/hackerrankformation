#2 If  n is odd, print Weird
#If  "is even and in the inclusive range of  to , print Not Weird
#If  "is even and in the inclusive range of  to , print Weird
#If "is even and greater than , print Not Weird
if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0): 
        print("Weird");
    elif (n%2==0 and 2<=n<=5): 
        print("Not Weird") ;
    elif (n%2==0 and 6<=n<=20):
     print("Weird") 
    elif(n%2==0 and n>20): 
        print("Not Weird");
#
#3 The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
##
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (0<=a<10**10 and 0<=b<=10**10):
        som=a+b;
        sous=a-b;
        mul=a*b;
        print(som)
        print(sous)
        print(mul)
##
# 4The provided code stub reads two integers,  and , from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
#No rounding or formatting is necessary.
#Example #
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (b!=0):
        div= a//b;
        di=a/b;
        print(div);
        print(di);
#
# 5
# The provided code stub reads and integer,n , from STDIN. For all non-negative integers , i<n print i**2 .##
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2);
##
# 6 An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#In the Gregorian calendar, three conditions are used to identify leap years:
#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source##
 
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4==0 and year%100!=0):
            leap= True ;
    elif(year%400==0):
            leap = True;
    return leap;
###
#7 The included code stub will read an integer, n, from STDIN.
#Without using any string methods, try to print the following:123....n

#Note that "" represents the consecutive values in between.
# #
if __name__ == '__main__':
    n = int(input())
    if (0<n<150):
        for i in range(1,n+1):
            print(i,end="")
            
#8
# Consider that vowels in the alphabet are a, e, i, o, u and y.
##Function score_words takes a list of lowercase words as an argument and returns a score as follows:
#The score of a single word is  if the word contains an even number of vowels. Otherwise, the score of this word is . The score for the whole list of words is the sum of scores of all words in the list.
#Debug the given function score_words such that it returns a correct score.
#Your function will be tested on several cases by the locked template code.##
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1;
    return score
##
# 9
# #