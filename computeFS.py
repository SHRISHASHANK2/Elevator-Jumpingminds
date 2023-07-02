# known values
N = 7 # number of floors
y1 = 5 
v1_dir = -1
y2 = 1
v2_dir = -1



def computeFS(N=N, y1=y1, v1_dir=v1_dir, y2=y2, v2_dir=v2_dir): 
    FS = 0
    d = abs(y1 - y2)
    
    if (y2 == 0 and v2_dir == -1) or (y2 == N and v2_dir == 1):
##        print('state 0')
        return None
    
    if (y1 >= y2 and v1_dir == -1 and v2_dir == -1) or (y1 <= y2 and v1_dir == 1 and v2_dir == 1):
##        print('satate 1')
        FS = N + 2 - d
    elif (y1 >= y2 and v1_dir == -1 and v2_dir == 1) or (y1 <= y2 and v1_dir == 1 and v2_dir == -1):
##        print('state 3')
        FS = N + 1 - d
    elif v1_dir == 0:
##        print('satate 4')
        FS = N + 1 - d
    elif (y1 > y2 and v1_dir == 1) or (y1 < y2 and v1_dir == -1):
##        print('state 5')
        FS = 1

    return FS

        
# test the FS computation
for y1, v1_dir in [(0, 0), (2, 1), (5, 1), (1, -1), (5, -1)]:
    print('y1:', y1, 'v1_dir:', v1_dir)
    for y2 in range(0, 8):
        print('floor', y2, ': ', computeFS(N, y1, v1_dir, y2, v2_dir))


