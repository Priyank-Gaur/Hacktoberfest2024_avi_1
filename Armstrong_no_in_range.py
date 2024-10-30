A=int(input())
B=int(input())
def print_armstrong_numbers_in_range(A,B):
    for i in range(A,B+1):
        x=i
        summ=0
        count=0
        while x>0:
            x//=10
            count+=1
        x=i
        while x>0:
            a=(x%10)**count
            x//=10
            summ+=a
        if summ==i:
            print(i,end=" ")
print_armstrong_numbers_in_range(A,B)
