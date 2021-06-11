

def par(numero):
    if numero % 2 == 1:
        return False
    else:
        return True

    


if __name__ == '__main__':

    while True:
        n = int(input().strip())

        if n>100 or n < 1:
            print('numero fuera de limite')
        else:
            if not par(n):
                print('Weird')
            elif par(n) and n>=2 and n<=5:
                print('Not Weird')
            elif par(n) and n>=6 and n<=20:
                print('Weird')
            elif par(n) and n > 20:
                print('Not Weird')
            

   