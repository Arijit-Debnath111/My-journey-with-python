#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print(hash(t))


# In[ ]:




