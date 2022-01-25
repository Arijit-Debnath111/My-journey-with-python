#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0,N):
        ie = input().split();
        if ie[0] == "print":
            print(Output)
        elif ie[0] == "insert":
            Output.insert(int(ie[1]),int(ie[2]))
        elif ie[0] == "remove":
            Output.remove(int(ie[1]))
        elif ie[0] == "pop":
            Output.pop();
        elif ie[0] == "append":
            Output.append(int(ie[1]))
        elif ie[0] == "sort":
            Output.sort();
        else:
            Output.reverse();


# In[ ]:




