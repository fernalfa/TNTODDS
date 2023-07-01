import re
import time
import pyautogui

time.sleep(3)
surcharge_percentage = 10  # 10% surcharge

data = '''
Odds To Win - Tour De France 2023 - Jun 30
Odds To Win - Tour De France 2023
Odds To Win - Tour De France 2023
Odds To Win - Tour De France 2023
Jun 30 - 4:29 Pm

Rot

Description

Odds


478501

** All Action **
478502

Jonas Vingegaard
478503

Tadej Pogacar
478504

Remco Evenepoel
478505

Primoz Roglic
478506

Enric Mas Nicolau
478507

Juan Ayuso
478508

Carlos Rodriguez
478509

Richard Carapaz
478510

Geraint Thomas
478511

Egan Bernal
478512

Jai Hindley
478513

Wout Van Aert
478514

David Gaudu
478515

Alexander Vlasov
478516

Joao Almeida
478517

Thymen Arensman
478518

Daniel Martinez
478519

Romain Bardet
478520

Tom Pidcock
478521

Adam Yates
478522

Ben O'connor
478523

Jack Haig
478524

Miguel Angel Lopez
478525

Jay Vine
478526

Simon Yates
478527

Julian Alaphilippe
478528

Mikel Landa
478529

Nairo Quintana
478530

Pavel Sivakov
478531

Wilco Kelderman
478532

Chris Froome
478533

Tao Geoghegan Hart
478534

Sepp Kuss
478535

Tobias Halland Johannessen
478536

Rigoberto Uran
478537

Brandon Mcnulty
478538

Gino Mader
478539

Alexey Lutsenko
478540

Tobias Foss
478541

Mark Padun
478542

Thibaut Pinot
478543

Damiano Caruso
478544

Lennard Kamna
478545

Pello Bilbao
478546

Sergio Higuita
478547

Hugh Carthy
478548

Johan Esteban Chaves
478549

Emanuel Buchmann
478550

Louis Meintjes
478551

Guillaume Martin
478552

Steven Kruijswijk
478553

Jan Hirt
478554

Lucas Plapp
478555

Cian Uijtdebroeks
478556

Rohan Dennis
478557

Jakob Fuglsang
478558

Mathieu Van Der Poel
478559

Mattias Skjelmose
478560

Ivan Ramiro Sosa
478561

Lenny Martinez
478562

Fausto Masnada
478563

Ruben Guerreiro
478564

George Bennett
478565

Ilan Van Wilder
478566

Rafal Majka
478567

Marc Soler
478568

Ethan Hayter
478569

Ben Tulett
478570

Eddie Dunbar
478571

Clement Champoussin
478572

Mauri Vansevenant
478573

Michael Storer
478574

Giulio Ciccone
478575

Michael Woods
478576

Filippo Ganna
478577

Lucas Hamilton
478578

Max Schachmann
478579

Laurens De Plus
478580

Neilson Powless
478581

Mattia Cattaneo
478582

Bob Jungels
478583

Nick Schultz
478584

Domenico Pozzovivo
478585

Stephen Williams
478586

Andreas Leknessund
478587

Romain Gregoire
478588

Aurelien Paret-Peintre
478589

Wout Poels
478590

Juan Pedro Lopez
478591

Santiago Buitrago
478592

Valentin Madouas
478593

Marco Brenner
478594

Pierre Latour
478595

Warren Barguil
478596

Tiesj Benoot
478597

Davide Formolo
478598

Ion Izagirre
478599

Marc Hirschi
478600

Finn Fisher-Black
478601

Sam Oomen
478602

Biniam Girmay
478603

Franck Bonnamour
478604

Matteo Fabbro
478605

Harm Vanhoucke
478606

Quinn Simmons
478607

Ben Zwiehoff
478608

Patrick Konrad
478609

Carlos Verona
478610

Jesus Herrada
478611

Kasper Asgreen
478612

Reuben Thompson
478613

Joseph Lloyd Dombrowski
478614

Matej Mohoric
478615

Felix Grossschartner
478616

Mark Donovan
478617

Miguel Eduardo Florez
478618

Henri Vandenabeele
478619

James Knox
478620

Lennart Van Eetvelt
478621

Bauke Mollema
478622

Matteo Jorgenson
478623

Michal Kwiatkowski
478624

Alessandro Covi
478625

Giovanni Aleotti
478626

Koen Bouwman
478627

Vadim Pronskiy
478628

Asbjorn Hellemose
478629

Fred Wright
478630

Magnus Sheffield
478631

Felix Gall
'''


odds_data = '''
Jonas Vingegaard
+105
Tadej Pogacar
+115
Jai Hindley
+1400
Enric Mas Nicolau
+2200
Richard Carapaz
+2800
Mattias Skjelmose
+2800
Ben O'Connor
+3300
David Gaudu
+4000
Adam Yates
+4000
Simon Yates
+5000
Tom Pidcock
+5000
Mikel Landa
+6600
Felix Gall
+8000
Romain Bardet
+8000
Daniel Martinez
+8000
Carlos Rodriguez
+8000
Wout Van Aert
+10000
Egan Bernal
+10000
Wilco Kelderman
+10000
Julian Alaphilippe
+15000
Sepp Kuss
+15000
Pello Bilbao
+15000
Matteo Jorgenson
+15000
Marc Soler
+20000
Torstein Traeen
+30000
Thibaut Pinot
+30000
Rigoberto Uran
+30000
Guillaume Martin
+30000
Louis Meintjes
+30000
Michael Woods
+30000
Tobias Halland Johannessen
+40000
Alexey Lutsenko
+40000
Emanuel Buchmann
+40000
Giulio Ciccone
+40000
Mathieu van der Poel
+40000
Jack Haig
+50000
Johan Esteban Chaves
+50000
Ruben Guerreiro
+50000
Rafal Majka
+50000
Neilson Powless
+50000
Valentin Madouas
+50000
Ion Izagirre
+60000
Biniam Girmay
+60000
Clement Champoussin
+75000
Juan Pedro Lopez
+75000
Tiesj Benoot
+75000
Antonio Pedrero
+100000
Wout Poels
+100000
Pierre Latour
+100000
Warren Barguil
+100000
Matej Mohoric
+100000
Felix Grossschartner
+100000
Jonathan Castroviejo
+150000
Aurelien Paret-Peintre
+150000
Bob Jungels
+150000
Nick Schultz
+150000
Patrick Konrad
+150000
Michal Kwiatkowski
+150000
Quinn Simmons
+200000
Kasper Asgreen
+200000
Peter Sagan
+250000
Fred Wright
+250000
Nils Politt
+450000
Magnus Cort Nielsen
+450000
Mads Pedersen
+450000
Elmar Reinders
+450000
'''

def enterodd():
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(odd)))
    pyautogui.press('enter')
    pyautogui.press('down')
def deleteodd():
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('down')

names = re.findall(r'\n\d+\n\n(.+)', data)
odds = re.findall(r'(.+)\n([-+]?\d+)', odds_data)
odds_dict = {}

for name, odd in odds:
    if 100 <= int(odd) <= 110:
        surcharged_odd = min(int(odd) + int(odd) * (surcharge_percentage / 100), 10000) * -1
    else:
        if int(odd) > 100:
            surcharged_odd = min(int(odd) - int(odd) * (surcharge_percentage / 100), 10000)
        elif int(odd) < -100:
            surcharged_odd = min(int(odd) + int(odd) * (surcharge_percentage / 100), 10000)
        else:
            surcharged_odd = (int(odd) * -1) * (surcharge_percentage / 100)
    odds_dict[name] = surcharged_odd

# Print the first list of names
print("First List:")
for name in names:
    print(name)

# Print the second list of names and odds
print("\nSecond List:")
for name in names:
    odd = odds_dict.get(name.strip())
    if odd is not None:
        print(f"{name}: {odd}")
        enterodd()
    else:
        print(f"{name}: NONE")
        deleteodd()