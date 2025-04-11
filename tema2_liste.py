def citeste_int(mesaj):
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("Eroare: trebuie să introduci un număr valid.")
def numara_pare(lista):
    c=0
    for element in lista:
        if element%2==0:
            c+=1
    return c
def numara_impare(lista):
    c=0
    for element in lista:
        if element%2==1:
            c+=1
    return c
def cauta_valoare(lista,vl):
    indici=[]
    for i in range(len(lista)):
        if(lista[i])==vl:
            indici.append(i)
    if len(indici)==0:
        return f"Elementul {vl} nu se afla in lista"
    else:
        return f"Elementul {vl} se afla pe urmatoarele pozitii : ",indici
def sterge_elemt(x,lista):
    i = 0
    while i < len(lista):
        if lista[i] == x:
            lista.pop(i)
        else:
            i += 1
    return lista
def meniu():
    print("Meniu : ")
    print("1.Informatii despre lista")
    print("2.Sortare lista")
    print("3.Cauta valoare")
    print("4.Stergere element")
    print("5.Iesire")
if __name__ == '__main__':
    lista=[]
    x=citeste_int("Introduceti numarul de elemente din lista : ")
    print("Introduceti elementele listei : ")
    for i in range(x):
        element=int(input(f"Elementul {i+1} = "))
        lista.append(element)
    print("Lista = ",lista)
    meniu()
    while True:
        y=citeste_int("Introduceti o comanda : ")
        if y==1:
            print("Nr de elemete din lista este : ",len(lista))
            print("Media aritmetica a elementelor listei este : ",sum(lista)/len(lista))
            print("Elementul maxim al listei este : ",max(lista))
            print("Elementul minim al listei este : ",min(lista))
            print(f"In lista sunt {numara_pare(lista)} numere pare si {numara_impare(lista)} numere impare")
        elif y==2:
            lista.sort()
            print("Lista sortata : ",lista)
        elif y==3:
            valoare=int(input("Introduceti valoare ce o cautati : "))
            print(cauta_valoare(lista,valoare))
        elif y==4:
            el_de_sters=citeste_int("Introduceti elementul ce doriti sa-l eliminati din lista : ")
            print(sterge_elemt(el_de_sters,lista))
        else:
            exit("Bye bye")



