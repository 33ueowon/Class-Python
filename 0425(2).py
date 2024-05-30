n = input()
n = int(n)
Sum=1

for i in range(1,n+1):
    Sum *= i
print("{}! = {}".format(n,Sum))
