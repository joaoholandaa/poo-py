from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangulo import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('João Pedro')
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(2, 3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_area(terrenoRetangular)