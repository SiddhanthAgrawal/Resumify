from EscapeCheck import EscapeCheck


def AboutMe(file):
    print("\nAbout Me\n")
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- ABOUT ME -----\n"
    write_string += indent * 2 + "\cvsection{About Me}\n"
    write_string += indent * 3 + "\\begin{quote}\n"
    aboutme = EscapeCheck(input("Write something about yourself: "))
    write_string += indent * 4 + aboutme + "\n"
    write_string += indent * 3 + "\end{quote}\n"
    file.write(write_string)