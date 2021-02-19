def move(n, start, finish):
    if n == 1:
        print(f"|    {n}   |    {start}  |    {finish}   |")
    else:
        tmp = 6 - start - finish
        move(n-1, start, tmp)
        print(f"|    {n}   |    {start}  |    {finish}   |")
        move(n-1, tmp, finish)
