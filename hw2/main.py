import csv
import sys
import requests
from graphviz import Digraph
import re


def load_config(config_file):
    with open(config_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return next(reader)


def get_dependencies(package_name):
    dependencies = []

    try:
        response = requests.get(f'https://pypi.org/pypi/{package_name}/json').json()
        for i in response['info']['requires_dist']:
            match = re.search(r'[\w\-]+', i)
            dependencies.append(i[match.start():match.end()])
    except Exception as e:
        pass
    return dependencies


def create_dependency_graph(package_name,  dot, visited, depth=0, name=None):
    if name and name != package_name:
        dot.edge(name, package_name)
    if depth > 1:
        return
    visited.add(package_name)
    dependencies = get_dependencies(package_name)
    c = 0
    for i in dependencies:
        if i in visited:
            continue
        if c > 5:
            break
        c += 1
        dot.node(i)
        create_dependency_graph(i, dot, visited, depth + 1, package_name)


def main(config_file):
    config = load_config(config_file)

    package_name = config['package_name']
    output_image_path = config['image_path']

    dot = Digraph(comment='Dependency Graph')
    create_dependency_graph(package_name, dot, set())
    dot.render(output_image_path, format='png', cleanup=True)


if __name__ == "__main__":
    main(sys.argv[1])
