from jinja2 import Environment, FileSystemLoader
from utils import saveToFile
environment = Environment(loader=FileSystemLoader("files/"))
template = environment.get_template("include/automation/leak.yaml.template")
sensors = ["shower_water",
           "shower_water2",
           "kitchen_water",
           "dishmachine_water",
           "filter_water",
           "aqua_water",
           "bath_water",
           "bath_water2",
           "underbath_water"]
result = template.render(sensors=sensors)

print(result)
saveToFile(template,result)
