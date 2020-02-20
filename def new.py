x = 'this is'
def function():
    global x
    x = 'hello'
print(x)
y = function()
print(x)
