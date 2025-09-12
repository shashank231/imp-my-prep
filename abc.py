

# class SomeClass:

#     def __ini__(self, a, b):

#     @staticmethod
#     def static1(a, b):
#         pass

#     @classmethod
#     def set_class1(cls, a, b):
#         # pass
#         return cls(a, b)

# obj1 = SomeClass()

# obj1.static1

# SomeClass.static1()

# SomeClass.set_class1()





# [[2,6], [5,10], [11,24], [30,32],[33,48],[50,100]]

# [[2,24], [30,48], [50,100]]

# [a, b] [c, d]

# b >= c-1

# [u, c, c, c, u, u, c]
# n, y

import pdb 


def solve1(lst1):

    answer = list()

    len_lst1 = len(lst1)
    index = 1

    tracking = [0]*(len_lst1)
    print("START")
    while (index < len_lst1):
        curr_ele = lst1[index]
        prev_ele = lst1[index-1]
        b = prev_ele[1]
        c = curr_ele[0]
        if b >= c-1:
            # yes collapsable
            tracking[index-1] = "y"
            tracking[index] = "y"
        else:
            # not collapsable
            # tracking[index-1] = "n"
            tracking[index] = "n"
            if tracking[index-1] == "y":
                tracking[index-1] = "y1"

        # pdb.set_trace()
        index += 1

    print(tracking)

l1 =  [[2,6], [5,10], [11,24], [30,32],[33,48],[50,100]]
        #  y       y      y     o           y       n
        # ['y', 'y', 'y1', 'y', 'y1', 'n']
        # [[2, 24], [30, 48], [50, 100]]


solve1(l1)






    