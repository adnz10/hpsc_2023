OBJECTS = main.o addition.o subtraction.o
output.txt : run.exe
	./run.exe > output.txt
run.exe : $(OBJECTS)
	gfortran $(OBJECTS) -o run.exe
%.o : %.f90
	gfortran -c $< 


