from EscapeCheck import EscapeCheck


def Skills(file):
    print("\nSkills\n")
    write_string = ""
    indent = "    "
    write_string += indent + "\\begin{paracol}{2}\n"
    write_string += indent * 2 + "% ----- SKILLS -----\n"
    write_string += indent * 2 + "\cvsection{Skills}\n"
    i = 1
    while True:
        write_string += indent * 3 + "\cvtag{"
        skill = EscapeCheck(input("Skill {}: ".format(i)))
        i += 1
        write_string += skill + "}\n"
        check = input("Do you want to add more skills (y/n): ")
        if check != "y":
            break
    file.write(write_string)