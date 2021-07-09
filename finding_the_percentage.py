'''
The provided code stub will read in a dictionary containing 
key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name 
provided, showing 2 places after the decimal.
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks.keys():
        lista = student_marks[query_name]
        total = 0
        for item in lista:
            total = total + item

        puntaje = total/len(lista)

    print(f'{puntaje:.2f}')