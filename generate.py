from jinja2 import Environment, FileSystemLoader
environment = Environment(loader=FileSystemLoader("files/"))
results_template = environment.get_template("friendly_temp_hum.yaml.template")
sensors = ["kitchen","bedroom","child","cabinet","bathroom","balcon","garderob"]
print(results_template.render(sensors=sensors))
