from ting_file_management.file_management import txt_importer


def test_validar_importar_noticias_com_sucesso(capsys):
    text_file = [
        "Acima de tudo,",
        "é fundamental ressaltar que a adoção de "
        "políticas descentralizadoras nos obriga",
        "à análise do levantamento das variáveis envolvidas.",
    ]
    assert txt_importer("statics/arquivo_teste.txt") == text_file


def test_validar_importar_com_extencao_invalida(capsys):
    txt_importer("statics/arquivo_teste.csv")
    out, err = capsys.readouterr()
    assert err == "Formato inválido\n"


def test_validar_importar_com_arquivo_nao_existente(capsys):
    txt_importer("statics/arquivo_nao_existe.txt")
    out, err = capsys.readouterr()
    assert err == "Arquivo statics/arquivo_nao_existe.txt não encontrado\n"
