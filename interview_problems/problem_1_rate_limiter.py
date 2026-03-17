"""
PROBLEMA 1 - Rate Limiter (Sliding Window)

Testa: Estruturas de dados, algoritmos, OOP

--- CONTEXTO ---
Implemente um Rate Limiter que controla quantas requisicoes
um cliente pode fazer dentro de uma janela de tempo.

--- REQUISITOS ---
1. `is_allowed(client_id)` retorna True se permitido, False se nao.
2. Cada cliente tem seu proprio contador.
3. Requisicoes fora da janela de tempo devem ser descartadas.

--- ASSINATURA ---
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        pass

    def is_allowed(self, client_id: str) -> bool:
        pass

--- FOLLOW-UP ---

1. Como faria funcionar com multiplas instancias? (Redis)

Com varias instancias do servico, cada uma tem sua propria memoria,
entao o rate limiter in-memory nao funciona (um cliente poderia fazer
3 reqs na instancia A e mais 3 na B, ultrapassando o limite).

Solucao: usar Redis como armazenamento centralizado com Sorted Sets.
O timestamp e o score, e cada requisicao e um membro:

    ZADD rate:user_1 1710612345.5 "req-uuid-1"      # adiciona req
    ZREMRANGEBYSCORE rate:user_1 0 (now - window)    # remove expiradas
    ZCARD rate:user_1                                # conta quantas restam

Todas as instancias consultam o mesmo Redis, o limite e global.
Redis garante atomicidade com MULTI/EXEC, evitando race conditions.


2. Token Bucket vs Sliding Window: tradeoffs?

Sliding Window (o que foi implementado aqui):
  - Guarda o timestamp de cada requisicao
  - Preciso: sabe exatamente quantas reqs aconteceram na janela
  - Mais memoria: guarda N timestamps por cliente
  - Bom pra limites baixos (ex: 100 reqs/min)

Token Bucket:
  - Tem um "balde" com tokens. Cada req consome 1 token.
    Tokens sao repostos a uma taxa fixa.
  - Permite bursts: se o balde ta cheio, o cliente gasta tudo de vez
  - Menos memoria: so guarda 2 valores por cliente (tokens + ultimo refill)
  - Bom pra limites altos e quando bursts sao aceitaveis

  Exemplo:
    Token Bucket: 10 tokens, refill 1/seg
    t=0: 10 tokens -> cliente faz 10 reqs de uma vez (burst) -> 0 tokens
    t=1: 1 token disponivel

    Sliding Window: max 10 reqs em 10 seg
    t=0: cliente faz 10 reqs -> bloqueado ate t=10

Na pratica: APIs como GitHub usam token bucket. Rate limiters de
seguranca (anti-DDoS) preferem sliding window por ser mais restritivo.


3. Como aplicar Open/Closed pra trocar de estrategia?

Usar o Strategy Pattern pra aceitar diferentes algoritmos sem
alterar o codigo do RateLimiter:

    class RateLimitStrategy(ABC):
        @abstractmethod
        def is_allowed(self, client_id: str) -> bool:
            pass

    class SlidingWindowStrategy(RateLimitStrategy):
        def is_allowed(self, client_id: str) -> bool:
            # implementacao com deque...

    class TokenBucketStrategy(RateLimitStrategy):
        def is_allowed(self, client_id: str) -> bool:
            # implementacao com tokens...

    class RateLimiter:
        def __init__(self, strategy: RateLimitStrategy):
            self.strategy = strategy

        def is_allowed(self, client_id: str) -> bool:
            return self.strategy.is_allowed(client_id)

Pra adicionar uma nova estrategia (ex: FixedWindowStrategy), cria
uma nova classe sem modificar RateLimiter nem as existentes.
Isso e Open/Closed: aberto pra extensao, fechado pra modificacao.
"""

import time
from collections import deque


# --- IMPLEMENTE AQUI ---
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients_req = {}

    def is_allowed(self, client_id: str) -> bool:
        if self.max_requests == 0:
            return False
        
        if client_id in self.clients_req:
            new_client_req = self.clients_req[client_id]
            while new_client_req and time.time() - new_client_req[0] > self.window_seconds:
                new_client_req.popleft()

            new_client_req.append(time.time())
            if len(new_client_req) > self.max_requests:
                return False
            self.clients_req[client_id] = new_client_req
            return True

        else:
            self.clients_req[client_id] = deque()
            self.clients_req[client_id].append(time.time())
            return True

# --- TESTES ---
def test_basic_rate_limiting():
    limiter = RateLimiter(max_requests=3, window_seconds=1)

    assert limiter.is_allowed("user_1") is True
    assert limiter.is_allowed("user_1") is True
    assert limiter.is_allowed("user_1") is True
    assert limiter.is_allowed("user_1") is False
    print("test_basic_rate_limiting PASSED")


def test_window_expiration():
    limiter = RateLimiter(max_requests=2, window_seconds=1)

    assert limiter.is_allowed("user_1") is True
    assert limiter.is_allowed("user_1") is True
    assert limiter.is_allowed("user_1") is False

    time.sleep(1.1)

    assert limiter.is_allowed("user_1") is True
    print("test_window_expiration PASSED")


def test_independent_clients():
    limiter = RateLimiter(max_requests=2, window_seconds=1)

    assert limiter.is_allowed("user_a") is True
    assert limiter.is_allowed("user_a") is True
    assert limiter.is_allowed("user_a") is False

    assert limiter.is_allowed("user_b") is True
    print("test_independent_clients PASSED")


if __name__ == "__main__":
    test_basic_rate_limiting()
    test_window_expiration()
    test_independent_clients()
    print("\nTodos os testes passaram!")
