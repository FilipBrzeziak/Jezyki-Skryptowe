@ECHO OFF
::a1=date b7=deaths c7=country

ECHO Wybierz kraj:
SET /P kraj=
ECHO Wybierz ile dni wyswietlic:
SET /P dni=
::SET /A dni=%dni%

::DEL temp_Deaths.txt
::DEL temp_sortDeaths.txt

TYPE NUL > temp_Deaths.txt
TYPE NUL > temp_sortDeaths.txt

FOR /F "skip=1 tokens=1,6,7" %%a IN (Covid.txt) DO (
    IF %%c == %kraj% echo %%c    %%a    %%b>> temp_Deaths.txt
)

java Sort < temp_Deaths.txt > temp_sortDeaths.txt
ECHO Najlepsze dni:
Head %dni% < temp_sortDeaths.txt
ECHO Najgorsze dni:
Tail %dni% < temp_sortDeaths.txt
