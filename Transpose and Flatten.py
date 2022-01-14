#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

m = map(int,input().split())
k = [map(int,input().split()) for _ in xrange(m[0])]

n = np.array(k)
print (np.transpose(n))
print (n.flatten())


# In[ ]:




