from EscapeCheck import EscapeCheck


def Projects(file):
    write_string = ""
    indent = "    "
    write_string += "\n\n%-----------PROJECTS-----------\n"
    write_string += "\section{Projects}\n"
    write_string += indent + "\\resumeSubHeadingListStart\n"
    print("\nProjects")
    i = 1
    while True:
        print("\nProjects {}".format(i))
        print()
        write_string += indent * 2 + "\\resumeProjectHeading\n"
        ProjName = EscapeCheck(input("Project Name: "))
        LangFram = EscapeCheck(input("Languages and Frameworks used: "))
        ItemList = []
        while True:
            ItemList.append(EscapeCheck(input("Bullet point: ")))
            choice = input("Do you want to add more bullet points (y/n): ")
            if choice.lower() != "y":
                break
        write_string += indent * 3 + "{\\textbf{"
        write_string += ProjName
        write_string += "} $|$ \emph{"
        write_string += LangFram
        write_string += "}}{}\n"
        write_string += indent * 3 + "\\resumeItemListStart\n"
        for project in ItemList:
            write_string += indent * 4 + "\\resumeItem{" + project + "}\n"
        write_string += indent * 3 + "\\resumeItemListEnd\n"
        choice = input("\nDo you want to add more Projects (y/n): ")
        if choice.lower() != "y":
            break
        i += 1
    write_string += indent + "\\resumeSubHeadingListEnd\n"
    file.write(write_string)
