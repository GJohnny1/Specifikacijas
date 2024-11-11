# Ievadīt desmit skaitļus un izvadīt mazāko un lielāko skaitli

saraksts = []
reizes = 0

# uztaisa mainīgos saraksts, kurā tiks ievadītas vērtības, un reizes, kas kontrolēs while ciklu

print("Lai beigtu programmu, nospiediet nulli!")
while reizes < 10:
    reizes += 1
    ievade = float(input("Ievadiet skaitļus"))
    saraksts.append(ievade)
# while ciklā ievada ievadītos skaitļus sarakstā

mazakaisSkaitlis = saraksts[0]
for i in saraksts:
    if i < mazakaisSkaitlis:
        mazakaisSkaitlis = i
# no ievadītajiem skaitļiem mainīgajā patur vismazāko skaitli un izvada to

lielakaisSkaitlis = saraksts[0]
for i in saraksts:
    if i > lielakaisSkaitlis:
        lielakaisSkaitlis = i
# no ievadītajjiem skaitļiem mainīgajā patur vislielāko skaitli un izvada to

if ievade == 0:
    print("Mazākais skaitlis ir:", mazakaisSkaitlis)
    print("Lielākais skaitlis ir:", lielakaisSkaitlis)
    
