## Pré-requisitos

- Uma **conta na ShardCloud**
- Um **bot do Discord** criado no [Developer Portal](https://discord.com/developers/applications)

## 1. Criar o bot no Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em **New Application** e dê um nome
3. Vá em **Bot** no menu lateral e clique em **Reset Token** para copiar o token
4. Em **OAuth2 → URL Generator**, marque `bot` e `applications.commands`
5. Selecione as permissões necessárias (Send Messages, Use Slash Commands)
6. Use a URL gerada para adicionar o bot ao seu servidor

## 2. Configurar a variável de ambiente

Este template lê o token do bot a partir da variável `TOKEN`. Ao fazer o
deploy na ShardCloud, preencha:

| Variável | Descrição                                       |
| -------- | ------------------------------------------------ |
| `TOKEN`  | Token do bot obtido no Discord Developer Portal |

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

Isso instala:

- `discord.py` — Biblioteca de interação com a API do Discord
- `python-dotenv` — Carrega variáveis de ambiente a partir de um arquivo `.env`

## 4. Rodar o bot

```bash
python main.py
```

Ao iniciar, o bot sincroniza os slash commands globalmente e fica online —
acompanhe os logs até aparecer a mensagem confirmando que está conectado.

## Arquivo `.shardcloud`

Configuração de deploy usada pela ShardCloud:

```
DISPLAY_NAME=bot de discord
MAIN=main.py
MEMORY=512
VERSION=recommended
LANGUAGE=python
```

### Parâmetros disponíveis

| Parâmetro        | Obrigatório | Descrição                                        |
| ----------------- | ----------- | ------------------------------------------------ |
| `DISPLAY_NAME`    | Sim         | Nome do app (máx. 50 caracteres)                 |
| `MAIN`            | Condicional | Arquivo principal (ignorado se `CUSTOM_COMMAND`) |
| `MEMORY`          | Sim         | RAM em MB (ex: `256`, `512`, `1024`)             |
| `VERSION`         | Sim         | `recommended` ou `latest`                        |
| `LANGUAGE`        | Não         | `node`, `python`, `java`, `go`, `static`, `php`  |
| `DESCRIPTION`     | Não         | Descrição do app (máx. 1024 caracteres)          |
| `CUSTOM_COMMAND`  | Não         | Comando customizado de inicialização             |

## Adicionando novos comandos

Novos slash commands podem ser adicionados em `main.py` seguindo o mesmo
padrão do comando `/ola`:

```python
@bot.tree.command(name="nome", description="Descrição do comando")
async def nome(interaction: discord.Interaction):
    await interaction.response.send_message("Resposta aqui")
```

Depois de adicionar ou alterar comandos, basta reiniciar o bot — a
sincronização acontece automaticamente no `setup_hook`.
