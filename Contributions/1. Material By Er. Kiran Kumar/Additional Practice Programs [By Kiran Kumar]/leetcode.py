class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1 
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1 
            while left < right  and not s[right].isalnum():
                right -= 1 
            if s[left].lower() != s[right].lower():
                return False 
            left += 1
            right -= 1 
        return True  
      



class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystring = s.lower()
        for char in mystring: 
            if char in [0,1,2,3,4,5,6,7,8,9]:
                mystring.remove(char)
        for char1 in mystring:
          if char1 == " ":
            final = mystring.replace(" ","").replace(",","").replace(":","")
        # print(final)

            reverse = final[::-1]
        if final == reverse:
          return True 
        else: 
          return False 

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))

          