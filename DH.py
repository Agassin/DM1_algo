def PE(t):
   return set(t) <= {0,1,2}

def inv(b,w,r,T,t):
   ok1= 0<=b<=w<=r+1<=len(T)
   ok2= b==0 or set(t[:b])=={0}  #zone bleue
   ok3= b==w or set(t[b:w])=={1} #zone blanche
   ok4= r+1==len(T) or set(t[r+1:])=={2} #zone rouge
   return ok1 and ok2 and ok3 and ok4 and sorted(t)==sorted(T)

def PS(b,w,r,T,t):
   ok1= 0<=b<=w and w==r+1<=len(T)
   ok2= b==0 or set(t[:b])=={0}  
   ok3= b==w or set(t[b:w])=={1}
   ok4= w==len(T) or set(t[w:])=={2} 
   return ok1 and ok2 and ok3 and ok4 and sorted(t)==sorted(T)


