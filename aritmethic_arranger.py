def arranjo(problems,aws = False):
  display = ""
  d = list()
  arranjed = {}
  if len(problems) > 4:
    display = "Error: Problemas demais (limite = 4)"
  l = 0
  v = 0
  for k in problems:
    l += 1
    d = k.split()
    #validador dos operadores:
    if len(d) < 3 or len(d) > 3:
      if d[0] or d[1] in '-+':
        display = "Parece que voce digitou apenas um dos operadores."
      else: 
        display = "Erro"
    #validador de sinal:
    if d[1] not in "+-":
      display = f"Ops, erro no {l}º problema: Dê espaço entre os algarismos e o sinal ou insira um sinal válido."
    try:
      a1 = int(d[0])
      a2 = int(d[2])
      l1 = len(d[0])
      l2 = len(d[2])
      r = eval(k)
      m = max(l1,l2) + 2
      
      i = [a1,a2,l1,l2,r,m,d[1]]
      arranjed[v] = i
      v += 1
    except:
      print("ouve um erro")
  #[✅]
  p = 0
  for k,v in arranjed.items():
    space = v[5] - v[2]
    while(space):
      display += " "
      space -= 1
    display += str(v[0])
    if p < len(problems)-1:
      for t in range(4):
        display += ' ' 
    p += 1 
  display += "\n"
  #[✅]
  e = 0
  for k,v in arranjed.items():
    display += str(v[6])+ " "
    if v[3] < v[2]:
      space = v[2] - v[3]
      while space:
        display += " "
        space -= 1
    display += str(v[1])
    if e < len(problems)-1:
      for t in range(4):
        display += ' ' 
    e += 1
  display += "\n" 
  #[✅]
  #linha
  u = 0
  for k,v in arranjed.items():
    line = int(v[5])
    while line:
      display += "-"
      line -= 1
    if u < len(problems)-1:
      for t in range(4):
        display += ' ' 
    u += 1    
  #return display
  print(display)
arranjo(["200 + 28","1000 - 12","1388 + 100","1277 + 142"])