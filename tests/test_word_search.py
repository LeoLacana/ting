from ting_word_searches.word_search import search_by_word, exists_word
from ting_file_management.file_process import process
from ting_file_management.queue import Queue


text_exists_word = [
    {
        "palavra": "Pedro",
        "arquivo": "statics/nome_pedro.txt",
        "ocorrencias": [{"linha": 1}],
    }
]
text_search_by_word = [
    {
        "palavra": "pedro",
        "arquivo": "statics/nome_pedro.txt",
        "ocorrencias": [
            {
                "linha": 1,
                "conteudo": "Aqui contem um texto que fala sobre um menino pobre chamado Pedro.",  # noqa
            }
        ],
    }
]


def test_validar_funcao_exists_word_com_sucesso(capsys):
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = exists_word("Pedro", project)
    out, err = capsys.readouterr()
    assert word == text_exists_word


def test_validar_funcao_exists_word_sem_palavra_existente(capsys):
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = exists_word("Ratinho", project)
    out, err = capsys.readouterr()
    assert word == []


def test_validar_search_by_word_com_sucesso(capsys):
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = search_by_word("pedro", project)
    out, err = capsys.readouterr()
    assert word == text_search_by_word


def test_validar_search_by_word_com_palavra_inexistente(capsys):
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = search_by_word("Ratinho", project)
    out, err = capsys.readouterr()
    assert word == []
