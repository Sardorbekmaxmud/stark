n=5
# for i in range(n):
#     for j in range(i,n):
#         print('*',end="  ")
#     print()

# bu = """👆👆👆
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
# """
# for i in range(n):
#     for j in range(n):
#         print("*", end="  ")
#     print()

# bu = """👆👆👆
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# """

# for i in range(n):
#     for j in range(i+1):
#         print("*",end="  ")
#     print()

# bu = """👆👆👆
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# """

# num, space = 5, " "
# for i in range(n):
#     num -= 1
#     print(space*num,end="")
#     for j in range(i+1):
#         print("*",end=' ')
#     print()

# bu = """👆👆👆
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# """

# space,num = " ",-1
# for i in range(n):
#     num += 1
#     print(space*num,end="")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# bu = """👆👆👆
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# """

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="  ")
#     for k in range(i+1):
#         print("*",end="  ")
#     print()

# bu = """👆👆👆
#             *
#          *  *
#       *  *  *
#    *  *  *  *
# *  *  *  *  *
# """

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="  ")
#     for e in range(i,n):
#         print("*",end="  ")
#     print()

# bu = """👆👆👆
# *  *  *  *  *
#    *  *  *  *
#       *  *  *
#          *  *
#             *
# """

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="  ")
#     for k in range(i+1):
#         print("*",end="  ")
#     for e in range(i):
#         print("*",end="  ")
#     print()

# bu = """👆👆👆
#                *
#             *  *  *
#          *  *  *  *  *
#       *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *
# """
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="  ")
#     for k in range(i,n):
#         print("*",end="  ")
#     for e in range(i+1,n):
#         print("*", end="  ")
#     print()

# bu = """👆👆👆
# *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *
#       *  *  *  *  *
#          *  *  *
#             *
# """

# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end="  ")
#     for k in range(i+1):
#         print("*",end="  ")
#     for e in range(i):
#         print("*",end="  ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="  ")
#     for k in range(i,n):
#         print("*",end="  ")
#     for e in range(i+1,n):
#         print("*", end="  ")
#     print()

# bu = """
#                *
#             *  *  *
#          *  *  *  *  *
#       *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *
#       *  *  *  *  *  *  *
#          *  *  *  *  *
#             *  *  *
#                *
# """

# for i in range(n-1):
#    for j in range(i+1):
#       print("*", end=" ")
#    print()
# for i in range(n-2):
#    for j in range(i,n-2):
#       print("*",end=" ")
#    print()

# bu = """👆👆👆
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# """

# for i in range(n-1):
#    for j in range(i,n-1):
#       print(" ", end=" ")
#    for k in range(i+1):
#       print("*", end=" ")
#    print()
# for i in range(n-2):
#    for j in range(i+2):
#       print(" ", end=" ")
#    for k in range(i,n-2):
#       print("*", end=" ")
#    print()

# bu = """
#         *
#       * *
#     * * *
#   * * * *
#     * * *
#       * *
#         *
# """

# for i in range(n-1):
#    for j in range(i+1):
#       print(" ", end="")
#    for k in range(i,n-1):
#       print("*", end=" ")
#    print()
# for i in range(n-2):
#    for j in range(i,n-2):
#       print(" ", end="")
#    for k in range(i+2):
#       print("*", end=" ")
#    print()

# bu = """
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# """

# for i in range(n):
#    for j in range(i,n-1):
#       print(" ", end="")
#    for k in range(i+1):
#       print("*", end=" ")
#    print()
# for i in range(n-1):
#    for j in range(i+1):
#       print(" ", end="")
#    for j in range(i,n-1):
#       print("*", end=" ")
#    print()

# bu = """👆👆👆
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# """

# for i in range(n-2):
#    for j in range(i,n):
#       print(" ", end="")
#    for k in range(i+1):
#       print("*", end=" ")
#    print()
# print("","* "*5)
# for i in range(n-2):
#    for j in range(i+3):
#       print(" ", end="")
#    for j in range(i,n-2):
#       print("*", end=" ")
#    print()

# bu = """
#      *
#     * *
#    * * *
#  * * * * *
#    * * *
#     * *
#      *
# """

# for i in range(n):
#    for j in range(i,n-1):
#       print(" ", end="")
#    for k in range(i+1):
#       print("*", end=" ")
#    for u in range(i,n-1):
#       print(" ", end=" ")
#    for k in range(i+1):
#       print("*", end=" ")
#    print()

# bu = """👆👆👆
#     *         *
#    * *       * *
#   * * *     * * *
#  * * * *   * * * *
# * * * * * * * * * *
# """




# this code determines the largest, medium and smallest 👇👇👇
# number = int(input("Uch xonali son kiriting: "))
# a = number // 100
# b = (number // 10) % 10
# c = number % 10
# if a > b and a > c:
#     print(a*100+b*10+c) if b > c else print(a*100+c*10+b)
# elif b > c:
#     print(b*100+a*10+c) if a > c else print(b*100+c*10+a)
# else:
#     print(c*100+a*10+b) if a > b else print(c*100+b*10+a)
