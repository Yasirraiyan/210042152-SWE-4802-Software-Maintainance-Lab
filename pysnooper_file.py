import pysnooper
@pysnooper.snoop("trace.log")
def add(a, b):
    return a + b
add(3,4)