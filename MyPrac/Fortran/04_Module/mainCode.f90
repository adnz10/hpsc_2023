program main
        use module1,only:solve
        implicit none
        real(kind=8)::a,b
        a = 10
        call solve(a,b)
        print*,b
        end program
