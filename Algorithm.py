#1 focntion de calculs

def solveMeFirst(a,b):
    return (num1+num2);
	# Hint: Type return a+b below


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

# 
import os
import random
import re
import sys

#
# 2 Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    somme = 0;
    for i in range(len(ar)):
        somme = somme + ar[i];
    return(somme);
        
        
    # Write your code here

ar=[1,2,3,10,11]
res=simpleArraySum(ar)
print(res)
#

#3 Given an array of integers, find the sum of its elements.
#For example, if the array 1,3 , so return 6 .
 #
def simpleArraySum(ar): 
    #Write your code here */
    return sum(ar);

#4 Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
#The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
##The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
#If a[i] > b[i], then Alice is awarded 1 point.
#If a[i] < b[i], then Bob is awarded 1 point.
#If a[i] = b[i], then neither person receives a point.
#Comparison points is the total points a person earned.
#Given a and b, determine their respective comparison points.
def compareTriplets(a, b):
    # Write your code here
    alice = 0;
    bob = 0;
    L =[];
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
              bob += 1
        else:
             pass
    L.append(alice);
    L.append(bob);
    return L;


#
# 5 In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
#Function Description
#Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
#aVeryBigSum has the following parameter(s):
#int ar[n]: an array of integers .#
def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)

##
# 6
# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.#
def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)

#7#
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#For example, the square matrix  is shown below:
#1 2 3
#4 5 6
#9 8 9  
#The left-to-right diagonal =15 . The right to left diagonal = 17. Their absolute difference is 2 #
def diagonalDifference(arr):
    # Write your code here
    lrd = []
    rld = []
    j = len(arr[0])
    k = j - 1
    for i in range(j):
        lrd.append(arr[i][i])
        rld.append(arr[i][k-i])
    if sum(lrd) > sum(rld) :
        return sum(lrd) - sum(rld)
    else:
        return sum(rld) - sum(lrd)
#8
#
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  6 places after the decimal.
#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.##

def plusMinus(arr):
    # Write your code here
    a = b = c = 0
    L = []
    for i in arr:
        if i > 0:
            a += 1
        elif i < 0:
            b += 1
        else:
            c += 1
    a = "{:.6f}".format(a/len(arr))
    b = "{:.6f}".format(b/len(arr))
    c = "{:.6f}".format(c/len(arr))
    print(a)
    print(b)
    print(c)
    pass
##9Staircase detail
#This is a staircase of size n=4;
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
#Write aprogram that prints a staircase of size # 

def staircase(n):
    # Write your code here
    for i in range (1,n+1):
        for j in range(1,n-i+1):
            print(' ',end='');
        for j in range(1,i+1):
            print('#', end='')
        print("");


  #10 Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.#     

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    arr1 = arr[:4]
    arr2 = arr[1:]
    print(sum(arr1),sum(arr2))

    # 11-You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.#
    def birthdayCakeCandles(candles):
        # Write your code here
        candles.sort()
        return candles.count(max(candles))
    
    # Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.#
    # 12Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 
#12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.  
def timeConversion(s):
    # Write your code here
    if 'AM' in s:
        if '12:' in s:
            return '00' + s[2:-2]
        else:
            return s[:-2]
    elif 'PM' in s:
        if '12:' in s:
            return s[:-2]
        else:
            hour = str(int(s[0:2]) + 12)
            return hour + s[2:-2]