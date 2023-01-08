'''This file is created by AllenSyney'''

def say_hello(name='you'):
    print(f'Hello,{name}')

def my_add(a,b):
    '''This is a simple addition function that add two numbers'''
    return a+b
def test_fstring(name,age):
    print(f'name:{name},age:{age}')

def subtract_test(a,b):
    return a-b
def stash_tess():
    print('This is a test for stash include untracked files')

def compare_tag():
    print('This is an example for test tag compare')
if __name__=="__main__":
    print(say_hello('xianshou123'))
    print(say_hello())
    print(stash_tess)    