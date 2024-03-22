import yaml
from ase.build import bulk
from ase.io import write


if __name__ == '__main__':
    with open('rendered_wano.yml') as fh:
        params = yaml.safe_load(fh)

    element = params.pop('element')
    struct = bulk(element, **params)
    write("structure.xyz", struct)
