# 1. Piešķirt vismaz 2 pamata tipu vērtības mainīgajiem

speles_nosaukums = "Minecraft"      #str
izlaisanas_gads = 2009      #int          
vai_vel_pastav = True     #bool

# 2. Konsoles izvade ar katras vērtības tipu, izmantojot type()

print("Spēles nosaukums:", (speles_nosaukums), type(speles_nosaukums))       #<class 'str'>
print("Spēles izlaišanas gads:", (izlaisanas_gads) , type(izlaisanas_gads))      #<class 'int'>
print("Vai spēle vēl pastāv:", (vai_vel_pastav), type(vai_vel_pastav))     #<class 'bool'>

# 3. Vismaz 3 Python truthy/falsy uzvedības piemērus ar komentāriem

print (bool("Nice!"))       #True, jo ir komentārs
print (bool(0.67))      #True, jo jebkuram skaitlim (izņemot 0) ir vērtība
print (bool([]))        #False, jo tukšs saraksts
print (bool(0))     #False, jo nulle (nav vērtības)

# 4. Vismaz 3 tiešās datu tipu pārveides un robežgadījumiem

print(str(0.67))    #float tiek pārveidots par string
print(int(True))     #bool tiek pārveidots par int, attēlojot True kā 1 un False kā 0
print(float("Hello!"))      #string tekstu nevar pārveidot par float, jo nav skaitlis
print(int("0.67"))      #float nevar pārveidot par integer, jo nav vesels skaitlis