! Fortran is not case sensitive, No formating, Statically Typed Language, Recursive, 1 indexing

! Single line comment

! Syntex 
Program prgname
        implicit none 
end program

! Object File / Compile (compile one file for multi dependency/subroutines can be done)
gfortran -c prgname.f90 !prgname.o format
! Linking (all files are necessary (Subroutines))
gfortran prgname.o !output is >>>>>'a.out'
! run a.out as ./a.out ...........  can also use '> output.txt' to dump the output 
! Both Together object and compile
gfortran prgname.f90
! change exec output name
gfortran prgname.f90 -0 prgname.exe ! other name than a.out

! Variable (Data Types)......................................
Program datatype
        implicit none
        integer :: i
        i = 1.d0 ! 10^0
        i = 1.d-1 ! 10^-1
        real(kind=8)::x,y
        integer, parameter :: n = 1000
        logical :: f
        f =.true.

        ! Arrays............................
        real(kind=8),dimensions(6)::m
        m = (/1,2,3,4,5,6,7/)
        real(kind=8)::x(2),y(3)
        real(kind=8)::x(0:2),y(4:6)

        ! Matrix
        real(kind=8),dimension(3,2)::mat
        mat = reshape((/1,2,3,4,5,6/),(/3,2/)) ! Along column fill

        ! Dynamic Allocation
        real(kind=8),dimension(:),allocatable::x
        allocate(x(10))
end program

! Output.................................................
program output
        implicit none
        print *,'something is ',i
        end program 
! Input ...................................................
program input
        read *,inputi
        end program

!....................Loop.................................

! For Loop
        integer,paramter::n=100
        integer ::i
        do i=1,n
                y(i) = n
        enddo

        do i = 1,10,2
        enddo

! While Loop
        do while (i<5)
                i = i+1
        enddo

! if else
        if (i<=5) then
                print *,'abc'
        elseif (i>5 .and. i<10) then
                print *,'bcd'
        else

        endif

! Logical..............................................
.and.! ....................... and
.or. !.........................or
/= !..........................notequal
?= !..........................make not equal run env variable than

! ...................function.................................
program fcn
        implicit none
        real(kind=8)::x,z
        real(kind=8),external::f
        z = f(x)
end program

real(kind=8) function f(x)
        implicit none
        real(kind=8), intent(in) :: x
        f = x**2
        end function f

!................Subroutines....................................
program sub
        implicit none
        real(kind=8) ::x,y,z

        call fsub(x,y,z)
        end program
subroutine fsub(x,y,z)
        implicit none
        real(kind=8), intent(in) :: x
        real(kind=8), intent(out) :: y
        real(kind=8), intent(inout) ::z
        z = z*10
        y = z+x
        end subroutine fsub
