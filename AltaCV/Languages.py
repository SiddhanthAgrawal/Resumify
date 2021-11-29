from EscapeCheck import EscapeCheck


def Languages(file):
    print("\nLanguages\n")
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- LANGUAGES -----\n"
    write_string += indent * 2 + "\cvsection{Languages}\n"
    i = 1
    while True:
        write_string += indent * 3 + "\cvlang{"
        lang = EscapeCheck(input("Langauge {}: ".format(i)))
        i += 1
        prof = EscapeCheck(input("Proficiency in {}: ".format(lang)))
        write_string += lang + "}{" + prof + "}\\\\\n"
        check = input("Do you want to add more languages (y/n): ")
        if check != "y":
            break
        write_string += indent * 3 + "\divider\n\n"
    write_string += indent * 3 + "\smallskip\n"
    file.write(write_string)