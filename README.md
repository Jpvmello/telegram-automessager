# Telegram Automessager

Rotina simples para enviar mensagens aleatórias (dentro de uma lista pré-definida) em momentos aleatórios (dentro de um intervalo pré-definido) para sua conta no Telegram.

A princípio, criei essa rotina para me surpreender em momentos inesperados com mensagens de otimismo, gratidão e perseverança, eventualmente me trazendo paz em momentos difíceis e me fazendo transformar esses bons preceitos em hábito. Porém, o escopo é facilmente alterável criando-se novos arquivos como [este](message_files/otimismo.txt), com mensagens à livre escolha. Sugestões:

* Mensagens de incentivo para não procrastinar;
* Mensagens de foco;
* Mensagens para reforçar que você deve deixar algum mal comportamento.

Recomenda-se utilizá-lo em combinação com uma _smartwatch_ conectada ao celular para aumentar as chances de visualizar a mensagem no momento do recebimento.

Apesar do objetivo inicial do projeto, a rotina também pode servir para estudos gerais de como se comunicar com um _bot_ Telegram em Python, permitindo a construção de projetos mais complexos.

# Instalação

`pip install telegram_send`

# Configuração

* Crie um novo _bot_ do Telegram com o [BotFather](https://telegram.me/botfather). Salve o _token_ gerado em algum lugar seguro;
* Execute `telegram-send --configure` e entre com o _token_ gerado na etapa anterior.

# Uso

```
python telegram_notif.py [--seg-min SEG_MIN] [--seg-max SEG_MAX] arquivo_notif
```

* `SEG_MIN`: intervalo mínimo entre notificações, em segundos. Padrão: 300 (5 minutos);
* `SEG_MAX`: intervalo máximo entre notificações, em segundos. Padrão: 3600 (1 hora);
* `arquivo_notif`: caminho para o arquivo contendo a lista de possíveis notificações. Vide [exemplo](message_files/otimismo.txt).

# Executar ao inicializar o sistema

_**Nota**: a princípio disponível apenas para Windows._

É possível configurar o sistema operacional para executar o _script_ automaticamente ao inicializar. Disponibilizei este [_batch script_ de exemplo](autoinit.bat) com essa finalidade. Personalize-o com os caminhos de seu repositório local e do executável Python de seu ambiente virtual, bem como com seus parâmetros de entrada desejáveis e siga [este tutorial]() para aprender a configurar o sistema para a execução automática ao inicializar. 