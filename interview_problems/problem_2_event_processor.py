"""
PROBLEMA 2 - Event Bus simples

Testa: Observer pattern, OOP, tratamento de erros, SOLID

--- CONTEXTO ---
Implemente um EventBus onde handlers se inscrevem para tipos
de eventos. Ao publicar um evento, todos os handlers inscritos
sao executados. Se um handler falhar, os demais continuam.

--- REQUISITOS ---
1. `subscribe(event_type, handler_fn)` registra uma funcao.
2. `publish(event_type, data)` executa todos os handlers do tipo.
3. Se um handler lancar excecao, os outros devem continuar.
4. `publish` retorna dict com contagem de sucessos e falhas.

--- ASSINATURA ---
class EventBus:
    def __init__(self):
        pass

    def subscribe(self, event_type: str, handler) -> None:
        pass

    def publish(self, event_type: str, data: dict) -> dict:
        '''Retorna {"successes": int, "failures": int}'''
        pass

--- FOLLOW-UP ---

1. Como garantir ordem de eventos em sistema distribuido?

O problema: com multiplas instancias consumindo eventos de uma fila,
a ordem de processamento nao e garantida. Ex: "order.paid" pode ser
processado antes de "order.created".

Solucoes:
- Partition key: ferramentas como Kafka permitem definir uma chave
  (ex: order_id). Todos os eventos da mesma chave vao pra mesma
  particao, que e consumida por um unico consumer, garantindo ordem.
- Sequence number: cada evento carrega um numero sequencial.
  O consumer so processa o evento N+1 depois de processar o N.
- Single writer: uma unica instancia escreve eventos de um
  agregado, garantindo ordem na origem.


2. Retry com backoff exponencial: como implementar?

Quando um handler falha, ao inves de desistir, tenta novamente
com intervalos crescentes:

    tentativa 1: espera 1s
    tentativa 2: espera 2s
    tentativa 3: espera 4s
    tentativa 4: espera 8s  (2 ** tentativa)

    import time

    def retry_with_backoff(func, data, max_retries=3):
        for attempt in range(max_retries):
            try:
                return func(data)
            except Exception:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)

Adicionar jitter (tempo aleatorio) evita que todos os retries
acontecam ao mesmo tempo (thundering herd problem).


3. Dead letter queue: quando usar?

DLQ e uma fila separada onde vao os eventos que falharam apos
todas as tentativas de retry. Serve pra:

- Nao perder eventos: ao inves de descartar, guarda pra analise
- Debugging: permite inspecionar o que deu errado
- Reprocessamento: apos corrigir o bug, reprocessa os eventos da DLQ

Quando usar:
- Eventos criticos que nao podem ser perdidos (pagamentos, pedidos)
- Quando o sistema precisa de auditoria
- Integracao com servicos externos instáveis

Quando NAO usar:
- Eventos descartaveis (metricas, logs de analytics)
- Sistemas onde perder um evento nao causa impacto


4. Event sourcing vs event-driven: diferenca?

Event-driven (o que implementamos aqui):
- Eventos sao notificacoes: "algo aconteceu, reaja"
- O estado atual fica no banco de dados
- Eventos podem ser descartados apos consumo
- Exemplo: publish("order.created") -> handler atualiza estoque

Event sourcing:
- Eventos SAO o banco de dados. O estado e reconstruido
  reprocessando todos os eventos desde o inicio.
- Nunca deleta eventos, sao imutaveis (append-only log)
- Permite reconstruir o estado em qualquer ponto no tempo
- Exemplo: saldo da conta = soma de todos os eventos de
  credito e debito desde a criacao

  eventos = [
      {"type": "deposito", "valor": 100},    # saldo: 100
      {"type": "saque", "valor": 30},         # saldo: 70
      {"type": "deposito", "valor": 50},      # saldo: 120
  ]

Event sourcing e mais complexo mas da auditoria total e
possibilidade de "voltar no tempo". Event-driven e mais
simples e resolve a maioria dos casos.
"""


# --- IMPLEMENTE AQUI ---

class EventBus:
    def __init__(self):
        self.events = {}

    def subscribe(self, event_type: str, handler) -> None:
        if event_type in self.events:
            self.events[event_type].append(handler)
        else:
            self.events[event_type] = [handler]

    def publish(self, event_type: str, data: dict) -> dict:
        report = {"successes":0,"failures":0}
        if len(self.events):
            handlers = self.events[event_type]
            for i, func in  enumerate(handlers):
                try:
                    func(data)
                    report['successes'] += 1
                except:
                    report['failures'] += 1
                    print("Erro ao executar. Continue ...")
        return report
        


# --- TESTES ---
def test_basic_subscribe_publish():
    bus = EventBus()
    results = []
    # recebo o tipo de evento e a função a ser executada
    bus.subscribe("order.created", lambda data: results.append(data))
    # recebo qual evento publicar e dispara as funçoes com os dados passados
    bus.publish("order.created", {"order_id": "1"})

    assert results == [{"order_id": "1"}]
    print("test_basic_subscribe_publish PASSED")


def test_multiple_handlers():
    bus = EventBus()
    log_a, log_b = [], []

    bus.subscribe("order.created", lambda d: log_a.append(d))
    bus.subscribe("order.created", lambda d: log_b.append(d))

    bus.publish("order.created", {"order_id": "1"})

    assert len(log_a) == 1
    assert len(log_b) == 1
    print("test_multiple_handlers PASSED")


def test_failure_doesnt_block_others():
    bus = EventBus()
    results = []

    def failing_handler(data):
        raise RuntimeError("boom")
    #tratamento de erro
    bus.subscribe("order.created", failing_handler)
    bus.subscribe("order.created", lambda d: results.append(d))

    report = bus.publish("order.created", {"order_id": "1"})

    assert len(results) == 1
    assert report["successes"] == 1
    assert report["failures"] == 1
    print("test_failure_doesnt_block_others PASSED")


def test_no_handlers():
    bus = EventBus()
    report = bus.publish("nothing", {})

    assert report["successes"] == 0
    assert report["failures"] == 0
    print("test_no_handlers PASSED")


if __name__ == "__main__":
    test_basic_subscribe_publish()
    test_multiple_handlers()
    test_failure_doesnt_block_others()
    test_no_handlers()
    print("\nTodos os testes passaram!")
