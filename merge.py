def merge():
    """ Asks to enter two lists,their size and merges them in increasing order"""
    a = []
    b = []
    c = []
    d = []
    print "Enter number of elements in first list"
    n = int(raw_input())
    print "enter number of elements in second list"
    m = int(raw_input())
    print "Now Enter the elements of first list"
    for k in range(n):
        a.append(raw_input("enter an element:"))
    print "Now Enter the elements of second list"
    for l in range(m):
        b.append(raw_input("enter an element:"))

    print a
    print b
    
    for i in a:
        c.append(i)
    for j in b:
        c.append(j)
    length = m + n
    for p in range(length):
        temp = c[0]
        for i in c:
            if int(i) <= int(temp):
                temp = i
        d.append(temp)
        c.remove(temp)
    
    
    print 'The merged list in increasing order is:',d
    
        
