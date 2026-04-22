import app 
 
def test_palindrome_true(): 
    assert app.is_palindrome("madam") is True 
    assert app.is_palindrome("racecar") is True 
 
def test_palindrome_false(): 
    assert app.is_palindrome("hello") is False 
    assert app.is_palindrome("python") is False