# Segré Alexis

from DH import*



#PE: len(T)>=0 ET AI: 0<=I<len(T) -> (T[I]=0 OR T[I]=1 OR T[I=2]) 
#
#PS: AI: 0<=I<b -> t[I]=0  ET AI: b<=I<=r -> t[I]=1 ET AI: r<I<len(t) -> t[I]=2 ET t=permut(T) 
def drapeau_hollandais(t):
   assert PE(t) , "PE : t ne contient que des éléments de {0,1,2}"
   T=t[:]
   b=0
   w=0
   r=len(T)-1
   assert inv(b,w,r,T,t)  , "Etape 1: initialisations"
   while w <= r:
      assert inv(b,w,r,T,t) and w <= r , "entree boucle"
      B=r-w+1  
      assert B>0 ,"Etape 4: la variante est > 0 "
      
      if t[w] == 0:
         t[b], t[w] = t[w], t[b]
         b += 1
         w += 1
      elif t[w] == 1:
         w += 1
      else: 
         t[w], t[r] = t[r], t[w]
         r -= 1

      assert r-w+1 < B ,"Etape 5 : la variante est strictement decroissante"   
      assert inv(b,w,r,T,t)  , "Etape 2: fin iteration"   

   assert inv(b,w,r,T,t) and w > r , "Etape 3: sortie de boucle"   
   #INV ET not(CC)
   #PS
   assert PS(b,w,r,T,t) , "PS"
   return t




##################################################################################

if __name__ == "__main__":
  # Tests de la fonction drapeau_hollandais
  def test_drapeau_hollandais():
      tests = [
          ([2, 1, 0, 1, 0, 1, 0, 2, 2, 1], [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]),
          ([0, 1, 2, 0, 2, 1, 1, 0], [0, 0, 0, 1, 1, 1, 2, 2]),
          ([2, 2, 2, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
          ([1, 0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 1, 2, 2]),
          ([0, 0, 0], [0, 0, 0]),
          ([1, 1, 1], [1, 1, 1]),
          ([2, 2, 2], [2, 2, 2]),
          ([0, 1, 2], [0, 1, 2]),
      ]
      for i, (input_list, expected) in enumerate(tests):
          assert drapeau_hollandais(input_list[:]) == expected, f"Test {i+1} échoué: {input_list} -> {drapeau_hollandais(input_list[:])}, attendu {expected}"
      print(f"Tests drapeau hollandais: ok ({len(tests)} tests passés)")
  
  test_drapeau_hollandais()


