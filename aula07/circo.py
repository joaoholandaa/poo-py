class Circo:

  def apresentar(self, apresentador: any):
    apresentador.apresentar_show()

class Malabarista:
  
  def apresentar_show(self):
    print('Malabarista apresentando seu show')

class Palhaco:

  def apresentar_show(self):
    print('Palhaço apresentando seu show')

class Magico:
  def apresentar_show(self):
    print('Mágico apresentando seu show')

circo = Circo()
palhaco = Palhaco()
circo.apresentar(palhaco)