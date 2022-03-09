import pytest

from ting_file_management.queue import Queue


def test_enqueue_deve_adicionar_um_valor_a_fila():
    queue = Queue()
    queue.enqueue(42)
    assert len(queue) == 1


def test_dequeue_deve_remover_um_valor_a_fila():
    queue = Queue()
    queue.enqueue(42)
    queue.enqueue(43)
    queue.enqueue(44)

    given = queue.dequeue()
    assert len(queue) == 2
    assert given == 42


def test_search_deve_buscar_um_valor_a_partir_de_um_indice():
    queue = Queue()
    queue.enqueue(42)
    queue.enqueue(43)
    queue.enqueue(44)
    assert queue.search(0) == 42
    assert queue.search(1) == 43
    assert queue.search(2) == 44


def test_search_com_indice_invalido():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.search(0)
    queue.enqueue(42)
    with pytest.raises(IndexError):
        queue.search(-1)
    with pytest.raises(IndexError):
        queue.search(2)
