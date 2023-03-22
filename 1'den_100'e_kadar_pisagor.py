def pisagor():
    pisagorlist = []
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i ** 2 + j ** 2 == k ** 2:
                    if (k > j > i):
                        pisagorlist.append(((i), (j), (k)))
    return pisagorlist


print(pisagor())



