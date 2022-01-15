#!/usr/bin/env python
# coding: utf-8

# In[3]:


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character;
    string = ''.join(l);
    return string


# In[ ]:




