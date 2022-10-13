from jinja2 import Environment, FileSystemLoader
from utils import saveToFile, save

environment = Environment(loader=FileSystemLoader("files/"))
template = environment.get_template("include/sockets/utility.yaml.template")
sockets = ["aqua_filter",
           "aqua_light",
           "boiler",
           "cabinet",
           "computer",
           "drymachine",
           "freezer",
           "fridge",
           "nas",
           "washmachine",
           "berdoom_tv"
        ]

for socket in sockets:
    result = template.render(name=socket)
    print(result)
    save("include/utility_meter/"+socket+".yaml",result)
    #saveToFile(template,result)
# template.name
#
# with open("output", "w") as fh:
#     fh.write(result)
