#filter()

def isntp(n):
    for x in range(2,n):
        if(n%x == 0):
            #print x,n
            return True
    return False

#print isp(3)

print filter(isntp,range(1,101))

    
