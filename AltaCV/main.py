from FileClear import FileClear
from Profile import Profile
from AboutMe import AboutMe
from Education import Education
from Experience import Experience
from Projects import Projects
from Skills import Skills
from Activities import Activities
from Languages import Languages
from Honors import Honors

file = open("AltaResume.tex", "r")
lines = file.readlines()
if len(lines) > 100:
    FileClear(file, lines)
file.close()

file = open("AltaResume.tex", "a")

Profile(file)
Skills(file)
Activities(file)
Languages(file)
Honors(file)
AboutMe(file)
Experience(file)
Education(file)
Projects(file)
