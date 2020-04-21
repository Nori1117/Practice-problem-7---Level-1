#Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.
#A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y
#For example, 123 is a seed of 738 as 123*1*2*3 = 738.


def seed_no(number,ref_no):
    #start writing your code here
    n = str(number)
    tot = 1
    for i in n:
        tot = tot*int(i)
    if(tot*number==ref_no):
        return True
    return False
    
number=23
ref_no=138
print(seed_no(number,ref_no))
