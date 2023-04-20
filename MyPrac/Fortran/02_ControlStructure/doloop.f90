program main
        integer::i,n
        character(len=32)::arg
        call get_command_argument(1,arg)
        read(arg,*) n
        do i=1,n
                print*,i
                enddo
                end program
