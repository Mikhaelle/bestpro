# SOLID

5 princípios usados em orientação a objetos que diminui acoplamento, aumentão coesão, facilita testes automatizados, refatoração, reutilização de códigos e manutenção.  É aplicável a classes e métodos e ocorre o baixo acoplamento quando os módulos tem poucas dependencias entre si, e alta coesão, quando eles são responsáveis apenas por atividades dentro de seus domínios e são bem definidas e relacionadas entre si.

## Single responsability principle
O princípio da responsabilidade unica propõe que um módulo deve ter apenas um motivo para mudar. Em outras palavras, o módulo deve ter apenas um domínio e ter responsabilidades únicas. Por exemplo, uma classe de usuário deve apenas ser responsável por criar, alterar, validar dados do usuário, enquanto outra classe é responsável por operações de dados no banco.
Está fortemente ligado ao Repository Pattern que separa a lógica de negócio(service) da persistência(repository).
Comumente utilizado em [Strategy Pattern](design_patterns/strategy.md), [Repository Pattern](design_patterns/repository.md), [Facade Pattern](design_patterns/facade.md) e [Build Pattern](design_patterns/build.md).

## Open Closed Principle

O princípio aberto-fechado descreve que um módulo deve estar fechado para modificação e aberto para extensão. Em outras palavras, deve ser possível adicionar novos comportamentos sem alterar o código existente. Isso evita a adiçao de bugs a módulos que já funcionam. 
Práticas utilizadas junto com o OCP são Inversão de dependencia e Interfaces(abstrações). 
Um exemplo para aplicação ocorre em métodos com condições que levam a diferentes operações, como diferentes descontos em data comemorativas, ou diferentes processamentos de pagamentos, facilmente identificados em vários ifs dentro de funções.
Está fortemente ligado ao Design Pattern [Strategy](design_patterns/strategy.md), [Template Method](design_patterns/template_method.md), [Decorator Pattern](design_patterns/decorator.md), [Plugin/Extension Pattern](design_patterns/plugin.md).

```Python
# abstração com interface
class Discount:
    def apply(self, price):
        return price

# implementação
class ChristmasDiscount(Discount):
    def apply(self, price):
        return price * 0.9


class BlackFridayDiscount(Discount):
    def apply(self, price):
        return price * 0.7

# uso
def calculate_price(discount, price):
    return discount.apply(price)

calculate_price(ChristmasDiscount(), 100)

#extensão
class NewYearDiscount(Discount):
    def apply(self, price):
        return price * 0.85
```
Obs: Métodos abstratos não tem implementações. No Python não existe uma palavra interface reservada como no java ou no typescrypt.
A classe Discount pode ser substituída por ABC
```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Ou pela estratégia do Duck Typing. Se as classes tem o mesmo método de implementaçao podem ser chamadas.
```Python
def process_price(discount, price):
    return discount.apply(price)

print(process_price(BlackFridayDiscount(), 100))
```

## Liskov Substitution Principle

O princípio da substituição de Liskov afirma que objetos de classes derivadas devem poder substituir objetos da classe base sem alterar o comportamento correto do programa. Comumente utilizada a injeção de dependência.
Comumente utilizado em [Strategy Pattern](design_patterns/strategy.md) e [Factory Pattern](design_patterns/factory.md).


## Interface Segregation Pinciple
O princípio afirma que interfaces devem ser específicas e não genéricas. Se uma classe usa uma interface e é formaçada a implementar todos os métodos que não utiliza então a interface está genérica demais. Nesse caso, a interface deve ser dividida em interfaces menores e mais específicas, de forma que cada classe dependa apenas dos métodos que realmente precisa.
Comumente utilizado em [Adapter Pattern](design_patterns/adapter.md), [Facade Pattern](design_patterns/facade.md) e [Strategy Pattern](design_patterns/strategy.md).

## Dependence Inversion Principle
O princípio da inversão de dependência afirma que métodos e classes devem depender de abstrações e não de implementações. O que evita a instanciação em classes e utiliza de injeção de dependência. Um módulo de Alto nível(lógica de negócio principal) não deve depender de módulo de baixo níveis e ambos devem depender de abstrações.
Comumente utilizado em [Dependency Injection](design_patterns/dependency_injection.md), [Factory Pattern](design_patterns/factory.md), [Strategy Pattern](design_patterns/strategy.md) e [Repository Pattern](design_patterns/repository.md).