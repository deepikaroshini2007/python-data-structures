d={}
x=int(input(&quot;Enter no. of students:&quot;))
for i in range(x):
n=input(&quot;Enter name :&quot;)
m=int(input(&quot;Enter marks:&quot;))
d[n]=m
print(d)
name=(input(&quot;Enter the searching student name:&quot;))
if name in d:
print(name,&quot;=&quot;,d[name])
else:
print(&quot;Student not found&quot;)
