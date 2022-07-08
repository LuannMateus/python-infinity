paisA = 80000
paisB = 200000
anos = 0

while True:
    paisA = (paisA * 0.03) + paisA
    paisB = (paisB * 0.015) + paisB
        
    anos += 1

    if paisA >= paisB:
        break

print(f"""A quantidade de anos 
necessária para que o 
país A ultrapasse país B é de {anos} anos""")
