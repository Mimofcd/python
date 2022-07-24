def format_number(x):
   x=str(x)
   ytre=""
   i=len(x)
   for i in range (len(x),0,i-3):
       ytre=","+slice(x[i],x[i-3])
   return(ytre)