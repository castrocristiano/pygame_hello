from pygame import Rect


class Colisao:
    ret: Rect
    x_ant: int
    y_ant: int

    def __init__(self, ret: Rect):
        self.ret = ret
        (self.x_ant, self.y_ant) = (ret.left, ret.top)

    def set_posicao_anterior(self, x: int, y: int):
        (self.x_ant, self.y_ant) = (x, y)

    def voltar_para_posicao_anterior(self):
        (self.ret.left, self.ret.top) = (self.x_ant, self.y_ant)

    def verificar_colisao(self, ret2: Rect):
        return self.ret.colliderect(ret2)

