# Forelesning #5, oppgave 9 side 135.
# Forfatter: Joakim Rønneberg Nilsen

tall = float(input('Skriv inn et tall fra 0 tilogmed 36: '))
if tall > 36:
    print('Tall utenfor gyldige tall!')
else:
    if tall < 0:
        print('Tall utenfor gyldige tall!')
    else:
        if tall == 0:
            print('Grønn.')
        else:
            if tall <= 10:
                tall_1 = tall / 2
                tall_10 = int(tall / 2)
                grp1 = tall_1 - tall_10
                if grp1 == 0:
                    print('Svart.')
                else:
                    print('Rød.')
            else:
                if tall <= 18:
                    tall_11 = tall / 2
                    tall_18 = int(tall / 2)
                    grp2 = tall_11 - tall_18
                    if grp2 == 0:
                        print('Rød.')
                    else:
                        print('Svart.')
                else:
                    if tall <= 28:
                        tall_19 = tall / 2
                        tall_28 = int(tall / 2)
                        grp3 = tall_19 - tall_28
                        if grp3 == 0:
                            print('Svart.')
                        else:
                            print('Rød.')
                    else:
                        if tall <= 36:
                            tall_29 = tall / 2
                            tall_36 = int(tall / 2)
                            grp4 = tall_29 - tall_36
                            if grp4 == 0:
                                print('Rød.')
                            else:
                                print('Svart.')

# Program slutt.
