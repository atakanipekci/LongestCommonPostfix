#Firstly i used a function called findCommonEnd to find the longest common postfix
#and return it. To do that i just compared the character of the given 2 strings and
#iterated through them starting from the last element. If the corresponding chars are
#not equal then just return the string created so far. Also since we are adding the
#characters to the end of the string we need to reverse it to get the correct order.
#longest_common_postfix_helper just slices the array of strings into 2 halves and does
#the same for both parts until there is only 1 element left. After doing so, it returns the
#common postfix of both halves.
#Time cost with Master Theorem:
#T(n)=2T(n/2)+f(n)
#where f(n) is equal to S(longest string of the array)*n since we have to compare every string
#and go through them char by char.
#T(n)=2T(n/2)+O(Sn) Case 3
#T(n)=O(Sn)


import sys


def findCommonEnd(str,str2):
    
    i=len(str)-1
    j=len(str2)-1
    flag=True;
    common=""
    while(i>=0 and j>=0 and flag==True):
        
        if(str[i]!=str2[j]):
            flag=False;
        else:
            common+=str[i]
        i-=1
        j-=1
    return common[::-1]
    
    

def longest_common_postfix(strArr):
    return longest_common_postfix_helper(strArr,0,len(strArr)-1)

def longest_common_postfix_helper(strArr,start,end):
    if(len(strArr)==1):
        return strArr[0]
    elif(start==end):
        return strArr[start]
    elif(start>end):
        print("how?")
    else:
        middle = (start+end)//2
        a=longest_common_postfix_helper(strArr,start,middle)
        b=longest_common_postfix_helper(strArr,middle+1,end)
        c=findCommonEnd(a,b)
    
        return c




inpStrings = ["absorptivity", "circularity", "electricity","importunity","humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)
#print(findCommonEnd("absorptivity", "circularity"))
#Output: ity