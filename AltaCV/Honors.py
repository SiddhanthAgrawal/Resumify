from EscapeCheck import EscapeCheck


def Honors(file):
    print("\nHonors & Awards\n")
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- HONORS -----\n"
    write_string += indent * 2 + "\cvsection{Honors}\n"
    write_string += indent * 3 + "\\begin{itemize}\n"
    i = 1
    while True:
        write_string += indent * 4 + "\item "
        honor = EscapeCheck(input("Honor {}: ".format(i)))
        write_string += honor + "\n"
        check = input("Do you want to add more honors (y/n): ")
        if check != "y":
            break
    write_string += indent * 3 + "\\end{itemize}\n"
    write_string += indent * 3 + "\smallskip\n\n"
    write_string += indent * 2 + "\\newpage\n\n"
    write_string += indent * 2 + "\switchcolumn\n\n"
    file.write(write_string)