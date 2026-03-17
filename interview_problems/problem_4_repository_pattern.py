"""
PROBLEMA 4 - Subscription Service com Repository Pattern

Testa: DDD basico, Clean Architecture, inversao de dependencia, regras de negocio

--- CONTEXTO ---
Modele um servico de assinaturas com estas regras de negocio:
1. Usuario so pode ter UMA assinatura ativa por vez.
2. Status possiveis: ACTIVE, CANCELLED, EXPIRED.
3. Preco nao pode ser negativo.
4. Assinatura expirada (end_date no passado) nao conta como ativa.

--- REQUISITOS ---
1. Classe Subscription com as regras de negocio.
2. Classe InMemoryRepository para persistencia fake.
3. Classe SubscriptionService que usa o repository (injecao de dependencia).

--- ASSINATURAS ---
class Subscription:
    def __init__(self, user_id: str, plan: str, price: float,
                 duration_days: int):
        pass

    def cancel(self) -> None:
        pass

    def is_active(self) -> bool:
        pass

class SubscriptionService:
    def __init__(self, repository):
        pass

    def create(self, user_id, plan, price, duration_days) -> Subscription:
        pass

    def cancel(self, subscription_id: str) -> None:
        pass

--- FOLLOW-UP (discussao verbal) ---
- Como migrar o InMemory pra SQLAlchemy sem mudar o Service?
- Como adicionar evento de dominio (SubscriptionCancelled)?
- Aggregate root vs entity nesse contexto?
"""

from datetime import datetime, timedelta
import uuid


class DomainError(Exception):
    pass


# --- IMPLEMENTE AQUI ---


# --- TESTES ---
def test_create_subscription():
    repo = InMemoryRepository()
    service = SubscriptionService(repo)

    sub = service.create("user_1", "premium", 29.90, 30)

    assert sub.status == "ACTIVE"
    assert sub.is_active() is True
    print("test_create_subscription PASSED")


def test_no_duplicate_active():
    repo = InMemoryRepository()
    service = SubscriptionService(repo)

    service.create("user_1", "basic", 9.90, 30)

    try:
        service.create("user_1", "premium", 29.90, 30)
        assert False, "Deveria lancar DomainError"
    except DomainError:
        pass

    print("test_no_duplicate_active PASSED")


def test_cancel():
    repo = InMemoryRepository()
    service = SubscriptionService(repo)

    sub = service.create("user_1", "premium", 29.90, 30)
    service.cancel(sub.id)

    assert sub.status == "CANCELLED"
    print("test_cancel PASSED")


def test_expired_not_active():
    sub = Subscription("user_1", "basic", 9.90, 0)
    sub.start_date = datetime.now() - timedelta(days=10)
    sub.end_date = datetime.now() - timedelta(days=1)

    assert sub.is_active() is False
    print("test_expired_not_active PASSED")


def test_negative_price_rejected():
    repo = InMemoryRepository()
    service = SubscriptionService(repo)

    try:
        service.create("user_1", "premium", -10.0, 30)
        assert False, "Deveria lancar DomainError"
    except DomainError:
        pass

    print("test_negative_price_rejected PASSED")


if __name__ == "__main__":
    test_create_subscription()
    test_no_duplicate_active()
    test_cancel()
    test_expired_not_active()
    test_negative_price_rejected()
    print("\nTodos os testes passaram!")
