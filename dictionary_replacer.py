d={&quot;store&quot;:&quot;shop&quot;,&quot;car&quot;:&quot;bike&quot;,&quot;present&quot;:&quot;gift&quot;}
s=input(&quot;Enter a string :&quot;)
words=s.split()
for i in words:
if i in d.keys():
print((d.get(i)),end=&quot; &quot;)
else:
print(i,end=&quot; &quot;)
