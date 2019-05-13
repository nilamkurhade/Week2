


import math
import random
import time

import numpy as np


class TestFunctional:
    """ demo program """

    @staticmethod
    def dipslay(name):  # it is static function which accepts string parameter
        print(name)  # printing name


    """ ====  harmonic numbers  ====="""

    @staticmethod
    def harmonic(n):  # it is a static method which accepts int values
        sum = 0  # initial sum =0
        for i in range(1, n, 1):  # starts form 1 , up to n and increment by 1
            sum = sum + float(1 / i)  # converting decimal values into floating values
        print("harmonic sum = ", sum)  # printing the sum

    """ ====  prime factors   ====="""

    @staticmethod
    def primefact(n):  # it is a static method which accepts int values
        for i in range(2, n, 1):  # range start from 2 ,n condition,increment by 1
            count = 0  # initial count =0
            while n % i == 0:  # n % i ==0  goes to inside while loop
                n = n / i  # divide n by i
                count += 1  # count increment by 1
                print("prime factors: ", i, "^ ", count)  # i ^ count(number of time i divides n)

    """ ====  gambler gaming concepts  ====="""

    @staticmethod
    def gambler(stake, goals, no_of_times):  # it is a static method which accepts 3 parameter stake,goals,no_of_times
        wins = 0                             # wins and bets are initializes to 0
        bets = 0
        for i in range(no_of_times):         # for loops up to given no_of_times
            cash = stake                     # cash initialize to stake
            while 0 < cash < goals:          # condition in while loop cash greater than 0 and lesser than goals
                bets += 1                    # bets increment by 1
                x = random.randint(1, 10)    # randomly chosen between 1 to 10
                if x > 5:                    # cash increments by 10 ,else decrements by 10
                    cash += 10
                else:
                    cash -= 10

            if cash == goals:                 # checks cash==goals
                wins += 1                     # wins will increments by 1

        print(wins, " wins of ", no_of_times)  # prints  wins out of no_of_times
        print("Percent of games won =", 100.0 * wins // no_of_times)  # print wining in percent
        print("Avg # bets           =", 1.0 * bets // no_of_times)  # print Avg bets  in percent

    """ ====  coupon generator concepts  ====="""

    @staticmethod
    def coupon_generator(no_of_coupons):  # it is a static method which accepts int values numbers of coupons to generate
        my_list = []                  # using the list to hold coupons
        count = 0                         # initial count is 0
        while len(my_list) < no_of_coupons:  # while runs un-till condition comes false

            x = random.randint(0, no_of_coupons)  # takes random between 0 to no_of_coupons
            count += 1                            # count will increment by 1
            if x not in my_list:                  # if x is not in my_list add to list
                my_list.append(x)

        print("total random number needed to have all distinct  numbers are : ", count)  # print distinct coupons
        print(my_list)  # print list

    """ ====  two-dimensional array concepts  ====="""

    @staticmethod
    def two_dimensional_array(m, n):  # it is a static method which accepts int values m(rows),n(columns)
        arr = [[0 for i in range(m)] for j in range(n)]  # arr with m rows and n columns
        for i in range(m):  # for i from m row
            for j in range(n):  # for j from n cols
                arr[i][j] = int(input("enter array element.."))  # reading user input and storing to the array
        array = np.array(arr)  # numpy is used for multidimensional arrays
        print(array)  # printing the array elements

    """ ====  finding triplets in an given arrays  ====="""

    @staticmethod
    def triplets(arr):  # it is a static method which accepts array values
        my_triplets = list()  # creating a  list variable
        count = 0  # initialize  count = 0
        for i in range(0, len(arr)):  # range 0 to len(arr)
            for j in range(i + 1, len(arr)):  # range i+1 to len(arr)
                for k in range(j + 1, len(arr)):  # range j+1 to len(arr)
                    if arr[i] + arr[j] + arr[k] == 0:  # checking the condition  array contents of i+j+k==0
                        if arr[i] not in my_triplets or arr[j] not in my_triplets or arr[
                            k] not in my_triplets:  # ignore duplicate
                            my_triplets.append(arr[i])  # appending array elements i
                            my_triplets.append(arr[j])  # appending array elements j
                            my_triplets.append(arr[k])  # appending array elements k
                            count += 1  # count increment by 1 for every triplets
        if count == 0:  # if count == 0 no triplets are found.
            print("triplets not found in given inputs...")
        else:
            print("founded triplets counts are: ", count)  # print triplets count
        print("triplets are: ", my_triplets)  # printing the list values triplets

    """ ====  distance problem  ====="""

    @staticmethod
    def distance(x, y):  # it is a static method which accepts int values X,Y
        px = pow(x, 2)  # x pow of 2
        py = pow(y, 2)  # y pow of 2
        result = px + py  # result =  x pow of 2 + y pow of 2
        square = math.sqrt(result)  # square root( x pow of 2 + y pow of 2 )
        print("distance is:", square)  # print result

    """ ====  start_stop_elapsed time   ====="""

    @staticmethod
    def start(choice):  # it is a static method which accepts int choice
        if choice == 1:  # check for if condition
            startTimer = time.time()  # assigns the start time =  epoch(time.time())
        return startTimer  # returns the startTime

    @staticmethod
    def stop(choice, start):  # it is a static method which accepts 2 integers choice and start
        if choice == 0:  # check for if condition to validate choice
            stopTimer = time.time() - start  # epoch(time.time())-start
        print("elapse time :", stopTimer, "secs..")  # print the elapsed time

    """@staticmethod
    def elapsed():                                           # it is a static method which accepts none
        elapsedTime = t.stopTimer - t.startTimer  # subtraction of start time and end time gives elapse time
        print("elapsed time: ", elapsedTime)   """  # print the elapsedTime

    """ ==== quadratic_equation  ====="""

    @staticmethod
    def quadratic_equation(a, b, c):  # it is a static method which accepts int values of a,b,c
        d = (b * b) - (4 * a * c)  # formula d = b^2 - 4ac
        if d > 0:  # if d > 0
            print("roots are real and unequal")
            root1 = (-b + math.sqrt(d)) / (2 * a)  # root1 = -b + square root of d divide by 2*a
            root2 = (-b - math.sqrt(d)) / (2 * a)  # root2 = -b + square root of d divide by 2*a
            print("first root :", root1)  # print root1,root2
            print("second root :", root2)

        elif d == 0:  # if condition d==0
            print("roots are real and equal")
            root1 = (-b + math.sqrt(d)) / (2 * a)  # root1 = -b + square root of d divide by 2*a
            print("first root :", root1)  # print root1
        else:
            print("roots are imaginary...")  # else roots are imaginary

    """ ====  wind chill problem  ====="""

    @staticmethod
    def wind_chill(t, v):  # it is a static method which accepts int values of t(temprature) and v(wind speed)
        # windchill1 = 0
        if t < 50 and 3 < v > 120:  # temp greater than 50 and wind speed should greater than 3 and  lesser than 120
            windchill1 = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
            # formula to find wind speed given by pre-defined standard
        print("wind chill is :", windchill1)  # print the result

    @staticmethod
    def permutation(string):  # it is a static method which accepts String as input
        if len(string) == 1:  # if length of string is 1 print as it is
            return string
        recursive_perm = []  # declaring list
        for i in string:
            for perm in t.permutation(string.replace(i, '', 1)):  # calling recursive function
                print(perm)
                recursive_perm.append(i + perm)  # appending  characters to list
        return recursive_perm  # return list

        """=================ALGORITHM PROBLEMS========================="""

        """ =========anagram problem =========="""

    @staticmethod
    def anagram(str1, str2):  # it is a static method which accepts two String as str1,str2
        if sorted(str1) == sorted(str2):  # sorting of str1 and str2 are equals it is anagram else not
            print("given strings are anagram \n ")  # if condition true print anagram
        else:
            print("given strings are not anagram \n ")  # else print not a anagram

        """ ========== prime numbers ==========="""

    @staticmethod
    def is_prime(start, end):  # it is a static method which accepts 2 int as parameter start and end parameter

        for val in range(start, end):  # taking user inputs from range start to end
            if val > 1:  # if val is greater than 1 moves to inner loop
                for n in range(2, val):  # range stars from 2 up to val
                    if (val % n) == 0:  # val % n == 0,then it is not a prime numbers
                        break  # exits from a program
                else:
                    print("prime values of given number is:", val)  # prints prime numbers for given range

        """ ====  Bubble_Sort problem   ====="""

    @staticmethod
    def bubble_sort(arr):  # it is a static method which accepts int as parameter
        start = t.start(1)
        print("start time is :", start, "secs...")
        temp = 0  # temp initialize to 0

        for i in range(0, len(arr)):  # for range start from 0 to len(arr)-1,increment by 1
            for j in range(i + 1, len(arr)):  # for range start from 1 to len(arr),increment by 1
                if arr[i] > arr[j]:  # checks swapping condition
                    temp = arr[j]  # swaps the elements
                    arr[j] = arr[i]
                    arr[i] = temp
        t.stop(0, start)

        return arr  # returns the sorted array

        """ ====  Binary_Search problem   ====="""

    @staticmethod
    def binary_search(arr, key):  # it is static function which accepts 2 inputs array,Key
        start = t.start(1)
        print("start time is :", start, "secs...")

        start = 0  # initialize start to 0
        end = len(arr) - 1  # end to length of array -1

        while start <= end:  # start less than end true enter to inner loop
            mid = (start + end) // 2  # finds mid

            if key == arr[mid]:  # checks key equal to array of mid
                return mid  # if yes,return mid element
            elif key < arr[mid]:  # if less than mid
                end = mid - 1  # initialize end to mid-1
            else:
                start = mid + 1  # initialize start to mid+1
        t.stop(0, start)
        return -1  # return -1 element is not found

        """ ====  Insertion_sort problem   ====="""

    @staticmethod
    def insertion_sort(arr):
        start = t.start(1)
        print("start time is :", start, "secs...")
        for i in range(1, len(arr)):
            currentvalue = arr[i]
            pos = i
            while pos > 0 and arr[pos - 1] > currentvalue:
                arr[pos] = arr[pos - 1]
                pos = pos - 1
                arr[pos] = currentvalue
        t.stop(0, start)
        return arr

        """ ====  Merge_sort problem   ====="""

    @staticmethod
    def merge_sort(arr):
        result = []
        if len(arr) < 2:
            return arr
        mid = int(len(arr) / 2)
        i, j = 0, 0
        left = t.merge_sort(arr[:mid])
        right = t.merge_sort(arr[mid:])

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]

        return result

        """ =======================  prime numbers of anagram  ======================="""

    @staticmethod
    def prime_number(n):
        my_list = []
        pm_list = []
        for i in range(0, n):
            if i > 1:
                result = True
                for j in range(2, i):
                    if i % j == 0:
                        result = False
                        break
                if result:
                    pm_list.append(i)
                    my_list.append(str(i))   # use here my_list.append(str(i))
        print("===prime numbers range n  are as follows......\n")
        print("prime numbers are:", pm_list)
        return my_list
        # return pm_list
    """============ code used for the printing 2D-prime Numbers=========="""
    @staticmethod
    def prime_number1(n):
        my_list = []
        pm_list = []
        for i in range(0, n):
            if i > 1:
                result = True
                for j in range(2, i):
                    if i % j == 0:
                        result = False
                        break
                if result:
                    pm_list.append(i)
                    my_list.append(str(i))   # use here my_list.append(str(i))
        print("===prime numbers range n  are as follows......\n")
        print("prime numbers are:", pm_list)
        # return my_list
        return pm_list

    @staticmethod
    def anagram_prime(my_list):
        my_list1 = list()
        result = False
        size = len(my_list)
        for i in range(size):
            for j in range(i + 1, size):
                if sorted(my_list[i]) == sorted(my_list[j]):
                    my_list1.append(int(my_list[i]))
                    result = True
        ang_list = list()
        if result:
            print("=====list of anagram prime numbers are:====")
            for i in range(len(my_list1)):
                ang_list.append(int(my_list1[i]))
        print(ang_list)
        return ang_list

    @staticmethod
    def palindrome(n):
        rev = 0
        temp = n
        while n > 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10
        if rev == temp:
            return temp
        """ ====  prime numbers for anagram  ====="""

    """ ==================  Vending Machine ====================="""

    @staticmethod
    def vending_machine(money, notes):
        rem = 0
        for i in range(0, len(notes), 1):
            if money >= notes[i]:
                callNotes = money // notes[i]
                rem = money % notes[i]
                money = rem
                total = int(callNotes)
                print(notes[i], "Notes ===>", callNotes)
        t.vending_machine(money, notes)  # vending_machine(money, notes)
        print("total notes in Vending Machines are: ", total)

    """ ======================  DAY_OF_WEEK   ============================="""

    @staticmethod
    def day_of_week(day, month, year):
        """y0 = y - (14 - m) // 12
        x = y0 - y0 // 4 - y0 / 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if d == 0:
            return "SUNDAY"
        elif d == 1:
            return "MONDAY"
        elif d == 2:
            return "TUESDAY"
        elif d == 3:
            return "WEDNESDAY"
        elif d == 4:
            return "THURSDAY"
        elif d == 5:
            return "FRIDAY"
        elif d == 6:
            return "SATURDAY"
        else:
            return "invalid entry" """
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                  9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        weeks = {0: 'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        y0 = year - (14 - month) // 12
        x = y0 - y0 // 4 - y0 // 100 + y0 // 400
        m0 = month + 12 * ((14 - month) // 12) - 2
        d0 = (day + x + 31 * m0 // 12) % 7
        print("Day of a week:", weeks[d0], "\t", "Month:", months[month], "\t", "Year:", year)
        return d0

    @staticmethod
    def monthlyPayment(p, y, r):
        n = 12 * y
        r0 = r / (12 * 100)
        payment = (p * r0) / (1 - math.pow(1 + r0, -n))
        print("monthly payment :", payment)

    @staticmethod
    def question_number(low, high):
        if (high - low) == 1:
            return low
        mid = int(low + high) / 2
        print("its your number less than:", mid, '?', "press 1 to yes or,press 0 to no \n")
        a = int(input())
        if a == 1:
            return t.question_number(low, mid)
        elif a == 0:
            return t.question_number(mid, high)
        else:
            print("invalid numbers\n")
            return 0
        print(a)

    @staticmethod
    def sqrt(n):  # taking input int n from user
        temp = n
        epilson = 1e-15
        while math.fabs(temp - n / temp) > epilson * temp:
            temp = ((n / temp) + temp) / 2
        print("square root of ", n, "is:", temp)  # prints the square root of n

    @staticmethod
    def decimalToBinary(num):
        if num > 1:
            t.decimalToBinary(num // 2)

        bin = num % 2
        print(bin, end=" ")

    @staticmethod
    def toBinary(str1):
        while len(str1) != 8:
            str1 = "0"+str1
        print("binary number after padding:", str1)
        mid = len(str1) / 2
        part1 = str1[:int(mid)]
        part2 = str1[int(mid):]
        print("part1:", part1)
        print("part2:", part2)
        new_str = part2 + part1
        print("after padding:", new_str)
        new_no = int((new_str), 2)
        print("new number is", new_no)
        if t.isPowerOfTwo(new_no):
            print("yes,it is power of two\n")
        else:
            print("no,it is not power of 2 \n")

    @staticmethod
    def log(x):
        return math.log10(x) / math.log10(2)

    @staticmethod
    def isPowerOfTwo(new_no):
        return math.ceil(t.log(new_no)) == math.ceil(t.log(new_no))


t = TestFunctional()  # creating reference of TestFunctional
