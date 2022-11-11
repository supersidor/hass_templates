from jinja2 import Environment, FileSystemLoader

from utils import save

environment = Environment(loader=FileSystemLoader("files/"))
template = environment.get_template("include/automation/heat_head.yaml.template")
heads = [("bedroom_heat", "bedroom_temperature"),
         ("child_heat", "child_temperature"),
         ("kitchen_heat", "kitchen_temperature"),
         ("cabinet_heat", "cabinet_temperature")]

for (sensor,temperature) in heads:
    result = template.render(sensor=sensor, temperature=temperature)
    print(result)
    save("include/automation/heat_head/" + str(sensor) + ".yaml", result)
