! Fortran code to calculate square root usint the Newton's method 

program main
        ! takes input for calculating sqrt
        implicit none
        real(kind=8) :: x,y
        print *,'Enter a number'
        read *,x
        if (x==0) then
                y = 0
        elseif (x<0) then
                print*,"Sqrt is not defined for negative number"
        else
                call sqrtNt(x,y)
                print *,'Sqrt =',y
        endif

end program

subroutine sqrtNt(x,y)
        implicit none
        real(kind=8),intent(in) :: x
        real(kind=8),intent(out) :: y
        real(kind=8)::s0,s,tol,delta_s
        integer :: i,kmax
        s = 1
        kmax = 100
        tol = 1.d-14
        do i=1,kmax
                s0 = s
                s = 0.5*(s+x/s)
                delta_s = s-s0
                if( (abs(delta_s)/x) < tol) then
                  exit
          endif       
        enddo
        y = s
end subroutine sqrtNt
