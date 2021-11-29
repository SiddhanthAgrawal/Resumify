from EscapeCheck import EscapeCheck


def Activities(file):
    print("\nActivities and Involvements\n")
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- ACTIVITIES -----\n"
    write_string += indent * 2 + "\cvsection{Activities}\n"
    i = 1
    while True:
        write_string += indent * 3 + "\cvtag{"
        activity = EscapeCheck(input("Activity/Involvement {}: ".format(i)))
        i += 1
        write_string += activity + "}\n"
        check = input("Do you want to add more activities/involvements (y/n): ")
        if check != "y":
            break
    file.write(write_string)