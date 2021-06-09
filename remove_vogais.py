def retira_vogais(cad):

    vogais = 'aeiouAEIOU'

    for ch in vogais:
        cad = cad.replace(ch,'')
    return cad

cad = 'vamos tEntar tirar As vOgaIs dessA frase'

print(retira_vogais(cad))