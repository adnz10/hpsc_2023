program main
        implicit none
        integer::num,num2
        character(len=32)::arg

        call get_command_argument(1,arg)
        call get_command_argument(2,arg)
        read(arg,*) num
        read(arg,*) num2
        print*,'num = ',num
        print*,'num2 = ',num2
end program
