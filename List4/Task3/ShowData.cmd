@echo off
GOTO start
:blad
echo Podales nieprawidlowe dane!

:start
echo Zad 3/1 Filip Brzeziak
echo Podaj kraj:
set /p kraj=
echo Podaj zakres miesiecy miedzy marcem a listopadem (np podanie 3 i następnie 5 oznacza zakres marzec-maj):
echo Od:
set /p dolnyZakres=
echo Do:
set /p gornyZakres=

set /a dolnyZakres= %dolnyZakres%
set /a gornyZakres= %gornyZakres%


if %dolnyZakres% lss 3 GOTO blad
if %gornyZakres% gtr 11 GOTO blad
if %gornyZakres% lss %dolnyZakres% GOTO blad

type nul > tempCovid.txt

choice /c PZ /m "Co chcesz poznac?: P - Przypadki / Z - Zgony "
set /a choiceResult= %ERRORLEVEL%

for /f "skip=1 tokens=2,3,5,6,7" %%a in (Covid.txt) do (
    if %%e == %kraj% (
        if %%b geq %dolnyZakres% (
            if %%b leq %gornyZakres% (
               if %choiceResult% equ 1 (
                    echo Dzien: %%a miesiac: %%b Przypadki: %%c %%e
                    echo %%c>> tempCovid.txt
               ) else (
                    echo Dzien: %%a miesiac: %%b Zgodnow: %%d %%e
                    echo %%d>> tempCovid.txt
               )
            )
        )
    )
)
echo Suma:
java SUM < tempCovid.txt
echo Srednia na dzien:
java AVG < tempCovid.txt
del tempCovid.txt

::sciaga a2=day b5=month c6=cases d7=deaths e8=country