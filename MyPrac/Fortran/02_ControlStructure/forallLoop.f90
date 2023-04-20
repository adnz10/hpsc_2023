program main
        ! execute i in any order(compiler), used in parallel programing
        integer::i,n
        real(kind=4), dimension(10)::x
        !character(len=32)::arg
        !call get_command_argument(1,arg)
        !read(arg,*) n
        n = 10
        forall (i=1:n)
                x(i) = i          
                ! cant put print in forall statement 
        endforall
   
        print *,x
                end program
