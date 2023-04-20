program main
       ! Also refered as structure
        type::atom
                character(len=2)::label
                real::x,y,z
        end type atom

        type(atom)::particle
        type(atom),dimension(3)::mcb

        !mcb(1)%type = 'C'

        particle%label = 'ab'
        particle%x = 10
        particle%y = 20
        particle%z = 30


        print *, particle
        print *, mcb
end program
