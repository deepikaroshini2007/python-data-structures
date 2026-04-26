l=[]
n=int(input(&quot;enter no of elements:&quot;))
print(&quot;Enter the elements:&quot;)
for i in range(n):
element=int(input())
l.append(element)
while True:
print(&quot;1.Maximum value&quot;)
print(&quot;2.Minimum value&quot;)
print(&quot;3.Slice&quot;)
print(&quot;4.Count occurence&quot;)
print(&quot;5.first occurence&quot;)
print(&quot;6.Exit&quot;)
choice=int(input(&quot;enter choice:&quot;))
if choice==1:
print(&quot;Maximum value:&quot;,max(l))
elif choice==2:
print(&quot;Minimum value:&quot;,min(l))
elif choice==3:
s=int(input(&quot;Starting index:&quot;))
e=int(input(&quot;Ending index:&quot;))
print(&quot;Slice:&quot;,l[s:e])

elif choice==4:
x=int(input(&quot;Enter element to be count the occurence:&quot;))
print(&quot;count of the digit&quot;,x,&quot;:&quot;,l.count(x))
elif choice==5:
x=int(input(&quot;Enter element to find its first occurence:&quot;))
if x in l:
print(&quot;First occurence index:&quot;,l.index(x))
else:
print(&quot;element not found&quot;)
elif choice==6:
break
else:
print(&quot;Invalid choice&quot;)
