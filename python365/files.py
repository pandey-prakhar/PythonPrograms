# =============================================================================
# s=open('prakhar.txt','w')
# s.write('i am a noob in pubg and want to learn and play more of it ,\nbut iam busy in different things')
# s.close()
# =============================================================================
# =============================================================================
# s=open('prakhar.txt','r')
# print(s.readline()) #read one by one
# print(s.readlines()) #convert the contents in list
# =============================================================================
#FUNCTIONS
#1st Fibinacci
def fib(n):
    '''
    Function to calculate fibonacci 

    Parameters
    ----------
    n : TYPE, optional
        DESCRIPTION. The default is int(input('enter count')).

    Returns
    -------
    None.

    '''
    a=0
    b=1
    for i in range(1,n+1):
        
        a,b=b,a+b
    return(int(a))
#2nd Mean of numbers in a list

# =============================================================================
def fib_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)
#the program above this can print a nth number in fibonacci series, below program prints whole seriesl.
# =============================================================================
# m=int(input('enter count- '))
# for i in range(0,m+1):
#     print(fib_1(i),end=' ')
# =============================================================================
# =============================================================================
# from timeit import Timer
# t1=Timer(fib(20))
# =============================================================================
