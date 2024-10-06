# EX_1 - Calculare preț discount

# Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.

# În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil, va avea o reducere de 10%.

# Atât pentru seniori cât și pentru non-seniori se va aplica o reducere suplimentară de 10% dacă vor călători în timpul iernii.

# De asemenea, atât pentru seniori, cât și pentru non-seniori se va aplica o taxă de lux de 3% dacă vor călători la clasa I
# (în orice sezon) sau 1% taxă de gestiune în caz contrar.

 #pret_bilet = pret_bilet - pret_bilet*discount + pret_bilet*tax

pret_bilet=int(input("Introduceti valoarea biletului"))
varsta_client=int(input("Introduceti varsta clientului"))
reducere_procent=0.1
sezon="iarna"
taxa=float(input("introduceti valoarea taxei"))
reducere_finala=pret_bilet - reducere_procent
pret_bilet = pret_bilet - pret_bilet*reducere_finala + pret_bilet*taxa

#if: varsta_client>=65
#    reducere=1.5%
#else:varsta_client<=65
#    copil>1
#   reducere=0.1%
#if:varsta_client>=65
#    varsta_client<=65
#   reducere=0.1%
#    sezon="iarna"
#if:varsta_client>=65
#   varsta_client<=65
#   taxa_lux=0.3
#else:taxa_gestiune=0.1
# —-----

# Pentru exercițiul de mai sus trebuie să scrieți structura alternativă if-elif-else astfel încât să implementați scenariul aferent.
# Prețul biletului se va citi de la tastatura si se va actualiza conform discountului și taxelor aferent

#Ex_2 - Calculare discount seller

# Compania X vinde mărfuri la punctele de vânzare pentru cumpărători wholesale și retail. Clienții wholesale primesc
# o reducere de două procente la toate comenzile. De asemenea, compania încurajează atât clienții wholesale
# cât și clienții cu amănuntul să plătească ramburs la livrare, oferind o reducere de două procente pentru această
# metodă de plată. Încă o reducere de două procente este acordată pentru comenzile de 50 sau mai multe unități.


# Ex_3 - Introduceți un nume de film de la tastatură și evaluați dacă numele acelui film este numele filmului vostru preferat.
# Dacă da, atunci printați pe ecran: “Acesta este filmul meu preferat”. În caz contrar printați pe ecran: “Din pacate nu este filmul meu preferat

#nume_film=input("Introduceti numele filmului preferat")
#film="coco"

#if:nume_film==("coco")
 #   print(f"Acesta este filmul meu preferat")
#else:print(f" Din pacate nu este filmul meu preferat")

# Ex_4 - Aveți la dispoziție următorul database url: jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
# Extrageți din acest text numele bazei de date: mysql.db.server
# Folosiți un if statement pentru a evalua dacă numele bazei de date este cel corect (presupunând că extrageți url-ul dintr-un sistem extern și nu știți care este acesta)

#nume_baza="mysql.db.server"
#if:
#    nume_baza= "mysql.db.server"
#    print(f"{nume_baza}")
