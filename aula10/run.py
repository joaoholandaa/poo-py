from modulos import Casa, Pessoa

casa_do_joao = Casa()
joao = Pessoa('Joao')

joao.set_local(casa_do_joao)
casa_do_joao.set_proprietario(joao)

proprietario = casa_do_joao.get_proprietario()
proprietario.se_apresentar()