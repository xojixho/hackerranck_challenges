if __name__ == '__main__':
    '''imprime  solo las listas que su suma es menor que un numero'''    

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([item for item in [[a, b, c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0, z+1)]
     if sum(item) != n])