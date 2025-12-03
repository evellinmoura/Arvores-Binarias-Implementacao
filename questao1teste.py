from questão1 import LinkedBinaryTree  # ou colar o código direto

def testar():
    print("\n=== INICIANDO TESTES ===")

    T = LinkedBinaryTree()

    print("\n[1] Testando criação da raiz...")
    r = T.add_root(10)
    assert T.root().element() == 10
    assert len(T) == 1
    print("OK ✔️")

    print("\n[2] Testando inserção de filhos...")
    l = T.add_left(r, 5)
    rr = T.add_right(r, 20)
    assert T.left(r).element() == 5
    assert T.right(r).element() == 20
    assert len(T) == 3
    print("OK ✔️")

    print("\n[3] Testando filhos do filho...")
    ll = T.add_left(l, 2)
    lr = T.add_right(l, 7)
    assert T.left(l).element() == 2
    assert T.right(l).element() == 7
    assert len(T) == 5
    print("OK ✔️")

    print("\n[4] Testando propriedades...")
    assert T.is_leaf(ll)
    assert not T.is_leaf(l)
    assert T.is_root(r)
    assert not T.is_root(l)
    print("OK ✔️")

    print("\n[5] Testando parent...")
    assert T.parent(l).element() == 10
    assert T.parent(ll).element() == 5
    print("OK ✔️")

    print("\n[6] Testando replace...")
        # ou colar o código direto

    print("\n[6] Testando replace...")
    old = T.replace(l, 8)
    assert old == 5
    assert l.element() == 8
    print("OK ✔️")

    print("\n[7] Testando delete (caso 1 filho)...")
    T.delete(lr)  # remove nó "7"
    assert len(T) == 4
    print("OK ✔️")

    print("\n[8] Testando delete (caso 0 filhos)...")
    T.delete(ll)  # remove nó "2"
    assert len(T) == 3
    print("OK ✔️")

    print("\n[9] Testando delete raiz...")
    T.delete(r)
    assert len(T) == 2
    print("OK ✔️")

    print("\n=== TODOS OS TESTES PASSARAM ✔️🔥 ===")

testar()