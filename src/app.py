import sys
import os
import string


def palindrome(s):
    # your code goes here
    possible = set(string.ascii_lowercase)
    s = s.lower()
    s = ''.join([char for char in s if char in possible])
    return s == s[::-1]

def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
