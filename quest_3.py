if __name__ == '__main__':
    list=[12,15,32,42,55,75,122,132,150,180,200]
    l=len(list)
    for i in range(0,l,1):
        if list[i]<=150:
            if list[i]%5==0:
                print(list[i])