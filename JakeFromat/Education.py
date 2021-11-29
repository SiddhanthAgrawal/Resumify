from EscapeCheck import EscapeCheck


def Education(file):
    indent = "    "
    file.write("%-----------EDUCATION-----------\n\\section{Education}\n" + indent + "\\resumeSubHeadingListStart\n" + indent * 2 + "\\resumeSubheading\n" + indent * 3 + "{")
    education = EscapeCheck(input("University/College: "))
    city = EscapeCheck(input("City: "))
    state = EscapeCheck(input("State: "))
    from_date = EscapeCheck(input("Education Start Date: "))
    end_date = EscapeCheck(input("Education End/Anticipated End Date: "))
    file.write(education + ", \\textit{" + city + ", " + state + "}}{" + from_date + " -- " + end_date + "}\n" + indent * 3 + "{")
    degree = EscapeCheck(input("Degree and field of Study: "))
    gpa = EscapeCheck(input("GPA: "))
    file.write(
        degree + "}{Cumulative GPA : " + gpa + "/4.00}\\newline\n" + indent * 3 + "%\\begin{itemize}[leftmargin=0.002in, label={}]\n" + indent * 3 + "% \\small{\\item{\n" + indent * 4 + "\\resumeItemListStart\n" + indent * 4 + "\\resumeItem{\\textbf{Relevant Coursework}}{: ")
    choiceRC = input("Do you want to add Relevant Courses (y/n): ")
    if choiceRC == "y":
        rel_coursework = EscapeCheck(input("Relevant Coursework: "))
        file.write(rel_coursework + "}\n" + indent * 3 + "\\resumeItemListEnd\n" + indent * 3 + "\\resumeSubHeadingListEnd\n\n\n")
