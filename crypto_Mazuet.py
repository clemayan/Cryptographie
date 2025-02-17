##Q1)
# A|B|XOR(A,B)|XOR(XOR(A,B),B)
# 0|0|   0    |      0
# 1|0|   1    |      1
# 0|1|   1    |      0
# 1|1|   0    |      1

#convertit_binaire_en_texte(chaine_binaire)
# chiffre_xor(chaine_binaire,clef_binaire)
# convertit_binaire_vers_decimal(octet)
# genere_clefs_publique_et_privee(a1,b1,a2,b2)
# chiffre_message(m,clef)
# bruteForceKidRSA( e, n)
# egcd(a, b)
# modinv(e, n)


##Q2)
print("Q2")
#
# def convertit_texte_en_binaire(texte):
#     bin = ""
#     for i in texte:
#         lbin = ""
#         dec = ord(i) #transforme ascii en decimal
#         #print(i,":",dec)
#         while dec > 0:
#             val = dec%2
#             #print("bin", val)
#             lbin =  lbin + str(val)
#             #print("binaire :",lbin)
#             dec = dec//2
#         lbin = "0" + lbin #ajout d'un 0 pour faire un octet
#         #print("lettre binaire :",lbin)
#         bin = bin + lbin
#     return bin


def convertit_texte_en_binaire(texte):
    """
    :param texte : de type str
    :return : renvoie texte convertit en une chaine binaire

    >>> convertit_texte_en_binaire("NSI")
    '010011100101001101001001'
    >>> convertit_texte_en_binaire(" ")
    '00100000'
    >>> convertit_texte_en_binaire("N")
    '01001110'
    >>> convertit_texte_en_binaire("S")
    '01010011'
    >>> convertit_texte_en_binaire("I")
    '01001001'
    """
    binaire = "" #chaine de caractère qui contiendra la chaine binaire finale
    for i in texte:
        lbinaire = ""
        dec = ord(i) #transforme ascii en decimal
        #print("decimal de i :",dec)
        lbinaire = bin(dec) #transforme decimal en binaire
        if i == " ":
            #print("bin :",lbinaire)
            lbinaire = lbinaire.replace("0b","00") #rajoute un 0 pour faire un octet
            #print("00 :",lbinaire)
        #print("binaire de i :",lbinaire)
        binaire = binaire + lbinaire
    #print("0b :",binaire)
    binaire = binaire.replace("0b","0") #change la notation faite par défaut par la fonction bin()
    #print("0 :",binaire)
    return binaire


print("'NSI' en binaire :",convertit_texte_en_binaire("NSI"))
print("'N' en binaire :",convertit_texte_en_binaire("N"))
print("' ' en binaire :",convertit_texte_en_binaire(" "))

print()


##Q3)
print("Q3")
#def convertit_binaire_vers_entier_base_10(chaine_binaire):
#    dec = 0
#    for i in range(len(chaine_binaire)):
#        #print(chaine_binaire[i])
#        if chaine_binaire[i] == "1":
#            #print(2**(7-i))
#            dec = dec + 2**(7-i)
#            #print(dec)
#    return dec

def convertit_binaire_vers_entier_base_10(chaine_binaire):
    """
    :param chaine_binaire : type str
    :return : renvoie le nombre décimal correspondant à chaine_binaire (un octet)

    >>> convertit_binaire_vers_entier_base_10("01001110")
    78
    """
    dec = int(chaine_binaire,2) #transforme la chaine binaire en decimal
    #print(type(dec))
    return dec


print("'01001110' en decimal :",convertit_binaire_vers_entier_base_10("01001110"))
print()


# def convertit_binaire_en_texte(chaine_binaire):
#     txt = ""
#     dec = 0
#     for j in range(len(chaine_binaire)//8): #rpépété le nombre de fois qu'il y a de lettre
#         lettreb =""
#         print(chaine_binaire)
#         for i in range(8): #un octet
#             lettreb = lettreb + chaine_binaire[i]
#             #print(lettreb)
#         print(lettreb)
#         chaine_binaire = chaine_binaire[8:len(chaine_binaire)-1] #enleve l'octet transformé
#         #print("ch",chaine_binaire)
#         dec = convertit_binaire_vers_entier_base_10(lettreb)
#         print(dec)
#     txt = txt + chr(dec) #ajout de la lettre
#     #print(txt)
#     return txt
#
# print(convertit_binaire_en_texte("010011100101001101001001"))
# #'NSI'
# print()


##Q4)
print("Q4")

def convertit_binaire_en_texte(chaine_binaire):
    """
    :chaine_binaire : de type str
    :return : retourne chaine de caractère en ASCII correspondant à la chaine binaire

    >>> convertit_binaire_en_texte("01001110")
    'N'
    >>> convertit_binaire_en_texte("010011100101001101001001")
    'NSI'
    """
    txt = "" #chaine qui contiendra la chaine ascii finale
    for j in range(len(chaine_binaire)//8): #répépété le nombre de fois qu'il y a de lettre (d'octets)
        lettreb = chaine_binaire[:8] #le premier octets de la chaine binaire
        chaine_binaire = chaine_binaire[8:] #enleve l'octet transformé
        #print("ch",chaine_binaire)
        #print("lettre :",lettreb)
        dec = convertit_binaire_vers_entier_base_10(lettreb) #convertit la lettre considérée en décimal
        #print("ascii en dec :",dec)
        txt = txt + chr(dec) #ajout de la lettre à la chaine finale
    #print(txt)
    return txt

print("'010011100101001101001001' en texte ASCII :", convertit_binaire_en_texte("010011100101001101001001"))
#l = list(convertit_binaire_en_texte("01001110010100110100100100100000")) #test de l'espace
#print(l)
print()


##Q5)
print("Q5")

def chiffre_xor(chaine_binaire, clef_binaire):
    """
    :param chaine_binaire : de type str
    :param clef_binaire : de type str : clef
    :return : renvoie la chaine chiffré avec l'operation xor entre chaine_binaire et clef_binaire

    >>> chiffre_xor('0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001','01010100010001010101001001001101')
    '0000011100010101000101110000111000011101000001000001111000000100000000000000000001110010000000110000011100001100'
    """
    dif = len(chaine_binaire)-len(clef_binaire) #différence de taille entre la chaine à chiffré et la clef
    for i in range (dif):
      clef_binaire = clef_binaire + clef_binaire[i] #répétition des valeurs de la clef pour transformer sa taille
    #print("taille chaine :",len(chaine_binaire))
    #print("taille clef :",len(clef_binaire))
    #print("nouv clef :",clef_binaire)

    message_code = "" #chaine str qui contiendra le message codé final
    for i in range(len(chaine_binaire)):
        #print("compa",chaine_binaire[i],clef_binaire[i])
        if (chaine_binaire[i] == "1" and clef_binaire[i] == "0") or (chaine_binaire[i] == "0" and clef_binaire[i] == "1") : #une valeur est '1', l'autre est '0'
            message_code = message_code + "1"
        else : #il y a 2 valeurs identiques
            message_code = message_code + "0"
        #print("message_code :",message_code)
    return message_code

print("xor binaire :", chiffre_xor('0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001','01010100010001010101001001001101'))
print()


##Q6)
print("Q6")

message = "SPECIALITE NSI"
clef_message = "TERM"
message_binaire = convertit_texte_en_binaire(message)
print(message,"en binaire :",message_binaire)
#0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001

clef_binaire = convertit_texte_en_binaire(clef_message)
print(clef_message, "en binaire :", clef_binaire)
#01010100010001010101001001001101

message_binaire_chiffre = chiffre_xor(message_binaire,clef_binaire)
print("message chiffré :",message_binaire_chiffre)
#0000011100010101000101110000111000011101000001000001111000000100000000000000000001110010000000110000011100001100

message_binaire_dechiffre = chiffre_xor(message_binaire_chiffre,clef_binaire)
print("message_binaire_dechiffre :",message_binaire_dechiffre)
#0101001101010000010001010100001101001001010000010100110001001001010101000100010100100000010011100101001101001001

print("message dechiffré en ASCII :",convertit_binaire_en_texte(message_binaire_dechiffre))
#SPECIALITE NSI
print()

message = "HELLO WORLD"
clef_message = "COUCOU"
message_binaire = convertit_texte_en_binaire(message)
print(message,"en binaire :",message_binaire)
#0100100001000101010011000100110001001111001000000101011101001111010100100100110001000100

clef_binaire = convertit_texte_en_binaire(clef_message)
print(clef_message, "en binaire :", clef_binaire)
#010000110100111101010101010000110100111101010101

message_binaire_chiffre = chiffre_xor(message_binaire,clef_binaire)
print("message chiffré :",message_binaire_chiffre)
#0000101100001010000110010000111100000000011101010001010000000000000001110000111100001011

message_binaire_dechiffre = chiffre_xor(message_binaire_chiffre,clef_binaire)
print("message_binaire_dechiffre :",message_binaire_dechiffre)
#0100100001000101010011000100110001001111001000000101011101001111010100100100110001000100

print("message dechiffré en ASCII :",convertit_binaire_en_texte(message_binaire_dechiffre))
#HELLO WORLD

print()

print("#######################################")

print()

##Q7)
print("Q7")
a1=5
b1=3
a2=7
b2=5

M = a1 * b1 - 1
print("M :", M)
#14
e = a2 * M + a1
print("e :", e)
#103
d = b2 * M + b1
print("d :", d)
#73
n = (e * d - 1) // M
print("n :", n)
#537
print("clef publique :",(e,n))
print("clef secrète :",(d,n))

#Donner le message chiffré par la clef publique représenté par le code ASCII de la lettre 'a' (en minuscule).
a = ord("a")
print("a :", a)
a_chiffre = (e * a) % n
print("a chiffré :",a_chiffre)
a_dechiffre = (d * a_chiffre) % n
print("a déchiffré :", a_dechiffre)

print()

##Q8)
print("Q8")

def genere_clefs_publique_et_privee(a1,b1,a2,b2):
    """
    :param a1,b1,a2,b2 : valeurs de type int
    :return : renvoie les clef publique et privée générées

    >>> genere_clefs_publique_et_privee(13,32,69,35)
    ((28648, 1004889), (14557, 1004889))
    """
    M = a1 * b1 - 1
    e = a2 * M + a1
    d = b2 * M + b1
    n = (e * d - 1) // M
    clef_pub = (e,n)
    clef_priv = (d,n)
    return clef_pub, clef_priv

(clef1,clef2)=genere_clefs_publique_et_privee(13,32,69,35)
#print((clef1,clef2))
#(clef1,clef2) = genere_clefs_publique_et_privee(9,11,5,8)
print("clef publique :", clef1)
print("clef privée :", clef2)
print()


def chiffre_message(m,clef):
    """
    :param m : de type str
    :param clef : de type tuple
    :return : renvoie le message chiffré de m sous forme de liste, en remplaçant chaque caractère par son code ASCII en décimal

    >>> chiffre_message("maya",clef1)
    [107965, 769078, 451741, 769078]

    """
    chiffre = [] #liste qui contiendra le resultat du message chiffré
    for i in m: #parcours chaque lettre du message
        #print(i)
        binm = convertit_texte_en_binaire(i)
        #print("binm :",binm)

        decm = convertit_binaire_vers_entier_base_10(binm)
        #print("n :",clef[0])
        #print("e :",clef[1])
        valeur = (clef[0] * decm)%clef[1] #valeur de la lettre i chiffrée
        chiffre.append(valeur)
    return chiffre


#print(clef1)
mchiffre = chiffre_message("maya",clef1)
print("'maya' chiffré :",mchiffre)
print()

def dechiffre_message(m,clef):
    """
    :param m : de type lst
    :param clef : de type tuple
    :return : renvoie le message déchiffré sous la forme d'une chaîne de caractères

    >>> dechiffre_message([107965, 769078, 451741, 769078],clef2))
    'maya'
    """
    dechiffre = "" #chaine de caractère qui contiendra le resultat du message dechiffré
    #print(clef)
    for i in m: #parcours chaque valeur du tableau chiffré
        #print("d :",clef[0])
        #print("n :",clef[1])
        #print(i)
        #print((clef[1] * i)%clef[0])
        valeur = chr((clef[0] * i)%clef[1]) #message déchiffré en ascii
        #print(valeur)
        #print(type(valeur))
        #print(type(dechiffre))
        dechiffre = dechiffre + valeur #message déchiffré en str
    return dechiffre

print(mchiffre, "déchifré :", dechiffre_message(mchiffre,clef2))

#
# def dechiffre_message(m,clef):
#     """
#     m : de type lst
#     renvoie le message déchiffré sous la forme d'une chaîne de caractères
#     """
#     binm = convertit_texte_en_binaire(m)
#     decm = convertit_binaire_vers_entier_base_10(binm)
#     print("bin message",binm)
#     print("dec message",decm)
#     return (d * decm)%n

# print()
# def dechiffre_message(m,clef):
#     """
#     m : de type lst
#     renvoie le message déchiffré sous la forme d'une chaîne de caractères
#     """
#     print("n :",clef1[1])
#     print("d :",clef2[0])
#     dechiffre = (clef2[0] * m)%clef1[1] #message déchiffré en ascii
#     return chr(dechiffre) #message déchiffré en str
#     #return (clef2[0] * m)%clef1[1]
#     #return (d * m)%n
#
#
# print(dechiffre_message(mchiffre,clef))
print()


##Q9)
print("Q9")
#(clef1,clef2)=genere_clefs_publique_et_privee(13,32,69,35)
print("clefs :", (clef1, clef2))
nsi_c = chiffre_message("NSI",clef1)
print("NSI chiffré :", nsi_c)
print("NSI déchiffré :", dechiffre_message(nsi_c,clef2))
print()


##Q10)
def bruteForceKidRSA(e,n):
    """
    : param e et n : de type int : valeurs de la clef publique
    :return : renvoie le premier entier d inférieur à n qui vérifie la relation 'e×d−1 est divisible par n'

    >>> bruteForceKidRSA(53447,5185112)
    323639
    """
    for i in range(n): #test toutes les valeurs
        if ( e * i - 1 )%n == 0: #e×i−1 est divisible par n
            #print(e,i,n)
            return i

##Q11)
print("Q11")
message_chiffre = [3580949, 2084433, 3687843, 4436101, 4489548, 1710304, 4329207, 4542995, 3901631, 1710304, 4061972, 3687843, 1710304, 3527502, 4222313, 4436101, 4436101, 1710304, 3687843, 4168866, 1710304, 4168866, 4436101, 3901631, 1710304, 3367161]
d = bruteForceKidRSA(53447,5185112)
print("d :", d)
(clef3,clef4) = ((53447,5185112),(d,5185112))
print("clef publique :", clef3)
print("clef privée :", clef4)
print("message déchiffré :", dechiffre_message(message_chiffre,clef4))
#print(dechiffre_message([3580949],clef4))
print()

##Q12)
# print("Q12")
# d4 = bruteForceKidRSA(230884490440319,194326240259798261076)
# message_chiffre4 = [16623683311702968, 19625181687427115, 16392798821262649, 16392798821262649, 20548719649188391, 7388303694090208, 17547221273464244, 15931029840382011, 19163412706546477, 7388303694090208, 15238376369061054, 18239874744785201, 18008990254344882, 19163412706546477, 7388303694090208, 19394297196986796, 19625181687427115, 20548719649188391, 15007491878620735, 19625181687427115, 20317835158748072, 7388303694090208, 7619188184530527]
# print("d :", d4)
# (clef5,clef6) = (194326240259798261076,230884490440319),(194326240259798261076,d4)
# print("clef publique :", clef5)
# print("clef privée :", clef6)
# print("message déchiffré :", dechiffre_message(message_chiffre4,clefs6))

#cela ne fonctionne pas car d est trop long à trouver car n est trop grand
# print()


##Q13)
print("Q13")

def modinv(e,n):
    """"
    : param e et n : de type int : valeurs de la clef publique
    :return : renvoie le premier entier d inférieur à n qui vérifie la relation 'e×d−1 est divisible par n'
    """
    g,x,y = egcd(e,n)
    if g != 1:
        return False
    else:
        return x % n

def egcd(a,b):
	if a == 0:
		return(b,0,1)
	else:
		g,y,x = egcd(b % a,a)
		return (g, x - (b//a)*y,y)

print("tests :")
message_chiffre6 = [224766, 368006, 81526]
d6 = bruteForceKidRSA(28648, 1004889)
d62 = modinv(28648, 1004889)
#(1004889, 28648) (1004889, 14557)
#d : 14557
print("d :", d6)
print("d :", d62)
(clef9,clef10) = ((28648, 1004889),(d6,1004889))
print("clef publique :", clef9)
print("clef privée :", clef10)
print("message déchiffré :", dechiffre_message(message_chiffre6,clef10))#Python int too large to convert to C int
print()

message_chiffre5 = [16623683311702968, 19625181687427115, 16392798821262649, 16392798821262649, 20548719649188391, 7388303694090208, 17547221273464244, 15931029840382011, 19163412706546477, 7388303694090208, 15238376369061054, 18239874744785201, 18008990254344882, 19163412706546477, 7388303694090208, 19394297196986796, 19625181687427115, 20548719649188391, 15007491878620735, 19625181687427115, 20317835158748072, 7388303694090208, 7619188184530527]
d5 = modinv(230884490440319,19432624025979826176)
print("d :", d5)
(clef7,clef8) = ((230884490440319,19432624025979826176),(d5,19432624025979826176))
print("clef publique :", clef7)
print("clef privée :", clef8)
print("message déchiffré :", dechiffre_message(message_chiffre5,clef8))
print()


##Q14)
#les clés sont habituellement de longueur comprise entre 1 024 et 2 048 bits
#En se servant simplement d'un microphone pour écouter les bruits émis par un ordinateur lorsqu'il décrypte un message chiffré
