#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
combined_name = (name1+name2).replace(" ","")
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
total_true = str(t+r+u+e)
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
total_love = str(l+o+v+e)
love_score = int(total_true+total_love)
if 10 > love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")


# In[ ]:





# In[ ]:




