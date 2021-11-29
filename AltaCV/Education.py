from EscapeCheck import EscapeCheck


def Education(file):
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- EDUCATION -----\n"
    write_string += indent * 2 + "\cvsection{Education}\n"
    print("\nEducation")
    i = 1
    while True:
        print("\nEducation Info {}".format(i))
        print()
        CompanyName = EscapeCheck(input("Name of the Institution: "))
        StartDate = EscapeCheck(input("Start Date:  "))
        EndDate = EscapeCheck(input("End Date: "))
        Position = EscapeCheck(input("Degree and field of Study: : "))
        City = EscapeCheck(input("City: "))
        State = EscapeCheck(input("State: "))
        GPA = EscapeCheck(input("GPA: "))
        write_string += indent * 3 + "\cvevent{" + Position + " }{| " + CompanyName + "}"
        write_string += "{" + StartDate + " -- " + EndDate + "}{" + City + ", " + State + "}\n"
        write_string += indent * 3 + "\\begin{itemize}\n"
        write_string += indent * 4 + "\item GPA: " + GPA + "\n"
        write_string += indent * 3 + "\\end{itemize}\n"
        choice = input("\nDo you want to add more Education Sections (y/n): ")
        if choice.lower() != "y":
            break
        i += 1
        write_string += indent * 3 + "\divider\n\n"
    file.write(write_string)