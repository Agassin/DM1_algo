# Nom prenom

from DH import*



#PE: len(T)>=0 ET AI: 0<=I<len(T) -> (T[I]=0 OR T[I]=1 OR T[I=2]) 
#
#PS: AI: 0<=I<b -> t[I]=0  ET AI: b<=I<=r -> t[I]=1 ET AI: r<I<len(t) -> t[I]=2 ET t=permut(T) 
def drapeau_hollandais(t):
   assert PE(t) , "PE : t ne contient que des éléments de {0,1,2}"
   T=t[:]
   b=...
   w=...
   r=...
   #INV:: 0<=b<=w<=r+1<=len(T) ET Ai: 0<=i<b -> t[i]=0  ET Ai: b<=i<w -> t[i]=1 ET Ai: r<i<len(t) -> t[i]=2 ET t=permut(T)
   assert inv(b,w,r,T,t)  , "Etape 1: initialisations"
   while ...:
      #INV ET CC
      assert inv(b,w,r,T,t) and ... , "entree boucle"
      B=...   # on affecte la valeur de la variante a B
      assert B>0 ,"Etape 4: la variante est > 0 "
      
      # .
      # .   Completer  
      # .

      assert ...<B  ,"Etape 5 : la variante est strictement decroissante"   
      assert inv(b,w,r,T,t)  , "Etape 2: fin iteration"   

   assert inv(b,w,r,T,t) and ... , "Etape 3: sortie de boucle"   
   #INV ET not(CC)
   #PS
   assert PS(b,w,r,T,t) , "PS"
   return t




##################################################################################

if __name__ == "__main__":
  
  #placer ici vos tests de la fonction drapeau_hollandais
  t=[2,1,0,1,0,1,0,2,2,1]
  print(t)
  print(drapeau_hollandais(t))
  print(" ")    
        


