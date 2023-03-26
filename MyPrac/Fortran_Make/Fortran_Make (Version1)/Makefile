
output.txt : run.exe
	./run.exe > output.txt
run.exe : main.o addition.o subtraction.o
	gfortran main.o addition.o subtraction.o -o run.exe
main.o : main.f90
	gfortran -c main.f90 
addition.o : addition.f90
	gfortran -c addition.f90
subtraction.o : subtraction.f90
	gfortran -c subtraction.f90

