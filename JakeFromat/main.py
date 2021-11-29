from FileClear import FileClear
from Profile import Profile
from Education import Education
from Experience import Experience
from Projects import Projects
from TechSkills import TechSkills

print("Hello")

file = open("template.tex", "r")
lines = file.readlines()
if len(lines) > 122:
    FileClear(file, lines)
file.close()

file = open("template.tex", "a")

Profile(file)
Education(file)
Experience(file)
Projects(file)
TechSkills(file)

file.write("\end{document}")

file.close()
