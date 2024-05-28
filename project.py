
def computeFirst(G):

  F = {}

  for key in G.keys():
    F[key] = []

  change = True

  while change:
    change = False

    for key, value in G.items():
      for item in value:
        if item == "e" and "e" not in F[key]:
          F[key].append("e")
          change = True
          continue

        for i in range(len(item)):
          
          if item[i].islower():
            if item[i] not in F[key]:
              F[key].append(item[i])
              change = True
            break

          elif item[i].isupper():

            for item2 in F[item[i]]:
              if item2 != "e" and item2 not in F[key]:
                F[key].append(item2)
                change = True
            
            if "e" not in F[item[i]]:
              break
            if i == len(item) - 1 and "e" not in F[key]:
              F[key].append("e")

  for key, value in F.items():
    print('First('+key+') = {', end="")
    for i in range(len(value)):
      if i == len(value) - 1:
        print(value[i], end="")
      else:
        print(value[i] + ", ", end="")
    print("}")

  computeFollow(G, F)

def computeFollow(G, F):
  FW = {}

  for key in G.keys():
    FW[key] = []

  FW["S"].append("$")

  for key, value in G.items():
    for item in value:
      for i in range(len(item)):
        if item[i].isupper():

          beta = item[i+1:len(item)]
          frstB = []

          for j in range(len(beta)):
            if beta[j].islower() and beta[j] not in frstB:
              frstB.append(beta[j])
              break
            elif beta[j].isupper():
              frstB.extend([item for item in F[beta[j]] if item not in frstB and item != "e"])
              if "e" not in F[beta[j]]:
                break
            
          FW[item[i]].extend(frstB)

  for key, value in G.items():
    for item in value:
      for i in range(len(item)):
        if item[i].isupper():

          if i == len(item) - 1:
            FW[item[i]].extend([itemFW for itemFW in FW[key] if itemFW not in FW[item[i]]])
            break

          beta = item[i+1:len(item)]
          frstB = []

          for j in range(len(beta)):
            if beta[j].islower() and beta[j] not in frstB:
              frstB.append(beta[j])
              break
            elif beta[j].isupper():
              frstB.extend([item for item in F[beta[j]] if item not in frstB and item != "e"])
              if "e" not in F[beta[j]]:
                break
            
          if "e" in frstB:
            FW[item[i]].extend([itemFW for itemFW in FW[key] if itemFW not in FW[item[i]]])

  for key, value in FW.items():
    print('Follow('+key+') = {', end="")
    for i in range(len(value)):
      if i == len(value) - 1:
        print(value[i], end="")
      else:
        print(value[i] + ", ", end="")
    print("}")



def main():
  c = int(input())
  for _ in range(c):
    l = int(input())
    G = {}
    j = 0
    while j < l:
      w = input()
      w = w.split()
      G[w[0]] = []
      for i in range(1,len(w)):
        G[w[0]].append(w[i])
      j+=1
    computeFirst(G)
main()