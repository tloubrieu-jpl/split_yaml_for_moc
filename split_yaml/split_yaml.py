import yaml
import os
import sys
import pystache
from io import StringIO
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

KUSTOMIZATION_TEMPLATE = os.path.join(
    os.path.dirname(__file__),
    'kustomization.yaml.mustache')

def create_resource_file(target_path, doc):
    resource_file = os.path.join(
        target_path,
        doc['kind'].lower() + '.yaml')

    # create resource file
    with open(resource_file, 'w') as file:
        yaml.dump(doc, file)

def create_kustomization_file(target_path, doc):
    renderer = pystache.Renderer()
    kustomization = renderer.render_path(KUSTOMIZATION_TEMPLATE, {'kind': doc['kind'].lower()})

    kustomization_file = os.path.join(
        target_path,
        'kustomization.yaml'
    )
    with open(kustomization_file, 'w') as file:
        file.write(kustomization)


def create_files_from_yaml(doc, output_dir='.'):
    target_path = os.path.join(
        output_dir,
        doc['apiVersion'].split('/')[0],
        doc['kind'].lower(),
        doc['metadata']['name']
    )

    logger.debug("create %s dir", target_path)
    os.makedirs(target_path, exist_ok=True)

    create_resource_file(target_path, doc)
    create_kustomization_file(target_path, doc)


def main():
    input_file = r'./tests/spark-operator-giant.yaml'
    output_dir = '/Users/loubrieu/Documents/sdap/HLS/moc/apps/cluster-scope/base'
    current_yaml_content = ""
    with open(input_file) as file:
        line = file.readline()
        while line:
            if line != "---\n":
                current_yaml_content += line
            else:
                yml_stream = StringIO(current_yaml_content)
                doc = yaml.load(yml_stream)
                if doc:
                    create_files_from_yaml(doc, output_dir=output_dir)
                current_yaml_content = ""

            line = file.readline()


if __name__ == '__main__':
    main()






