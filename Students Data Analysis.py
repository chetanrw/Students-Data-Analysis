#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
pd.options.display.max_columns = 9999


# In[2]:


student_data=pd.read_csv('C:\\Users\\Chetan\\Desktop\\student-mat.csv')


# This dataset contains information about the life of students of mathematical courses and their academic success. So let's examine in detail the information about the students and find out what influences their grades the most.

# In[3]:


student_data.head()


# In[4]:


student_data.columns


# __Let's see which age group of students we are dealing__

# In[5]:


sns.catplot(x="age", kind="count", data=student_data, height = 5)
plt.title('age of students')
plt.show()


# And so, basically we are dealing with students 15-22 years ,mostly are of 15-19

# __Let's look at the gender of our students. Count the number of boys and girls.__

# In[6]:


sns.catplot(x="sex", kind="count",data=student_data, height = 5)
plt.title("Gender of students : F - female,M - male")


# In[7]:


student_data['sex'].value_counts(normalize=True)


# So 52%(approx) of data is female and 48%(approx) is male

# In[8]:


student_data['studytime'].value_counts()


# In[9]:


labels = ['<2 hours','2 - 5 hours','5 - 10 hours','> 10 hours']
values = student_data["studytime"].value_counts().tolist()

fig1, ax1 = plt.subplots()
ax1.pie(values,labels=labels, autopct='%1.1f%%',
        shadow=True)
ax1.axis('equal') 

plt.show()


# Most students spend 2 to 5 and 5 to 10 hours a week studying. It would be better if we had the exact number of hours for each student.

# In[10]:


plt.figure(figsize=(18,7))
plt.title("Box plot for final grades,depending on the study time")
sns.boxplot(y="studytime", x="G3", data = student_data , orient="h", palette = 'rainbow')


# In[11]:


student_data[student_data['studytime']==1]['G3'].mean()


# In[12]:


student_data[student_data['studytime']==2]['G3'].mean()


# In[13]:


student_data[student_data['studytime']==3]['G3'].mean()


# In[14]:


student_data[student_data['studytime']==4]['G3'].mean()


# The lowest average result is shown by students who spend less than two hours a week studying.Few students spend more than 10 hours a week studying. and they are showing a very good result

# In[15]:


sns.catplot(x="address", kind="count",hue = "traveltime", data=student_data, height = 5)
plt.title("Students address: U - urban, R - rural")


# time that students spend on the way to school ( 1 - very close, 4 - very far).

# Most of the students live in the city. Few students take long to get to school.

# __Let's see the effect of absence based on Urban or Rural areas__

# In[16]:


f= plt.figure(figsize=(18,7))

ax=f.add_subplot(121)
sns.distplot(student_data[(student_data['address'] == 'U')]["absences"],color='orange',ax=ax)
ax.set_title('Distribution of absences for students who live is city')

ax=f.add_subplot(122)
sns.distplot(student_data[(student_data['address'] == 'R')]['absences'],color='gray',ax=ax)
ax.set_title('Distribution of absences for students who live in village')


# There is not much difference between absence of students living in city and students living in village

# In[17]:


student_data['famsize'].value_counts()


# In[18]:


plt.figure(figsize=(18,7))
plt.title("Box plot for final grades,depending on the familysize")
sns.boxplot(y="famsize", x="G3", data = student_data , orient="h", palette = 'rainbow')


# In[19]:


student_data[student_data['famsize']=='GT3']['G3'].mean()


# In[20]:


student_data[student_data['famsize']=='LE3']['G3'].mean()


# students with family size <= 3 has little less average grade than students whose family size > 3 but this is not giving us as much information about grade score

# In[21]:


student_data.head()


# Relationship status

# In[22]:


sns.catplot(x="age", kind="count",hue = "romantic", data=student_data, height = 5)
plt.title("Relationship status with age")


# In[23]:


sns.catplot(x="romantic", kind="count",data=student_data, height = 5)
plt.title("relationship status of students ")


# count of single students are more than students with relationship

# __Now let's see how relationship status affect grades__

# In[24]:


f= plt.figure(figsize=(18,7))

ax=f.add_subplot(121)
sns.distplot(student_data[(student_data['romantic'] == 'yes')]["G3"],color='orange',ax=ax)
ax.set_title('Distribution of grades for students who are in relationship')
mean=student_data[student_data['romantic']=='yes']['G3'].mean()
median=student_data[student_data['romantic']=='yes']['G3'].median()


ax.axvline(mean, color='r', linestyle='--')
ax.axvline(median, color='g', linestyle='-')

ax=f.add_subplot(122)
sns.distplot(student_data[(student_data['romantic'] == 'no')]['G3'],color='gray',ax=ax)
ax.set_title('Distribution of grades for students who are single')

mean=student_data[student_data['romantic']=='no']['G3'].mean()
median=student_data[student_data['romantic']=='no']['G3'].median()



ax.axvline(mean, color='r', linestyle='--')
ax.axvline(median, color='g', linestyle='-')


# As seen from the graph avg score of grades of single students is more than students with relationship

# In[25]:


f= plt.figure(figsize=(17,5))

ax=f.add_subplot(121)
sns.distplot(student_data[(student_data.romantic == 'no')]["absences"],color='coral',ax=ax)
ax.set_title('Distribution of absences for classes by single people')

mean=student_data[student_data['romantic']=='no']['absences'].mean()
median=student_data[student_data['romantic']=='no']['absences'].median()
ax.axvline(mean, color='r', linestyle='--')
ax.axvline(median, color='g', linestyle='-')

ax=f.add_subplot(122)
sns.distplot(student_data[(student_data.romantic == 'yes')]['absences'],color='purple',ax=ax)
ax.set_title('Distribution of absences for classes by people in love')
mean=student_data[student_data['romantic']=='yes']['absences'].mean()
median=student_data[student_data['romantic']=='yes']['absences'].median()
ax.axvline(mean, color='r', linestyle='--')
ax.axvline(median, color='g', linestyle='-')


# Single people miss fewer classes than people in love

# In[26]:


student_data['Talc'] = student_data['Dalc'] + student_data['Walc']


# In[28]:


student_data[student_data['romantic']=='no']['Talc'].count()


# In[29]:


student_data[student_data['romantic']=='yes']['Talc'].count()


# In[30]:


f= plt.figure(figsize=(17,5))

ax=f.add_subplot(121)
sns.distplot(student_data[(student_data['romantic'] == 'no')]["Talc"],color='coral',ax=ax)
ax.set_title('Distribution of absences for classes by single people')

mean=student_data[student_data['romantic']=='no']['Talc'].mean()
median=student_data[student_data['romantic']=='no']['Talc'].median()
ax.axvline(mean, color='r', linestyle='--')
ax.axvline(median, color='g', linestyle='-')

ax=f.add_subplot(122)
sns.distplot(student_data[(student_data['romantic'] == 'yes')]['Talc'],color='purple',ax=ax)
ax.set_title('Distribution of absences for classes by people in love')
mean=student_data[student_data['romantic']=='yes']['Talc'].mean()
median=student_data[student_data['romantic']=='yes']['Talc'].median()
ax.axvline(mean, color='r', linestyle='--')
ax.axvline(median, color='g', linestyle='-')


# - On an average single people and commited people drink 3 times a week.
# - Count of single drinkers are more than commited

# __Amount of alcohol and health__

# In[31]:


student_data['health'].value_counts(normalize=True)


# It can be seen that around 11% students health conditions are extremely bad.

# 36% of students health comditions are very good

# In[32]:


plot1 = sns.factorplot(x="Walc", y="health", hue="sex", data=student_data)
plot1.set(ylabel="Health", xlabel="Weekend Alcohol Consumption")


plot2 = sns.factorplot(x="Dalc", y="health", hue="sex", data=student_data)
plot2.set(ylabel="Health", xlabel="Weekend Alcohol Consumption")


# __Alcohol consumption and Grade__

# In[33]:


plot1 = sns.factorplot(x="G3", y="Walc", data=student_data)
plot1.set(ylabel="Final Grade", xlabel="Weekend Alcohol Consumption")

plot2 = sns.factorplot(x="G3", y="Dalc", data=student_data)
plot2.set(ylabel="Final Grade", xlabel="Workday Alcohol Consumption")


# __Health vs grade__

# In[34]:


plt.title("Box plot for final grades,depending on current health")
sns.boxplot(y="health", x="G3", data = student_data , orient="h", palette = 'winter',showmeans=True)


# In[35]:


plt.figure(figsize=(16,5))
plt.title("Box plot for absences,depending on current health")
sns.boxplot(y="health", x="absences", data = student_data , orient="h", palette = 'summer',showmeans=True)


# There is no tangible connection between the level of health of the student and the number of absences to classes.

# In[36]:


f= plt.figure(figsize=(17,5))

ax=f.add_subplot(121)
sns.distplot(student_data[(student_data.Dalc == 5)]["G3"],color='red',ax=ax)
ax.set_title('Distribution of grades for people who consume a lot of alcohol on weekdays')

mean=student_data[student_data['Dalc']==5]['G3'].mean()
ax.axvline(mean, color='r', linestyle='--')



ax=f.add_subplot(122)
sns.distplot(student_data[(student_data.Dalc == 1)]['G3'],color='gray',ax=ax)
ax.set_title('Distribution of grades for people who consume little alcohol on weekdays')

mean=student_data[student_data['Dalc']==1]['G3'].mean()
ax.axvline(mean, color='r', linestyle='--')


# Drinking alcohol on weekdays is a bad idea! :D Of course, the number of those who love to drink on weekdays is much less than the number of those who prefer to spend weekdays sober. But we can see that the final grades of these students are significantly lower.

# In[37]:


f= plt.figure(figsize=(17,5))

ax=f.add_subplot(121)
sns.distplot(student_data[(student_data.Walc == 5)]["G3"],color='red',ax=ax)
ax.set_title('Distribution of grades for people who consume a lot of alcohol on weekends')

mean=student_data[student_data['Walc']==5]['G3'].mean()
ax.axvline(mean, color='r', linestyle='--')



ax=f.add_subplot(122)
sns.distplot(student_data[(student_data.Walc == 1)]['G3'],color='gray',ax=ax)
ax.set_title('Distribution of grades for people who consume little alcohol on weekends')

mean=student_data[student_data['Walc']==1]['G3'].mean()
ax.axvline(mean, color='r', linestyle='--')


# __How many students want to get higher education__

# In[38]:


sns.catplot(x="higher", kind="count",palette="rocket", data=student_data, height = 6)
plt.title("How many students want to get higher education?")


# almost all students want to get higher education

# __Distribution of grades for students who does not want to get higher education__

# In[39]:


plt.figure(figsize=(17,5))
plt.title("Box plot for final grades,depending on the desire to have higher education")
sns.boxplot(y="higher", x="G3", data = student_data , orient="h", palette = 'tab10',showmeans=True)

f= plt.figure(figsize=(17,5))
ax=f.add_subplot(121)
sns.distplot(student_data[(student_data.higher == 'yes')]["G3"],color='orange',ax=ax)
ax.set_title('Distribution of grades for students who wants to get higher education')

ax=f.add_subplot(122)
sns.distplot(student_data[(student_data.higher == 'no')]['G3'],color='red',ax=ax)
ax.set_title('Distribution of grades for students who does not want to get higher education')


# desire to get higher education stimulates students to get higher grades

# __How many students have not Internet__

# In[40]:


sns.catplot(x="internet", kind="count",palette="autumn", data=student_data, height = 6)
plt.title("How many students do not have Internet")


# __Let's see whether the availability of the Internet affects the number of hours students spend on their studies.__

# In[41]:


labels = ['<2 hours','2 - 5 hours','5 - 10 hours','> 10 hours']
values =student_data[(student_data.internet == 'no')].studytime.value_counts().tolist()

fig1, ax1 = plt.subplots()
ax1.pie(values,labels=labels, autopct='%1.1f%%',
        shadow=True)
ax1.axis('equal') 

plt.show()


# In[42]:


labels = ['<2 hours','2 - 5 hours','5 - 10 hours','> 10 hours']
values =student_data[(student_data.internet == 'yes')].studytime.value_counts().tolist()

fig1, ax1 = plt.subplots()
ax1.pie(values,labels=labels, autopct='%1.1f%%',
        shadow=True)
ax1.axis('equal') 

plt.show()


# In[43]:


plt.figure(figsize=(17,5))
plt.title("Box plot for final grades,depending on the access to the Internet")
sns.boxplot(y="internet", x="G3", data = student_data , orient="h", palette = 'pink',showmeans=True)


# students having internet having average grade is much more than students having no internet

# ## Final Conclusions -

# - On an average single people and commited people drink 3 times a week.
# - Count of single drinkers are more than commited
# - Most students spend 2 to 5 and 5 to 10 hours a week studying.
# - Avg score of grades of single students is more than students with relationship
# - It can be seen that around 11% students health conditions are extremely bad and 36% of students health comditions are very good
# - There is no tangible connection between the level of health of the student and the number of absences to classes.
# - Drinking alcohol on weekdays is a bad idea! :D Of course, the number of those who love to drink on weekdays is much less than the number of those who prefer to spend weekdays sober. But we can see that the final grades of these students are significantly lower.
# - Almost all students want to get higher education
# - Students having internet having average grade is much more than students having no internet
