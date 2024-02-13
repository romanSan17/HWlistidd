nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ").capitalize()
    nimed.append(nimi)

  
print("loetelu oli: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)

for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
print("Vimasena oli lisatud: ",nimi)

uued_nimed=[]
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print(uued_nimed)

õpilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati', 'Mati']
unikaalsed_õpilased=list(set(õpilased))
print("unikaalne nimekiri:",unikaalsed_õpilased)

vanus=[1,13,18,33,55]
min_vanus = min(vanus)
max_vanus = max(vanus)
sum_vanus = sum(vanus)
keskmine_vanus = sum_vanus / len(vanus)
print("väikseim vanus:",min_vanus ,"suurim vanus:",max_vanus ,"vanus kokku:",sum_vanus ,"keskmine vanus:",keskmine_vanus )

        
