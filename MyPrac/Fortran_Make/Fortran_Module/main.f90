
program main

        use method, only:solve,globalIn
        implicit none
        real(kind=8)::a,b
        a = 8

        call solve(a,b)
        print *, b
        print *, globalIn

end program 
