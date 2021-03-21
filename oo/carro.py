class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE="Norte"
SUL="Sul"
LESTE="Leste"
OESTE="Oeste"

class Direcao:
# o código DO IF ABAIXO foi substituido pelo dicionário
    rotacao_a_direita_dict = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
#
    rotacao_a_esquerda_dict = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]

# código do IF ABAIXO
#    def girar_a_direita(self):
#        if self.valor == NORTE
#            self.valor = LESTE
#        elif self.valor == LESTE
#            self.valor = SUL
#        elif self.valor == SUL
#            self.valor = OESTE
#        elif self.valor == OESTE
#            self.valor = NORTE



