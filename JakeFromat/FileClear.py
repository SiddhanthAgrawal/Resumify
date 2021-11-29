def FileClear(file, lines):
    template = lines[:122]
    template = template[:121] + [template[121][:19]]
    template_string = ""
    for line in template:
        template_string += line
    file.close()
    file = open("template.tex", "w")
    file.write(template_string)