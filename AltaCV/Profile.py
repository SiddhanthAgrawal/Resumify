from EscapeCheck import EscapeCheck


def Profile(file):
    write_string = ""
    indent = "    "
    name = EscapeCheck(input("Full Name: "))
    write_string += name
    write_string += "}\n"
    write_string += indent + "\\tagline{"
    profession = EscapeCheck(input("Profession/Current Position: "))
    write_string += profession + "}\n\n"
    write_string += indent + "\personalinfo{\n"
    email = EscapeCheck(input("E-Mail: "))
    write_string += indent * 2 + "\email{" + email + "}\smallskip\n"
    write_string += indent * 2 + "\phone{"
    phone = EscapeCheck(input("Phone Number: "))
    if "-" in phone:
        write_string += phone
    else:
        write_string += phone[:3] + "-" + phone[3:6] + "-" + phone[6:]
    write_string += "}\n"
    write_string += indent * 2 + "\linkedin{"
    linkedin = EscapeCheck(input("Linkedin username: "))
    write_string += linkedin
    write_string += "}\n"
    write_string += indent * 2 + "\github{"
    github = EscapeCheck(input("Github username: "))
    write_string += github
    write_string += "}\n"
    write_string += indent + '}\n\n'
    write_string += indent + "\makecvheader\n\n"
    write_string += indent + "\columnratio{0.3}\n\n"
    file.write(write_string)