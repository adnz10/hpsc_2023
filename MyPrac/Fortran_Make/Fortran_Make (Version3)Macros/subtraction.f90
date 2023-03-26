! addition
subroutine subtraction(num1,num2,sub)
        implicit none
        real(kind = 8),intent(in)::num1,num2
        real(kind = 8),intent(out)::sub
        sub = num1-num2
end subroutine
