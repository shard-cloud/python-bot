## O que é este template?

**Python Bot** é um boilerplate mínimo de bot do Discord em **Python**, usando
**discord.py**. Ele traz o essencial já configurado — conexão com o Discord,
sincronização de slash commands e um comando de exemplo — para você começar a
adicionar suas próprias funcionalidades sem precisar montar a estrutura do
zero.

## O que o bot faz?

- Conecta ao Discord usando um token lido do ambiente (`TOKEN`)
- Sincroniza slash commands globalmente ao iniciar
- Vem com um comando de exemplo, `/ola`, que responde "Olá mundo!"

### Fluxo básico de uso

```
Deploy do template → Bot conecta ao Discord → Slash commands sincronizados
                                                          ↓
                                    /ola → "Olá mundo!"
```

## Estrutura do projeto

```
dune/
├── main.py              ← Código principal do bot
├── requirements.txt     ← Dependências (discord.py, python-dotenv)
├── .shardcloud           ← Config de deploy da ShardCloud
└── docs/
    ├── _manifest.json
    ├── 01-intro.md       ← Esta página
    └── 02-config.md      ← Configuração
```

## Próximos passos

1. **[Configurar o bot](02-config.md)** — como obter o token do Discord e
   preparar o app para rodar
