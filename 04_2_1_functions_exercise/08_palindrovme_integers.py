def palindrome(num):
    if num == num[::-1]:
        return True
    return False


numbers = input().split(', ')
for num in numbers:
    print(palindrome(num))