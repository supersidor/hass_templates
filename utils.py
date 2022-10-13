import os


def saveToFile(template: "Template", result: str):
    save( template.name.replace(".template", ""), result)

def save(path: str, result: str):
    saveToPath = "output/" + path
    os.makedirs(os.path.dirname(saveToPath), exist_ok=True)
    with open(saveToPath, "w") as fh:
        fh.write(result)
