students=[]
n=int(input(&quot;Enter number of students&quot;))

for i in range(n):
id=int(input(&quot;Enter id&quot;))
name=input(&quot;Enter name&quot;)
marks=input(&quot;Enter marks&quot;)
students.append((id,name,marks))
print(&quot;All students details&quot;)
for s in students:
print(s)
id=int(input(&quot;Enter id to be search&quot;))
for s in students:
if s[0]==id:
print(&quot;STUDENT FOUND \n&quot;,s)
break
else:
print(&quot;STUDENT NOT FOUND \n&quot;)
high=students[0]
for s in students:
if s[2]&gt;high[2]:
high=s
print(&quot;Highest mark student :&quot;,high)
for s in students:
if int(s[2])&lt;40:
print(&quot;student less than 40 marks :\n&quot;,s)
tot=0
for s in students:
tot+=int(s[2])
avg=tot/n
print(&quot;Average marks compared to all students :&quot;,avg)
