#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
n,m,p = map(int,input().split())
array_1 = [list(map(int, input().split())) for i in range(n)]
array_2 = [list(map(int, input().split())) for i in range(m)]
print(numpy.concatenate((array_1, array_2), axis = 0))


# In[ ]:




