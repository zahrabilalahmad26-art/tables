def table(n):
    tab=""
    for i in range(1,11):
        tab += f"{n}*{i}={n*i}\n" 
    with open(f"tables/table{n} ","w") as f:
         f.write(tab)
        
for i in range(2,22):
     table(i)  