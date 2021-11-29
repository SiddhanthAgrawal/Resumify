from EscapeCheck import EscapeCheck


def Experience(file):
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- EXPERIENCE -----\n"
    write_string += indent * 2 + "\cvsection{Experience}\n"
    print("\nExperience")
    i = 1
    while True:
        print("\nExperience {}".format(i))
        print()
        CompanyName = EscapeCheck(input("Name of the Employer or the Company you worked with: "))
        StartDate = EscapeCheck(input("Start Date:  "))
        EndDate = EscapeCheck(input("End Date: "))
        Position = EscapeCheck(input("Position held: "))
        City = EscapeCheck(input("City: "))
        State = EscapeCheck(input("State: "))
        ItemList = []
        while True:
            ItemList.append(EscapeCheck(input("Bullet point: ")))
            choice = input("Do you want to add more bullet points (y/n): ")
            if choice.lower() != "y":
                break
        write_string += indent * 3 + "\cvevent{" + Position + " }{| " + CompanyName + "}"
        write_string += "{" + StartDate + " -- " + EndDate + "}{" + City + ", " + State + "}\n"
        write_string += indent * 3 + "\\begin{itemize}\n"
        for exp in ItemList:
            write_string += indent * 4 + "\item " + exp + "\n"
        write_string += indent * 3 + "\\end{itemize}\n"
        choice = input("\nDo you want to add more Work Experience (y/n): ")
        if choice.lower() != "y":
            break
        i += 1
        write_string += indent * 3 + "\divider\n\n"
    file.write(write_string)