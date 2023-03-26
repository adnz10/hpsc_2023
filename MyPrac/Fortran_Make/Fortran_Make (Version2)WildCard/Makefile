
output.txt : run.exe
	./run.exe > output.txt
run.exe : main.o addition.o subtraction.o
	gfortran main.o addition.o subtraction.o -o run.exe
%.o : %.f90
	gfortran -c $< 


