program main
        real(kind=8)::x
        real(kind=8),external::procedure,func2
        x = 5
        area=procedure(x)
        resultant = func2(x)
        print*,area
        print*,resultant
end program

function procedure(x)
        real(kind=8)::procedure
        real(kind=8),intent(in)::x
        procedure = 10*x
        end function procedure
! Different name
function func2(x) result(something)
        real(kind=8)::something
        real(kind=8),intent(in)::x
        something = 5*5
        end function func2
