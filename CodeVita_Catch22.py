forward = []
backward = []
distance_covered = 0

def ways_forward(f, b, t, fd, bd):
    
    forward.append(f * t)
    backward.append(b * t)
    
    global distance_covered
    distance_covered += (f - b)
    
    if (distance_covered + f) >= fd:
        forward.append((fd - distance_covered) * t)
        return
    else:
        ways_forward(f, b, t, fd, bd)
        
        
def ways_backward(f, b, t, fd, bd):
    
    forward.append(f * t)
    backward.append(b * t)
    
    global distance_covered
    distance_covered += (b - f)
    
    if distance_covered >= bd:
        backward.append((bd - distance_covered) * t)
        return
    else:
        ways_backward(f, b, t, fd, bd)


N = int(input("Enter the number of test cases:"))

for i in range(0, N):
    F, B, T, FD, BD = map(int, input().split())
    
    if F == B:
        if F >= FD:
            print(str(FD) + ' ' + 'F')
        else:
            print("No Ditch")
            
    elif F > B:
        if F >= FD:
            print(str(FD)+ ' ' + 'F')
        else:
            ways_forward(F, B, T, FD, BD)
            print(str(sum(forward) + sum(backward)) + ' ' + 'F')
            
    else:
        ways_backward(F, B, T, FD, BD)
        print(str(sum(forward) + sum(backward)) + ' ' + 'B')
        
        
    distance_covered = 0
    forward = []
    backward = []
