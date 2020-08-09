from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_500,Sem_desconto

class Calcula_de_descontos:

    def calcula(self,orcamento):
        desconto = Desconto_por_cinco_itens( Desconto_por_mais_de_500(Sem_desconto).calcula(orcamento))


if __name__ == "__main__":

    from orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item("ITEM - 1", 100 ))
    orcamento.adiciona_item(Item("ITEM - 2", 50 ))
    orcamento.adiciona_item(Item("ITEM - 3", 400 ))

    calculador = Calcula_de_descontos()

    desconto= calculador.calcula(orcamento)

    print(desconto)

