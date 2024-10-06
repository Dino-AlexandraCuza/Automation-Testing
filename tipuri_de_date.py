
"Ex_1 - Definiți o adresă de memorie care să salveze data curentă. Va fi o variabilă sau o constantă?"

data_curenta=26
"constanta"

"Ex_2 - Identificați tipul de dată pe care îl are variabila pe care ați definit-o folosind una din funcțiile învățate la curs"

int

"Ex_3 - Definiți alte câteva variabile care să stocheze cursul la care sunteți, ce zi este și la ce sesiune de curs sunteți"

curs_nume="TMTA"
ziua=26
sesiune_curs=1.3

"Ex_4 - Salvați fiecare cuvânt din propoziția: “Ana s-a nascut in anul 1990” în câte o adresă de memorie"

nume="ana"
actiune="s-a nascut"
timp="anul"
prepozitie="in"
anul=1990

"Ex_5 - Printați propoziția de mai sus folosind trei tipuri diferite de printuri"

print(f"{nume} {actiune} {timp} {prepozitie} {anul}")
print(str(nume) + str(actiune) + str(timp) + str(prepozitie) + str(anul))
print("Ana s-a nascut in anul 1990")
print()


"Ex_6 - Declarați câteva alte adrese de memorie la alegere și inițializați-le folosind funcția input."
nume="axi"
obiect="jucarie"
numar=3
actiune="joaca"
musca=True

actiune_axi=input("Cu ce se joaca cainele ?")

"Ex_7"
#Definiti o noua constanta care sa reprezinte valoarea
# unei excursii pe care ati achizitionat-o recent si respectiv una care sa stocheze
#un eventual discount pe care l-ati avut.
#Valorile se vor da de la tastaura.
# In final veti calcula valoarea finala a calatoriei
# folosind pretul de baza al biletului si valoarea
#discountului.
#Ce trebuie sa ii faceti functiei input pt ca acest exercitiu sa functioneze?

VALOARE_EXCURSIE=float(input("Va rugam sa introduceti valoarea excursiei"))
PROCENT_DISCOUNT=float(input("Va rugam sa introduceti procentul de discount aplicat"))
VALOARE_DISCOUNT= VALOARE_EXCURSIE * PROCENT_DISCOUNT
VALOARE_EXCURSIE_CU_DISCOUNT= VALOARE_EXCURSIE - VALOARE_DISCOUNT

print(f"valoarea excursiei cu discount este{VALOARE_EXCURSIE_CU_DISCOUNT}")
