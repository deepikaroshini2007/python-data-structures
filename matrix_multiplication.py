r1=int(input(&quot;enter the row for Matrix1 :&quot;))
c1=int(input(&quot;enter the column for Matrix1 :&quot;))
r2=int(input(&quot;enter the row for Matrix2 :&quot;))
c2=int(input(&quot;enter the column for Matrix2 :&quot;))
if c1!=r2:
print(&quot;Matrix mutiplication not possible&quot;)
else:
A=[]

B=[]
print(&quot;Enter the Matrix A&quot;)
for i in range(r1):
row=[]
for j in range(c1):
num=int(input())
row.append(num)
A.append(row)
print(&quot;Enter the Matrix B&quot;)
for i in range(r2):
row=[]
for j in range(c2):
num=int(input())
row.append(num)
B.append(row)
c=[]
for i in range(r1):
row=[]
for j in range(c2):
row.append(0)
c.append(row)
for i in range(r1):
for j in range(c2):
for k in range(c1):
c[i][j]=c[i][j]+A[i][k]*B[k][j]
print(&quot;Resultant Matrix&quot;)
for i in range(r1):
for j in range(c2):
print(c[i][j],end=&quot; &quot;)
print()
