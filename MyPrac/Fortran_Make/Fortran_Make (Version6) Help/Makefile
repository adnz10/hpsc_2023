FC = gfortran
FFLAGS = -O3
LFLAGS = 
OBJECTS = main.o addition.o subtraction.o
.PHONY = clean clobber help
output.txt : run.exe
	./run.exe > output.txt
run.exe : $(OBJECTS)
	$(FC) $(LFLAGS) $(OBJECTS) -o run.exe
%.o : %.f90
	gfortran $(FFLAGS) -c $< 

clean :
	rm -f $(OBJECTS) run.exe
clobber :
	rm -f $(OBJECTS) run.exe output.txt
help : 
	echo 'Valid Target' run.exe output.txt
	@echo 'Dependencies' $(OBJECTS)
