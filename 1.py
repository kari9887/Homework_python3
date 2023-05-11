A= int(input("Введите число: "))
B= int(input("Введите степень:"))
def func(A,B):
    if (B==0):
        return (1)
    if (B==1) :
        return(A)
    if (B !=1):
        return(A* func(A,B-1))
print(func(A,B))