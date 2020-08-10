# aris-recovery-prediction
Maturaarbeit Alexander Doongaji EMS Schiers 2020

Der Code wurde mit Hilfe der Spyder IDE geschrieben. Ein Python interpreter wird benoetigt um den Code laufen zu lassen. 

Die Haupt�nderung des Modells ligt dadirn, dass das Modell jetzt der Start auch im Modell enthalten ist. Somit ist das Modell in zwei Teile eingeteilt. Hierbei wird auch von einer Instantanous Geschwindigkeit augegangen, sprich einer v0 und nicht einer Beschleunigung, wie es eigentlich sein sollte. 

Das Wetter kommt von der OpenWeatherMap API. 

N�tige Variablen: 
roh = Dichte der Luft
c_d = Dragcoefficient -> zusammenfassung meherer komplexen Werte. N�tig f�r die berechnung des Luftwiederstands 
t_b = burn time 
F = Kraft des Triebwerkes 
m = Masse mit Triebsatz
a_burn = Beschleunigung 
A = Oberfl�che der Rakete
A_Para = Fl�che des Fallschirms 
dt = timestep
D = zusammenfassung der Konstanten Werter der Wiederstandsgleichung 
N�tige Angaben:
Standpunkt des Starts 

Der Code kann ohne weitere Angaben ausgefuehrt werden. Alle Masseinheiten entsprechen den SI-Einheiten. Die Variabeln koennen direkt im Code veraendert werden. 

Die auskommentierten Linien wurden zum Testen des Codes benoetigt. 

Wenn man den Code ausf�hrt, werden die bewegung in x und y Richtung aufgezeigt. Andere m�glichkeiten sind auskommentiert daneben aufgezeigt. 

Der Test des Modells erfolgte �ber einen Flug, bei dem ich versuchte den Landepunkt mit dem Modell vorauszusagen. Die Berechnung wurde mit Messen der Distanz und des Winkels �berpr�ft. 
