program main
        implicit none 
        integer::n
        ! cant do n = 4 because only variable should be defined first
        integer,dimension(3,3)::matrix
        real,dimension(5)::vector
        real,dimension(1:4)::can
        real,dimension(1:3,1:3,1:3)::threeD
        real,dimension(3,3,3)::Multi
        can(2) = 10
        print *,Multi
end program
