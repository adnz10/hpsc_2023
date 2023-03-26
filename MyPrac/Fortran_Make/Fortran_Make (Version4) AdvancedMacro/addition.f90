! addition
subroutine addition(num1,num2,add)
        implicit none
        real(kind = 8),intent(in)::num1,num2
        real(kind = 8),intent(out)::add
        add = num1+num2
end subroutine
