from EscapeCheck import EscapeCheck


def Profile(file):
    write_string = ""
    indent = "    "
    name = EscapeCheck(input("Full Name: "))
    write_string += " " + name
    write_string += "} \\\\ \\vspace{1pt}\n"
    write_string += indent + "\small \\raisebox{-0.1\height}\\faPhone\ "
    phone = EscapeCheck(input("Phone Number: "))
    if "-" in phone:
        write_string += phone
    else:
        write_string += phone[:3] + "-" + phone[3:6] + "-" + phone[6:]
    write_string += " ~ \href{mailto:"
    email = EscapeCheck(input("E-Mail: "))
    write_string += email
    write_string += "}{\\raisebox{-0.2\height}\\faEnvelope\\  \\underline{"
    write_string += email
    write_string += "}} ~ \n" + indent + "\href{https://"
    linkedin = EscapeCheck(input("Linkedin (linkedin.com/in/..../): "))
    write_string += linkedin
    write_string += "}{\\raisebox{-0.2\\height}\\faLinkedin\\ \\underline{"
    write_string += linkedin
    write_string += "}} ~ \n" + indent + "\\href{https://"
    github = EscapeCheck(input("GitHub (github.com/...): "))
    write_string += github
    write_string += "}{\\raisebox{-0.2\\height}\\faGithub\\ \\underline{"
    write_string += github
    write_string += "}}\n" + indent + "\\vspace{-8pt}\n\\end{center}\n\n"
    file.write(write_string)
