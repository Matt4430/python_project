
"""
    九九乘法表------简单又容易忘......
        重点： end=""
        print(str(j)+" * "+str(i)+" = "+str(i*j)+"\t",end="")
    print(" ")
"""

for i in range(1,10):
    for j in range(i):
        j = j+1
        print(str(j)+" * "+str(i)+" = "+str(i*j)+"\t",end="")
    print(" ")