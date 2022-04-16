echo off
ReturnCode.exe silnik sprzeglo chlodnica blotnik felga szyba zderzak
set /A KOD = %ERRORLEVEL%
set /A ZDERZAK=1
set /A SZYBA=2
set /A FELGA=4
set /A BLOTNIK=8
set /A CHLODNICA=16
set /A SPRZEGLO=32
set /A SILNIK=64

SET /A WYNIK="%KOD% & %SILNIK%"
IF %WYNIK% EQU %SILNIK% ECHO uszkodzony silnik

SET /A WYNIK="%KOD% & %SPRZEGLO%"
IF %WYNIK% EQU %SPRZEGLO% ECHO uszkodzone sprzeglo

SET /A WYNIK="%KOD% & %CHLODNICA%"
IF %WYNIK% EQU %CHLODNICA% ECHO uszkodzona chlodnica

SET /A WYNIK="%KOD% & %BLOTNIK%"
IF %WYNIK% EQU %BLOTNIK% ECHO uszkodzony blotnik

SET /A WYNIK="%KOD% & %FELGA%"
IF %WYNIK% EQU %FELGA% ECHO uszkodzona felga

SET /A WYNIK="%KOD% & %SZYBA%"
IF %WYNIK% EQU %SZYBA% ECHO uszkodzona szyba

SET /A WYNIK="%KOD% & %ZDERZAK%"
IF %WYNIK% EQU %ZDERZAK% ECHO uszkodzony zderzak

echo returning...