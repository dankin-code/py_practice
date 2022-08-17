'''
Closures
# maintain references to objects from eraliern scopes
'''

def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func


'''
Function factory
#function that retuens new, specialized funtion
'''

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

'''
LEGB does not apply when making new bindings

'''