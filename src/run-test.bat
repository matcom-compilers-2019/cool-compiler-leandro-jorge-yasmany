@echo off 
echo Compilando pueba de factorial-recursivo
python main.py test/factorial-recursivo.cl test-mips/factorial-recursivo.mips

echo Compilando pueba de factorial-iterativo
python main.py test/factorial-iterativo.cl test-mips/factorial-iterativo.mips

echo Compilando pueba de herencia
python main.py test/herencia.cl test-mips/herencia.mips

echo Compilando pueba de let-case
python main.py test/let-case.cl test-mips/let-case.mips

echo Compilando pueba de input
python main.py test/input.cl test-mips/input.mips

echo Compilacion finalizada :)
pause