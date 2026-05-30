# Padrão de Projeto — Singleton

## O que é?

O **Singleton** é um padrão de projeto criacional que garante que uma classe
possua **apenas uma instância** durante toda a execução do programa, e fornece
um ponto de acesso global a ela.

-----

## Quando usar?

|Situação                                             |Exemplo real                |
|-----------------------------------------------------|----------------------------|
|Um único objeto deve coordenar ações no sistema      |Gerenciador de configurações|
|O recurso é caro para criar e deve ser reutilizado   |Conexão com banco de dados  |
|Estado compartilhado é necessário em toda a aplicação|Logger centralizado         |

-----

## Como funciona (este código)

A implementação sobrescreve o método especial `__new__`, que é chamado **antes**
de `__init__` e é responsável por criar o objeto em memória.

```python
class Singleton:
    _instancia = None          # atributo de classe — compartilhado por todos

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)   # cria UMA VEZ
        return cls._instancia                        # sempre retorna a mesma
```

Na primeira chamada `Singleton()`:

1. `_instancia` é `None` → um objeto é criado e salvo.

Nas chamadas seguintes:

1. `_instancia` já existe → o mesmo objeto é retornado, sem criar nada novo.

-----

## Executando

```bash
python singleton.py
```

Saída esperada:

```
=== Padrão Singleton ===

Criando nova instância...
a → Singleton(id=..., valor=0)

Retornando instância existente.
b → Singleton(id=..., valor=0)

a é b? True

Após 2 incrementos em 'a':
  a.valor = 2
  b.valor = 2
```

> `a` e `b` apontam para o **mesmo objeto** — por isso alterar `a` reflete em `b`.

-----

## Estrutura do projeto

```
.
├── singleton.py   # Implementação e demonstração do padrão
└── README.md
```

-----

## Vantagens e Desvantagens

|✅ Vantagens                         |⚠️ Desvantagens                                          |
|------------------------------------|--------------------------------------------------------|
|Controle total sobre instância única|Dificulta testes unitários (estado global)              |
|Economiza memória e recursos        |Pode introduzir acoplamento excessivo                   |
|Acesso global conveniente           |Viola o Princípio de Responsabilidade Única se mal usado|

-----

## Referências

- [Refactoring Guru — Singleton](https://refactoring.guru/pt-br/design-patterns/singleton)
- Gamma et al., *Design Patterns: Elements of Reusable Object-Oriented Software* (GoF)