'''
    Advance examples

    Create a function that reverses the next string:
    I am Yesi Days
    syaD iseY ma I
'''

string = 'I am Yesi Days'

#Easy way
easyText = string[::-1] #syaD iseY ma I
print(easyText)

#Join
text = "".join(reversed(string))
print(text)

#Loop
def reverse(s):
    x = ''
    for i in s:
        x = i + x
    return x

r = reverse(string)
print(r)
