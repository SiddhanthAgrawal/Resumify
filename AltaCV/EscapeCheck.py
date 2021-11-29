def EscapeCheck(inpString):
    operators = ["&", "%", "$", "#", "_", "{", "}", "^", "\\", "#"]
    outString = ""
    for ch in inpString:
        if ch in operators:
            if ch == "\\":
                outString += "\\textbackslash "
            elif ch == "#":
                outString += "##"
            else:
                outString += "\\" + ch
        else:
            outString += ch
    return outString