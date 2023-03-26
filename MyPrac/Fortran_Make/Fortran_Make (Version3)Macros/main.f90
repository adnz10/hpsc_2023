! Calculator

program main
        implicit none
        real (kind = 8)::num1,num2,add,sub
        num1 = 2
        num2 = 3
        call addition(num1,num2,add)
        call subtraction(num1,num2,sub)
        print *, 'Sum of number is ',add
        print *, 'Subtraction of number is ',sub

end program

