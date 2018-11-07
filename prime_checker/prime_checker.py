def count_primes(num):
    x = 0
    list_2 = []
    def factors(num2):
        list_ = []
        for y in range(2,num2):
            if (num2%y) == 0:
                list_.append(y)
        return list_
    for t in range(2,num):
        l = factors(t)
        if l == []:
            x += 1
            list_2.append(t)
    print('Number of Prime Numbers leading up to your number:')
    print(x)
    print('The Prime Numbers leading up to your number:')
    print(list_2)        

count_primes(int(input('Your number here: ')))
