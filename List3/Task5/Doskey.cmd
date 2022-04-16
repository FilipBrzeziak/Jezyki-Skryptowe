doskey a=xcopy /S $1 $2

doskey e=dir  /a-d %1 ^| find /v "Directory" ^| find ":" ^| sort /+20  ^| Head 1

doskey f=dir  /a-d %1 ^| find /v "Directory" ^| find ":" ^| sort /+20 /r ^| Head 1
