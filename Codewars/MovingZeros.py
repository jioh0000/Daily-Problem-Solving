def move_zeros(lst):
    
    cnt = 0
    for i in range(0,len(lst)):
        if lst[i] == 0:
            cnt += 1
    for _ in range(cnt):
        lst.remove(0)
    for _ in range(cnt):
        lst.append(0)
    
    return lst