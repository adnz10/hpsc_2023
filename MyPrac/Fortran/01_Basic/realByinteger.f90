program main
        implicit none
        real(kind=8)::x
        integer::n,m
        m = 3
        x = 10.
        n = 5
        print *,'x=10.0 n = 5, m =3'
        print *,'x/n',x/n
        print *,'m/n',m/n
end program
