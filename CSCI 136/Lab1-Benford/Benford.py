# -----------------------------------------------------------------------------
# 
# File Name: Benford.py
#
# Author: Jacob Sriraman
#
# Credits: Guidance from Douglas Galarus
#
# Description:  Implements object-oriented programming to open and read a text
#               file composed of numbers, and determine how many times an integer
#               (0-9) occurs in the nth digit of each number in the file. It will
#               output a list of how many times each integer occurs. This is useful
#               in determining whether a given dataset is compliant with 
#               Benford's law.
#
# How to use:   Use in the command line, with two input arguments: the nth digit 
#               that you want to count and the text file you want to read
#
# Example use: python Benford.py 0 TestData.txt
#
# -----------------------------------------------------------------------------

# Import sys for command line arguments
import sys

# Create class for Benford methods, which build upon each other to 
# create final main loop output 
class Benford:

    print("---------------------------------------------------------------")
    # Initialize members of the class.
    def __init__(self):
        pass

    # Returns the number of digits in the number num.
    def countDigits(self, num):
        count = 0
        if num == 0:
            return 1
        # Uses loop to repeat floor division by 10 until num = 0
        while num != 0:
            num //= 10
            count += 1
        return count
        
    # Returns the digit at the nth position from the right
    # in the number num
    def nthDigitBack(self, n, num):
        if n >= len(str(num)):
            return -1
        # Repeats floor division by 10 until num is one digit
        while n != 0:
            num //= 10
            n = n - 1
        # Returns the last digit, modulo by 10 for the remainder
        # Which is the nth digit from the right
        return num % 10
    
    # Returns the digit at the nth position from the left
    # in the number num
    def nthDigit(self, n, num):
        digits = self.countDigits(num)
        if n >= len(str(num)):
            return -1
        # Uses its relationship with nthDigitBack to return the digit nth from the left
        ans = self.nthDigitBack(digits-(n+1),num)
        return ans
        
    # Updates and returns the tally list with a new count
    # based on the corresponding digit n in the number num.
    def nthDigitTally1(self, n, num, tally):
        # Create blank list that will eventually be added to tally
        blankList = [0,0,0,0,0,0,0,0,0,0]
        if n >= len(str(num)):
            return tally
        digit = self.nthDigit(n,num)
        
        # Add tally to certain digit of blankList
        blankList[digit] = 1
        
        # Add values of lists into new list
        return [i + j for i,j in zip(blankList,tally)]
    
    # Returns a tally list of all digits in the nth position.
    def nthDigitTally(self, n, nums):
        # Create list of 10 0s
        tally = [0]*10
        for num in nums:
                # Compile all digits into the tally list
                tally = self.nthDigitTally1(n,num,tally)
        return tally
    
    # Opens a file and reads all the numbers into a list.
    # Assumes the first number is the count of subsequent numbers
    # in the file and does not include that number in the list.   
    def readMysteriousNumbers(self, fName):
        nums = []
        with open(fName, 'r') as f:
            # Turn each line into type int
            lines = int(f.readline())
            # Read each line seperately with for loop
            for i in range(0,lines):
                # Add each line to list nums
                nums.append(int(f.readline()))
            f.close()
            return nums
# Main function, outside of Benford class. Creates final tally of digits
if __name__ == '__main__':
    ben = Benford()
    nums = ben.nthDigitTally(int(sys.argv[1]), ben.readMysteriousNumbers(sys.argv[2])) 
    # Create output in specified format
    for i in range(0, len(nums)):
        print(str(i) + "s: " + str(nums[i]))
    
    
    
    
        
            
     
        
        
        
            
        
    
       
        
