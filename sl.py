import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import math
st.write('# Trying streamlit for the first time with probability')
#streamlit run C:/Users/Daria/PycharmProjects/streamlit_histogram/sl.py
number = st.slider('Pick a number', 0, 10, 2)
a = random.randrange(1,10) *100
b = random.randrange(1,10) *10
#a = 500
#b = 100
st.write('Mean and standard deviation are being randomly generated each time')
st.write('Normal distribution with mean = ', a, 'and standard deviation = ', b)
x = np.random.normal(loc= a, scale=b, size=10000)

np.mean(x)
sample_mean = []

y = random.sample(x.tolist(), 200)
avg = np.mean(y)
st.write('min value:',np.min(y))
st.write('max value: ',np.max(y))

#st.write('y:', y, 'average:', avg)
#print(y[0])
#to display in python/pycharm
plt.plot(y)
plt.show()
#to plot in streamlit
st.line_chart(y)
st.write('mean over these drawn samples is ', avg)
#st.pyplot(y)

#bins = (np.max(y) - np.min(y))/100
#r_bins = math.ceil(bins)
st.write('we have numbers that span over ', math.floor(np.min(y)/100)*100, '-', math.ceil(np.max(y)/100)*100)
bins = math.ceil(np.max(y)/100) - math.floor(np.min(y)/100)
st.write('how many bins do we need? as many as hundreds, that is ', bins)
for i in range(math.floor(np.min(y)/100),math.ceil(np.max(y)/100)):
    st.write(i)
for i in range(math.floor(np.min(y)/100),math.ceil(np.max(y)/100)+1):
    if (i == math.floor(np.min(y)/100)):
        st.write('we have numbers that span over ', i*100, '-', (i+1)*100)
    if (i == math.ceil(np.max(y)/100)):
        st.write(', ', i * 100, '-', (i + 1) * 100, '.')
    if (i!=math.floor(np.min(y)/100) and i!=math.ceil(np.max(y)/100)):
        st.write(', ', i*100,'-',(i+1)*100)

line = ''
for i in range(math.floor(np.min(y)/100),math.ceil(np.max(y)/100)):
    if (i == math.floor(np.min(y)/100)):
        line = line+('We have numbers that span over '+str(i*100)+'-'+str((i+1)*100))
    if (i == math.ceil(np.max(y)/100)-1):
        line = line+(', '+str(i * 100)+ '-'+ str((i + 1) * 100)+ '.')
    if (i!=math.floor(np.min(y)/100) and i!=math.ceil(np.max(y)/100)-1):
        line = line+(', '+ str(i*100)+'-'+str((i+1)*100))

st.write(line)
#print('min', np.min(y), 'max', np.max(y),'bins',bins,'rounded up bins', r_bins)
#to find how many bins we need
# #find biggest number, find smallest number
#difference = biggest - smallest
#bins = round up(difference / 100)


fig = sns.displot(data=y, bins = bins)
st.pyplot(fig)

# Bootstrap Sampling
for i in range(40):
  y = random.sample(x.tolist(), 5)
  avg = np.mean(y)

  sample_mean.append(avg)

print(sample_mean)
print(np.mean(sample_mean))
st.line_chart(sample_mean)
print(np.mean(sample_mean))
st.write(np.mean(sample_mean))

#matplotlib is used here
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.write(arr)
st.write(fig,ax)
