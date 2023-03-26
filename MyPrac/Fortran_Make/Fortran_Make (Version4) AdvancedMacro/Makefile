FC = gfortran
FFLAGS = -O3
LFLAGS = 
OBJECTS = main.o addition.o subtraction.o
output.txt : run.exe
	./run.exe > output.txt
run.exe : $(OBJECTS)
	$(FC) $(LFLAGS) $(OBJECTS) -o run.exe
%.o : %.f90
	gfortran $(FFLAGS) -c $< 


