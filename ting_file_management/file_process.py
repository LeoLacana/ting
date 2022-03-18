from email import message
import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    if len(instance) != 0:
        return None
    else:
        instance.enqueue(path_file)
        return sys.stdout.write(str(result))


def remove(instance):
    if not len(instance.queue_list):
        return sys.stdout.write("Não há elementos\n")
    else:   
        return sys.stdout.write(f"Arquivo {instance.dequeue()} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
