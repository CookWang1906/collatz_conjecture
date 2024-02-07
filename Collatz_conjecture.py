#status: Completed
#info: Pick a random positive integer. If EVEN then divise, if ODD then multiply the number by 3 and add 1.
n = int(input("Please input your number here: "))
while n < n*n:
    if n % 2==0:
        n = n/2
        print('Down', n)
    else:
        n = n*3 + 1
        print("Up", n)
    if n == 1:
        break