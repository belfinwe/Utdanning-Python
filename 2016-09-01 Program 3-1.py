# Program for Kathryn:

# Les inn tre testresultater
# Regn ut gjennomsnittet

# Dersom gjennonsnittet er over 95, gratuler brukeren!

# Skriv ut gratulasjonsmelding dersom gjennomsnittet er over 95%.

############################################################

test1 = float(input('Testresultat #1: '))
test2 = float(input('Testresultat #2: '))
test3 = float(input('Testresultat #3: '))

gjennomsnitt = (test1 + test2 + test3) / 3
print('Gjennomsnittet er:', gjennomsnitt)

if gjennomsnitt > 95:
    print('Gratulerer med en testscore høgare enn 95%. Ikkje verst! :D')
