from app import services

def setup_function():
    # roda antes de cada teste
    services.usuarios_cadastrados.clear()
    services.next_id = 1


def test_cadastrar_user_cria_com_id_incremental():
    u1 = services.cadastrar_user("Ana", 20)
    u2 = services.cadastrar_user("Bob", 30)

    assert u1["id"] == 1
    assert u2["id"] == 2
    assert u1["nome"] == "Ana"
    assert u2["idade"] == 30


def test_mostrar_cadastros_retorna_lista():
    assert services.mostrar_cadastros() == []

    services.cadastrar_user("Ana", 20)
    users = services.mostrar_cadastros()

    assert isinstance(users, list)
    assert len(users) == 1
    assert users[0]["nome"] == "Ana"


def test_deletar_user_existente_retorna_true_e_remove():
    u1 = services.cadastrar_user("Ana", 20)
    ok = services.deletar_user(u1["id"])

    assert ok is True
    assert services.mostrar_cadastros() == []


def test_deletar_user_inexistente_retorna_false():
    ok = services.deletar_user(999)
    assert ok is False
