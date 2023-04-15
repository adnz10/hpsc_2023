program monte_carlo_pi
    use omp_lib
    implicit none
    integer :: i,inside,inside0,inside1,inside2,inside3,num_points,thread_num,nthread
    real(kind=8) :: x,y,dist,estimate_pi
    character(len=32) :: arg
    
    ! read num_points as command line argument.
    ! Run the code as: './a.out 100'
    call get_command_argument(1, arg)
    read(arg , *) num_points

    !print *, num_points
    inside0 = 0
    inside1 = 0
    inside2 = 0
    inside3 = 0
    !$ call omp_set_num_threads(4)
    !$omp parallel do private(x,y,dist)    
    do i=1,num_points

        call random_number(x)
        x = x-0.5
        !print *, "x=", x
        call random_number(y)
        y = y-0.5
        !print *, "y=", y

        dist=sqrt(x**2 + y**2)
        !print *, "dist=", dist
        !$ nthread = omp_get_thread_num()
            
        if (dist < 0.5) then
                !$ if (nthread == 0) then
                        inside0 = inside0 + 1
                !$ elseif (nthread == 1) then
                !$      inside1 = inside1 + 1
                !$ elseif (nthread == 2) then
                !$      inside2 = inside2 + 1
                !$ else
                !$      inside3 = inside3 + 1
                !$ endif
        endif

    enddo
    !$omp end parallel do
    inside = inside0+inside1+inside2+inside3
    print *, inside, "points fall inside the circle out of", num_points, "points"
            
    estimate_pi = (inside * 4.d0) / num_points
    print *, "estimate_pi=",estimate_pi

end program monte_carlo_pi

