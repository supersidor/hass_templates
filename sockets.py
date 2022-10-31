from jinja2 import Environment, FileSystemLoader
from utils import saveToFile, save

environment = Environment(loader=FileSystemLoader("files/"))
templateUtility = environment.get_template("include/sockets/utility.yaml.template")
templateMoney = environment.get_template("include/sockets/money.yaml.template")
sockets = ["aqua_filter",
           "aqua_light",
           "boiler",
           "cabinet",
           "computer",
           "drymachine",
           "dishmachine",
           "freezer",
           "fridge",
           "nas",
           "washmachine",
           "berdoom_tv"
        ]

for socket in sockets:
    result = templateUtility.render(name=socket)
    print(result)
    save("include/utility_meter/"+socket+".yaml",result)
    result = templateMoney.render(name=socket)
    print(result)
    save("include/sensor/money/"+socket+".yaml",result)
    #saveToFile(template,result)
# template.name
#
# with open("output", "w") as fh:
#     fh.write(result)
