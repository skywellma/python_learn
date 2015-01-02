def prod(L):
    return reduce(lambda x,y:x*y,L)

print prod(range(1,5))
