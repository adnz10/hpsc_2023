
program main
        real::x,y
        interface
                subroutine sub(x,y)
                        real,intent(in)::x
                        real,intent(out)::y
                    
                end subroutine sub
                end interface
        x = 10
        call sub(x,y)

                endprogram

                subroutine sub(x,y)
                        y = 10*x
                        end subroutine
