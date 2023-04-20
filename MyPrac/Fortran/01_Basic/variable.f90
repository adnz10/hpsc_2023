program main
        implicit none
        ! integer
        integer::n
        ! constant
        integer,parameter::m=1000
        ! Real type
        real(kind=4)::x,y
        real(kind=8)::p,q
        ! Logical
        logical :: debug
        logical,parameter::on=.false.
        ! Complex
        complex :: c,c2
        ! Character
        character(len=10)::arg
        n = -10
        x = 3.14
        y = 12.3
        p = 4.d15
        debug = .true.
        c = (1.,2.)
        c2 = cmplx(x,y)
        arg = 'this is'
        print *,'n = ', n
        print *,'x = ', x
        print *,'y = ', y
        print *,'p = ', p
        print *,'debug = ', debug
        print *,'c = ', c
        print *,'c2 = ', c2
        print *, 'arg =', arg
        print *, 'on = ',on

end program

