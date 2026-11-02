# Day 3 Solution
import string

def is_palindrome(text: str) -> bool:
    # Strip punctuation and whitespace, then lowercase the string
    clean_text = "".join(char.lower() for char in text if char not in string.punctuation and not char.isspace())
    
    # Compare the cleaned text to its reverse
    return clean_text == clean_text[::-1]

# Test driver
if __name__ == "__main__":
    phrases = ["A man, a plan, a canal: Panama", "Python programming", "Racecar"]
    for p in phrases:
        print(f"'{p}' is a palindrome? {is_palindrome(p)}")
