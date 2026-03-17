"""
PROBLEMA 3 - Circuit Breaker

Testa: State machine, resiliencia, integracao de servicos, OOP

--- CONTEXTO ---
Seu servico depende de uma API externa. Quando ela fica fora,
chamadas repetidas causam timeout em cascata. Implemente um
Circuit Breaker com 3 estados:

- CLOSED: normal, requisicoes passam. Conta falhas consecutivas.
- OPEN: rejeita tudo com CircuitOpenError (fail fast).
- HALF_OPEN: apos recovery_timeout, deixa UMA chamada passar.
  Sucesso -> CLOSED. Falha -> OPEN.

--- REQUISITOS ---
1. CLOSED -> OPEN quando falhas consecutivas = failure_threshold.
2. OPEN -> HALF_OPEN apos recovery_timeout segundos.
3. HALF_OPEN -> CLOSED (sucesso) ou OPEN (falha).
4. Sucesso em CLOSED zera o contador de falhas.

--- ASSINATURA ---
class CircuitBreaker:
    def __init__(self, failure_threshold: int, recovery_timeout: float):
        pass

    def call(self, func, *args, **kwargs):
        pass

    @property
    def state(self) -> str:
        pass

--- FOLLOW-UP (discussao verbal) ---
- Como integrar com Prometheus/Datadog?
- Circuit breaker vs retry vs bulkhead: diferencas?
- Como configurar via env vars em producao?
"""

import time


class CircuitOpenError(Exception):
    pass


# --- IMPLEMENTE AQUI ---


# --- TESTES ---
def test_allows_when_closed():
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)
    result = cb.call(lambda: "ok")

    assert result == "ok"
    assert cb.state == "CLOSED"
    print("test_allows_when_closed PASSED")


def test_opens_after_threshold():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=1.0)

    def fail():
        raise ConnectionError("timeout")

    for _ in range(2):
        try:
            cb.call(fail)
        except ConnectionError:
            pass

    assert cb.state == "OPEN"
    print("test_opens_after_threshold PASSED")


def test_open_rejects_fast():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=1.0)

    def fail():
        raise ConnectionError("timeout")

    for _ in range(2):
        try:
            cb.call(fail)
        except ConnectionError:
            pass

    try:
        cb.call(lambda: "ok")
        assert False, "Deveria lancar CircuitOpenError"
    except CircuitOpenError:
        pass

    print("test_open_rejects_fast PASSED")


def test_half_open_recovers():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=1.0)

    def fail():
        raise ConnectionError("timeout")

    for _ in range(2):
        try:
            cb.call(fail)
        except ConnectionError:
            pass

    time.sleep(1.1)

    result = cb.call(lambda: "recovered")
    assert result == "recovered"
    assert cb.state == "CLOSED"
    print("test_half_open_recovers PASSED")


def test_half_open_fails_reopens():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=1.0)

    def fail():
        raise ConnectionError("timeout")

    for _ in range(2):
        try:
            cb.call(fail)
        except ConnectionError:
            pass

    time.sleep(1.1)

    try:
        cb.call(fail)
    except ConnectionError:
        pass

    assert cb.state == "OPEN"
    print("test_half_open_fails_reopens PASSED")


def test_success_resets_failures():
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)

    def fail():
        raise ConnectionError("timeout")

    try:
        cb.call(fail)
    except ConnectionError:
        pass

    cb.call(lambda: "ok")

    try:
        cb.call(fail)
    except ConnectionError:
        pass

    assert cb.state == "CLOSED"
    print("test_success_resets_failures PASSED")


if __name__ == "__main__":
    test_allows_when_closed()
    test_opens_after_threshold()
    test_open_rejects_fast()
    test_half_open_recovers()
    test_half_open_fails_reopens()
    test_success_resets_failures()
    print("\nTodos os testes passaram!")
