from jinja2 import Environment, FileSystemLoader
from utils import saveToFile
environment = Environment(loader=FileSystemLoader("files/"))
template = environment.get_template("include/sensor/friendly_temp_hum.yaml.template")
sensors = ["kitchen","bedroom","child","cabinet","bathroom","balcon","garderob"]
result = template.render(sensors=sensors)

print(result)
saveToFile(template,result)
# template.name
#
# with open("output", "w") as fh:
#     fh.write(result)
