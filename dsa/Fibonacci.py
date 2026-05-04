# -------------- Fibonaacci Numbers ---------------------f(n)=f(n-1)+f(n-2)

#------- with FOR LOOP

num_1=0
num_2=1
for value in range(5):
  res=num_1+num_2
  print(res)
  num_1=num_2
  num_2=res

#------- with Recursion

count=2
def Fibo(prev_1,prev_2):
    global count
    if count <=10:
        result=prev_1+prev_2
        print(result)
        prev_2=prev_1
        prev_1=result
        count+=1
        Fibo(prev_1,prev_2)

Fibo(0,1)

















