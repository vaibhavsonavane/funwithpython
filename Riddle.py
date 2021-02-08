# 3 numbers will be provided at the start.
# Every round 1 will be deducted from 2 of the three numbers.
# The program has to provide the number of count after which deduction will result in -1 of 2/3 numbers.
# eg: [2,3,4]->(2,2,3)->(2,1,2)->(1,1,1)->(0,0,1) -->>> Count = 4


def counter(a, b, c):
    count = 0
    while (a != 0 and b != 0) or (a != 0 and c != 0) or (b != 0 and c != 0):
        picker = 2
        if a > 0 and picker > 0:
            a -= 1
            picker -= 1
        if b > 0 and picker > 0:
            b -= 1
            picker -= 1
        if c > 0 and picker > 0:
            c -= 1
            picker -= 1
        count += 1
        print(f" {a}, {b}, {c}")
    return count


a, b, c = input("a,b,c :  ").split()
print(f"Total iterations is: {counter(int(a), int(b), int(c))} ")
