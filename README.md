# aris-recovery-prediction
Maturaarbeit Alexander Doongaji EMS Schiers 2020

Der Code wurde mit Hilfe der Spyder IDE geschrieben. Ein Python interpreter wird benoetigt um den Code laufen zu lassen. 

Das Wetter kommt von der OpenWeatherMap API. 

Nötige Variablen: 
roh = Dichte der Luft
c_d = Dragcoefficient -> zusammenfassung meherer komplexen Werte. Nötig für die berechnung des Luftwiederstands 
t_b = burn time 
F = Kraft des Triebwerkes 
m = Masse mit Triebsatz
a_burn = Beschleunigung 
A = Oberfläche der Rakete
A_Para = Fläche des Fallschirms 
dt = timestep
D = zusammenfassung der Konstanten Werter der Wiederstandsgleichung 
Nötige Angaben:
Standpunkt des Starts 

Der Code kann ohne weitere Angaben ausgefuehrt werden. Alle Masseinheiten entsprechen den SI-Einheiten. Die Variabeln koennen direkt im Code veraendert werden. 

Die auskommentierten Linien wurden zum Testen des Codes benoetigt. 

Wenn man den Code ausführt, werden die bewegung in x und y Richtung aufgezeigt. Andere möglichkeiten sind auskommentiert daneben aufgezeigt. 

