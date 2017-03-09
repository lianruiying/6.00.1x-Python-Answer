def McNuggets(n):
    a = []
    b = []
    c = []
    for i in range(n):
        if i*6 <= n:
            a.append(i)
        if i*9 <= n:
            b.append(i)
        if i*20 <= n:
            c.append(i)
    #print a,b,c
    for x in a:
        for y in b:
            for z in c:
                #print x,y,z
                if x*6+y*9+z*20 == n:
                    return True
    return False
    
print McNuggets(26)
