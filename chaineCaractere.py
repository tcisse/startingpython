prenom = 'Tom'
nom = "Cruise"
age = 59
# print(type(prenom))
# print(type(nom))
# print(type(age))
nom_complet = prenom + " " + nom # concatenation

nom_complet_age = prenom + " " + nom + " " + str(age)

message = "Hello are you guys"
# print(len(message)) # compter le nombre de caractères
# print(nom_complet_age)

hello = "Bonjour je m'appelle"
have = "j'ai"
result = hello + " " + prenom + " " + have + " " + str(age) + " " + "ans"

# print(result)

# texte = "Hello my name is " + prenom + " I have " + str(age) + " years" # concatenation

texte = f"Hello my name is {prenom} I have {age} years" # formatage f-string
print(texte)

