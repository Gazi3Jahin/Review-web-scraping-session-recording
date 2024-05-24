#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests_html


# In[5]:


pip install requests-html nest_asyncio


# In[9]:


import requests
from bs4 import BeautifulSoup
url = "https://www.prothomalo.com/bangladesh/district/l9iivxgmt0"

response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

print(soup.find('h1').text)
all_paragraphs = soup.find_all('p')

for paragraph in all_paragraphs:
    print(paragraph.text)




# In[ ]:




