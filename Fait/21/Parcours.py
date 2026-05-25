from ListNode import ListNode
from typing import Optional

def parcours(liste : Optional[ListNode]) :
    pListe = liste
    while pListe != None :
        print(pListe.val)
        pListe = pListe.next

#print(parcours(ListNode(1, ListNode(2, ListNode(4)))))

def ajout(liste : Optional[ListNode]) :
    if liste == None :
        liste = ListNode(1)
        pListe = liste
        pListe.next = ListNode(2)
        pListe = pListe.next
        pListe.next = ListNode(4)
        pListe = pListe.next
    return liste

print(parcours(ajout(None)))

