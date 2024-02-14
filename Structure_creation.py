import shutil


def copy_wano_to_structure():
    shutil.copyfile('rendered_wano.yml', 'structure.yml')


if __name__ == '__main__':
    copy_wano_to_structure()
