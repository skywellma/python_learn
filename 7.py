def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

#for x in fib(6):
#    print x


o = fib(6)

for x in o:
    print x
