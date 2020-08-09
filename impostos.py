class ISS(object):

	def calcula(self, orcamento):

		return orcamento.valor * 0.1

class ICMS(object):

	def calcula(self, orcamento):

		return orcamento.valor * 0.06

class ICPP:
	def calcula(self,orcamento):
		if orcamento.valor  > 500:
			return orcamento.valor *0.07
		else:
			return orcamento.valor *0.05

class IKCV:
	def calcula(self,orcamento):

		if orcamento.valor >500 and  self.__tem_item_maior_que_100_reais(orcamento):
			return orcamento.valor *0.01
		else:
			return orcamento.valor*0.06

	def __tem_item_maior_que_100_reais(self,orcamento):
		for item in orcamento.obter_itens():
			if item.valor >100:
				return True
			else:
				return False
