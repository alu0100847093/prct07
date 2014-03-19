#! encoding: UTF-8
#! /usr/bin/python
#def imprimir(l):
 #for i in range(1,l):
  #print"i\ t_upla1\ t_upla2\ t_upla3\ t_upla4\ t _upla5\ t_upla6"
import modulo07
t_upla=(10,100,1000,10000,100000,1000000)
l=[]
for i in range(len(t_upla)):
  s=modulo07.aproximacion_pi(t_upla[i])
  l=l+[s]
print l
# el numero maximos es 6
# para 8 elementos
# si se puede con notacion cientifica