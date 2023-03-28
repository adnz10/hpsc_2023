
module method
        implicit none
        real(kind =8)::x,y,globalIn
contains
   
subroutine solve(x,y)
        implicit none 
        real(kind=8), intent(in) :: x
        real(kind=8),intent(out) :: y
        
        if (x<10) then
                y = 10*x
        else if (x>10 .and. x<100) then
                y = 100*x
        else
                print *, 'greater than 100'
        endif
end subroutine solve
end module method

