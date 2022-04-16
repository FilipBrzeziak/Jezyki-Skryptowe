@echo off
dir /a:-d /s /-c | find ":" | find /v "Directory of" | sort /+20 /r | Head 2