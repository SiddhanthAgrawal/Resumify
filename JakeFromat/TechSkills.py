from EscapeCheck import EscapeCheck


def TechSkills(file):
    write_string = ""
    indent = "    "
    write_string += "\n\n%-----------PROGRAMMING SKILLS-----------\n"
    write_string += "\section{Technical Skills}\n"
    write_string += indent + "\\begin{itemize}[leftmargin=0.15in, label={}]\n"
    write_string += indent * 2 + "\small{\item{\n"
    print("\nTechnical Skills")
    i = 1
    while True:
        print("\nTechnical Skills {}".format(i))
        print()
        category = EscapeCheck(input("Technical Skill Category (eg: Languages, Frameworks, Libraries, etc.): "))
        skills_string = "\n{}: ".format(category)
        skills = EscapeCheck(input(skills_string))
        write_string += indent * 3 + "\\textbf{" + category + "}{: " + skills + "} \\\\\n"
        choice = input("\nDo you want to add more Skill Category and Skills (y/n): ")
        if choice.lower() != "y":
            break
        i += 1
    write_string += indent * 2 + "}}\n"
    write_string += indent + "\end{itemize}\n"
    file.write(write_string)
    print("\nYour resume is complete!\n")

