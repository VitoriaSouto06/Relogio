class Relogio:
    def __init__(self,hora,minuto,segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo


    def set_hora(self,n_hora,n_minuto,n_segundo):
        self.__hora = n_hora
        self.__minuto = n_minuto
        self.__segundo = n_segundo


    def get_hora(self):

        return f'{self.__hora} {self.__minuto:} {self.__segundo}'.replace(' ',':')


    def avancar(self):
        if self.__segundo >= 59:
            self.__segundo = 00
            if self.__minuto >=59:
                self.__minuto = 00
                if self.__hora >=11:
                    self.__hora = 00
                else:
                    self.__hora = self.__hora +1

            else:
                self.__minuto = self.__minuto + 1

        elif self.__segundo < 59:
            self.__segundo = self.__segundo + 1



