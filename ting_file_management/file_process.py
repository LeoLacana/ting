import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    print(instance.queue_list)
    
    if len(instance) != 0 and path_file in instance.queue_list:
        return None
    else:
        instance.enqueue(path_file)
        return sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
