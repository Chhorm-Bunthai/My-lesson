s_list = ['tbc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

# print(len(s_list[0]))
# print(len(s_list[1]))
# print(len(s_list[2]))
# print(len(s_list[3]))
# print(len(s_list[4]))
# print(len(s_list[5]))
shortest = s_list[0]
longest = s_list[0]

for i in s_list :
    if len(i) <= len(shortest):
        shortest = i
        print(i)
    elif len(i) > len(longest):
        longest = i
# print(shortest)
# print(longest)




