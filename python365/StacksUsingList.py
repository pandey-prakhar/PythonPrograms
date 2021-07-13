#!/usr/bin/env python
# coding: utf-8

# STACKS CAN BE EASILY FORMED FROM LIST

# In[1]:


stack=[]


# In[2]:


stack.append(4)


# In[7]:


stack.append(7)
print(stack)


# In[8]:


stack[-1]


# CREATING A CLASS THAT CAN CREATE A STACK USING A LIST AND HAVE METHOD ASSOCIATED WITH LIST.

# In[24]:


class Stack():
    def __init__(self):
        self.list_stack=[]
    def is_empty(self):
        if not self.list_stack:#if self.list_stack==0: (it can also be used)
            return True
        else:
            return False
    def push(self,item):
        self.list_stack.append(item)
    def pop(self):
        self.list_stack.pop()
    def peek(self):
        if self.list_stack==[]:
            return None 
        else :
            return(self.list_stack[-1])
    def __repr__(self):#prints the instance or just prints the things of object , not very clear but it prints
        return repr(self.list_stack)
        


# In[25]:


nstack=Stack()


# In[26]:


nstack.is_empty()


# In[27]:


nstack.push(5)


# In[28]:


nstack.push(4)


# In[29]:


nstack.__repr__()


# In[30]:


nstack.peek()


# In[31]:


nstack.pop()


# In[32]:


nstack.peek()


# In[33]:


nstack.is_empty()


# In[ ]:




