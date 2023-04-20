program main
        real(kind=8)::x,y
        x = 10
        call sub(x,y)
        print *,y
        end program

        subroutine sub(x,y)
                real(kind=8),intent(in)::x
                real(kind=8),intent(out)::y
                y = x*10
                endsubroutine
