from EscapeCheck import EscapeCheck


def Projects(file):
    write_string = ""
    indent = "    "
    write_string += "\n\n" + indent * 2 + "% ----- PROJECTS -----\n"
    write_string += indent * 2 + "\cvsection{Projects}\n"
    print("\nProjects")
    i = 1
    while True:
        print("\nProject {}".format(i))
        print()
        ProjectName = EscapeCheck(input("Name of the Project: "))
        gityn = input("Do you want to add a github link (y/n): ")
        if gityn == "y":
            github = input("Github link: ")
        webyn = input("Do you want to add a website link (y/n): ")
        if webyn == "y":
            website = input("Website link: ")
        ItemList = []
        while True:
            ItemList.append(EscapeCheck(input("Bullet point: ")))
            choice = input("Do you want to add more bullet points (y/n): ")
            if choice.lower() != "y":
                break
        write_string += indent * 3 + "\cvevent{" + ProjectName + " }"
        write_string += "{"
        if gityn == "y" or webyn == "y":
            if gityn == "y":
                write_string += "\cvrepo{|\n"
                write_string += indent * 3 + "\\faGithub}{" + github + "}"
            if webyn == "y":
                write_string += "\cvrepo{|\n"
                write_string += indent * 3 + "\\faGlobe}{" + website + "}"
        write_string += "}"
        write_string += "{}{}\n"
        write_string += indent * 3 + "\\begin{itemize}\n"
        for des in ItemList:
            write_string += indent * 4 + "\item " + des + "\n"
        write_string += indent * 3 + "\\end{itemize}\n"
        choice = input("\nDo you want to add more Projects (y/n): ")
        if choice.lower() != "y":
            break
        i += 1
        write_string += indent * 3 + "\divider\n\n"
    file.write(write_string)
    file.write(indent + "\n\end{paracol}\n")
    file.write("\end{document}")