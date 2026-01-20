class aluno():
    def __init__(Self,nome,nota1,nota2):
           Self.nome = nome
           Self.nota1 = nota1
           Self.nota2 = nota2
    def mediageral(self):
        return (self.nota1 + self.nota2) / 2
    def situação(self):
      if self.mediageral() >= 7:
         print(" o aluno foi aprovado ")
      elif 5 <= self.mediageral < 7:
         print(" ficará de recuperação")
      else: 
         print(" foi reprovado! " )
    def tudo(Self):
       print("nome é:", Self.nome)
       print("nota1 é:", Self.nota1)
       print("nota2 é:", Self.nota2)
       print("media foi:", (Self.mediageral))
       print("situação:", (Self.situação))
a1 = aluno("lucio", 8, 9)
a1.mediageral()
a1.situação()
a1.tudo()