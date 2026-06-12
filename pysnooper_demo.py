import pysnooper
@pysnooper.snoop()
def square(x):
    y=x*x
    return y
square(5)