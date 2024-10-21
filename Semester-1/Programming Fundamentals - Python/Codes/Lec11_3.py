def main():
    file = open('numbers1.txt', 'r') #to read six integers from file
    n = int(file.readline())
    print (n, end=' ')
    n = int(file.readline())
    print (n, end=' ')
    n = int(file.readline())
    print (n, end=' ')
    n = int(file.readline())
    print (n, end=' ')
    n = int(file.readline())
    print (n, end=' ')
    n = int(file.readline())
    print (n, end=' ')
    file.close()

main()

