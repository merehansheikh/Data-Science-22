def main():
    file = open('nums.txt', 'w')
    i = 1
    n = int(input('Enter any integer:'))
    while i <= 10:
        file.write(str(i*n)+'\n')   # to write 10 multiples of the integer
        i = i + 1
    file.close()

main()

