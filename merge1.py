def merge1():
    """ Asks to enter two lists,their size and merges them in increasing order"""
    a = []
    b = []
    c = []
    
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
    
    i = 0
    j = 0
    while(i < n or j < m):
        if(i < n and j < m):
            if(int(a[i]) < int(b[j])):
                c.append(int(a[i]))
                i = i + 1
            else:
                c.append(int(b[j]))
                j = j + 1
        elif(i < n and j >= m):
            c.append(int(a[i]))
            i = i + 1
        else:
            c.append(int(b[j]))
            j = j + 1
        
    print c
        
        
        
        
