import csv
import sys
import pkg_resources
from graphviz import Digraph


def load_config(config_file):
    with open(config_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return next(reader)


def get_dependencies(package_name):
    dependencies = set()

    try:
        dist = pkg_resources.get_distribution(package_name)
        for req in dist.requires():
            dependencies.add(req.project_name)
            dependencies.update(get_dependencies(req.project_name))
    except Exception as e:
        raise ValueError(f"Ошибка при получении зависимостей для {package_name}: {e}")

    return dependencies


def create_dependency_graph(package_name, dependencies, output_path):
    dot = Digraph(comment='Dependency Graph')

    dot.node(package_name)

    for dep in dependencies:
        dot.node(dep)
        dot.edge(package_name, dep)

    dot.render(output_path, format='png', cleanup=True)
    print(f"Граф зависимостей успешно сохранен в {output_path}")


def main(config_file):
    config = load_config(config_file)

    package_name = config['package_name']
    output_image_path = config['image_path']

    dependencies = get_dependencies(package_name)

    create_dependency_graph(package_name, dependencies, output_image_path)


if __name__ == "__main__":
    main(sys.argv[1])
