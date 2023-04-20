program main
        real(kind=8),external::nfactorial
        real(kind=8)::answer
        integer,parameter::n=10
        answer = nfactorial(n)
        print *, answer
        end program 
recursive function nfactorial(n) result(fac)
        integer,intent(in)::n
        real(kind=8)::fac

        select case(n)
        case (0:1)
                fac = 1
        case default
                fac = n * nfactorial(n-1)
        end select
end function nfactorial
