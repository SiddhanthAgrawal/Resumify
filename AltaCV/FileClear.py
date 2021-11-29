def FileClear(file, lines):
    template = lines[:100]
    template = template[:99] + [template[99][:10]]
    template_string = ""
    for line in template:
        template_string += line
    file.close()
    file = open("tex1string.tex", "w")
    file.write(template_string)