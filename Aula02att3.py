frase = str(input("Insira uma frase: "))
h = frase.split(" ")
count2 = len(h)
count1 = int(0)
while (count1 != count2): 
    print((count1 + 1)," - ", h[count1])
    count1 = count1 + 1