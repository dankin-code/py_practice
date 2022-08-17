# LEGB rule
# local, enclosing, global, build-in rule

g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    
    inner()

# Local functions
'''
    useful for specialized, one-off functions
    aid in code organization and readability
    similar to lambdas, but more general
        - may contain multiple expressions
        - may contain statements

'''