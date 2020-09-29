'''class simple:
    a=10
    def hi():
        return('welcome Krushik')'''

#addition operation
'''class simple():
    print('operations')
    
    def add():
        a=10
        b=20

        return ('addition of two numbers is',a+b)'''
#Dynamic variables
'''class simple():
    print('Arithmetic operations')

    def add(a,b):
        return ('addition of two number is:',a+b)

a=int(input('enter a value:'))
b=int(input('enter b value:'))
obj=simple.add(a,b)
print(obj)'''

class hello:
    data="welcome Krushik"

    def hii():
        return('good morning')
obj=hello
print(dir(obj))
print(obj.data)
print(obj.hii())

