class Aluno ():
    def _init_(self,matricula, nome, prova1, prova2, trabalho1):
        self.matricula = matricula
        self.nome = nome
        self.prova1 = prova1 
        self.prova2 = prova2
        self.trabalho1 = trabalho1
        self.media = self.media()

    def media(self):
        return (2.5*self.prova1+2.5*self.prova2+2.0*self.trabalho1)/(7)
    def final(self):
        if self.media >= 4.0 and self.media < 7.0:
            return True
        else:
            return False


igor = Aluno(123, "igor", 2.5, 2.5, 2.0)
print(igor.final())