from EscapeCheck import EscapeCheck


def Experience(file):
    indent = "    "
    file.write("%-----------EXPERIENCE-----------\n\\section{Experience}\n" + indent + "\\resumeSubHeadingListStart\n\n")
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
        file.write(indent * 2 + "\\resumeSubheading\n" + indent * 3 + "{" + CompanyName + "}{" + StartDate + " -- " + EndDate + "}\n")
        file.write(indent * 3 + "{" + Position + "}{" + City + ", " + State + "}\n")
        file.write(indent * 3 + "\\resumeItemListStart\n")
        for responsibility in ItemList:
            file.write(indent * 4 + "\\resumeItem{" + responsibility + "}\n")
        file.write(indent * 3 + "\\resumeItemListEnd\n")
        choice = input("\nDo you want to add more Work Experience (y/n): ")
        if choice.lower() != "y":
            break
        i += 1
    file.write(indent * 3 + "\\resumeSubHeadingListEnd")
