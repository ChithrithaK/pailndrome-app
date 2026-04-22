def is_palindrome(word: str) -> bool: 
    cleaned = word.lower().replace(" ", "") 
    return cleaned == cleaned[::-1] 
 
if __name__ == "__main__": 
    user_input = input("Enter a word: ") 
    if is_palindrome(user_input): 
        print(f" '{user_input}' is a palindrome!") 
    else: 
        print(f" '{user_input}' is not a palindrome.")