if __name__ == '__main__':
    '''imprime de una lista de corredores el runner-up
    osea el segundo'''

    n = int(input())
    arr = map(int, input().split())

    lista = list(set(arr))
    lista.sort(reverse=True)
    print(lista[1])
    