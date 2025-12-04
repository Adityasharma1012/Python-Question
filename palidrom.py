# find the weather given number is palidrom or not
def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]
# Example usage
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
