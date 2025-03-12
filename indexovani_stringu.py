# Pomocí indexů a operací slicing, striding zpracuj zadané hodnoty tak, ať dostaneš:
# Prvních 5 písmen slova 'indexování'
# posledních 5 písmen slova 'indexování'
# každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i")
# všechny výstupy zapiš přímo do funkce print
# výstup dále úprav podle ukázky níže.

slovo = "indexování"

print("Prvních 5 písmen: ", slovo[:5])
print("Posledních 5 písmen: ", slovo[-5:])
print("Každé 3. písmeno (počínaje prvním) od 'i': ",slovo[::3])
