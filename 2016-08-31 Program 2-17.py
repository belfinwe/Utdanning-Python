#2-17 etter programkart 31/08.

# Programstart /E

# Les inn antall sekunder /P

# Beregne antall hele timer /R
# Beregne antall gjenværende sekunder /R
# Beregne antall hele minutter /R
# Beregne antall gjenværende sekunder /R

#Skriv ut antal timer, minutter og sekunder /P

#Program-slutt /E



sek_fra_kunde = float(input('Skriv inn antall sekunder: '))

timer = int(sek_fra_kunde / 3600) # Gir timer i heltall.

sek_etter_timer = sek_fra_kunde - (3600 * timer) #Gir sekunder etter antall hele timer er funnet.
minutter = int(sek_etter_timer / 60) #Gir minutter i heltall.
sekunder = sek_etter_timer - (60 * minutter) #Sekunder etter at antall hele minutter er funnet.

print('Antall sekunder som skal konverteres:', sek_fra_kunde)
print('Timer:', timer)
print('Minutter:', minutter)
print('Sekunder:', sekunder)
