
#     for a in range(1, 13):
#         for b in range(1, 13):
#             if a == 1:
#                 print("")
#                 c = 1
#                 while c < 13:
#                     print("\t\t %i x %i  = %-10i" % (a * c, b, ((a * c) * b)), end='')
#                     c += 1

# for a in range(1, 13):
#     print()
#     for b in range(1, 13):
#         print("%i x %i  = %-3i" % (a, b, (a * b)), end='\t\t')

a = 1
while a < 13:
    print()
    b = 1
    while b < 13:
        print("%i x %i  = %-3i" % (a, b, (a * b)), end='\t\t')
        b = b + 1
    a = a + 1

# a = 0
# x = "ACE-CLAN"
# y = len(x)
# while a < y:
#     print(x[a])
#     a = a + 1

