module module1
        implicit none
        real(kind=8)::x,y
contains
        subroutine solve(x,y)
        real(kind=8),intent(in)::x
        real(kind=8),intent(out)::y

        y = 10*x

        end subroutine solve
end module module1
