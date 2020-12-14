# SmartFlower
Projeto desenvolvido para a disciplina C115 do Inatel.
Repositório responsável por acomodar uma aplicação em Python que realiza a simulação de sensores. Todos os dados são enviados através do protocolo [MQTT](https://mqtt.org/).

O projeto consiste na monitoração de solo para agricultura.

## Utilização:

A aplicação pode ser executada através do Docker, garantindo a instalação de todas as dependências necessárias, para isto:

```
  docker build -t smart_flower .
```

```
  docker run -t smart_flower
```

