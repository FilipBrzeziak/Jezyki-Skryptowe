@echo off
GOTO start
:blad
echo Bledne dane!

:start
echo Podaj kontynent:
set /p kontynent=
echo Podaj numer miesiaca miedzy marcem a listopadem:
set /p miesiac=
set /a miesiac= %miesiac%

if %miesiac% lss 3 GOTO blad
if %miesiac% gtr 11 GOTO blad

type nul > daneKontynentTemp.txt

for /f "skip=1 tokens=3,5,11" %%a in (Covid.txt) do (
    if %kontynent% equ %%c (
        if %miesiac% equ %%a (
            echo %%b>> daneKontynentTemp.txt
        )
    )
)

echo Sumaryczna ilosc przypadkow na kontynencie %kontynent%:
java SUM < daneKontynentTemp.txt

del daneKontynentTemp.txt
::sciaga a3=month b5=cases c11=kontynent