class Singleton:

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando nova instância...")
            cls._instancia = super().__new__(cls)
            cls._instancia.valor = 0
        else:
            print("Retornando instância existente.")
        return cls._instancia

    def incrementar(self):
        self.valor += 1

    def __repr__(self):
        return f"Singleton(id={id(self)}, valor={self.valor})"


# ─── Demonstração ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Padrão Singleton ===\n")

    a = Singleton()
    print(f"a → {a}\n")

    b = Singleton()
    print(f"b → {b}\n")

    print(f"a é b? {a is b}\n")   # True — mesma instância

    a.incrementar()
    a.incrementar()
    print(f"Após 2 incrementos em 'a':")
    print(f"  a.valor = {a.valor}")
    print(f"  b.valor = {b.valor}")   # Mesmo valor — compartilhado
