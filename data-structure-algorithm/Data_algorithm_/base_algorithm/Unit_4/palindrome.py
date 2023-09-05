def palindrome(s):
    qu = []
    st = []

    for x in s:
        if x.isalpha():
            qu.append(x.lower()) 
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
        
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))