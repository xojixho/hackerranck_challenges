if __name__ == '__main__':
    n = int(input())
    string = ''

    if 1<=n<=150:
        for i in range(1,n+1):
            string += f'{i}'
            
        print(string)
    else:
        pass    
