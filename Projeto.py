class clientes:
 def __init__(self,nome,pago,mensalidade):
   self.nome=nome
   self.pago=pago
   self.mens=mensalidade
   self.next= None
   self.previous=None
   
class listaclientes:
  def __init__(self):
    self.primeiro=None
  
  def novo_cliente(self,cliente:clientes):
    if self.primeiro is None:
      self.primeiro=cliente
      return
    
    pri=self.primeiro
    while pri.next is not None:
      pri=pri.next
      
    pri.next=cliente
  
  def pagamento(self,nome,pago):
    cliente2=self.primeiro
    if cliente2 is not None:
      while cliente2.nome!=nome:
        cliente2=cliente2.next
      cliente2.pago=pago    
    
  def remover(self,nome):
    if self.primeiro is None:
      print("Sem Clientes")
      return
    elif self.primeiro.nome==nome:
      pagou=self.primeiro
      self.primeiro=self.primeiro.next
      if self.primeiro!=None:
        self.primeiro.previous=None
      return pagou
    previous_node=self.primeiro
    current_node = self.primeiro.next
    while current_node.nome!=nome:
      previous_node=current_node
      current_node=current_node.next
    if current_node.next != None:
      previous_node.next=current_node.next
      current_node.next.previous=current_node.previous
      return current_node
    else:
      previous_node.next=None
      return current_node
      
  def mostrarlista(self):
    cliente_atual=self.primeiro
    while cliente_atual is not None:
      print(f"{cliente_atual.nome}  {cliente_atual.pago}  {cliente_atual.mens}")
      cliente_atual=cliente_atual.next
      
class main:  
  def main():
    cl=listaclientes()
    while True:
      print(" ")
      print("-"*20)
      print("Selecione uma opcao")
      print("-"*20)
      print("1. Adicinar Cliente")
      print("2. Atualizar pagamento")
      print("3. Retirar Cliente")
      print("4. Mostrar lista")
      print("5. Sair")
      print("-"*20)
      escolha=int(input("\nDigite a opcao desejada:"))
      if escolha==1:
        item1=input("\nDigite o nome do cliente a ser adcionado: ")
        item2=input(f"{item1} realizou o pagamento? ")
        item3=input(f"Valor da mensalidade que {item1} escolheu: ")
        nd=clientes(item1.title(),item2.title(),item3)
        cl.novo_cliente(nd)
      elif escolha==2:
        item1=input("Qual o nome do cliente? ")
        item2=input(f"{item1} realizou o pagemento? ")
        cl.pagamento(item1.title(),item2.title())
      elif escolha==3:
        item= input("\nDigite o cliente a ser removido:")
        removido=cl.remover(item.title())
        if removido.pago=="Nao":
          print("Cliente removido!")
          print(f"{item} precisa realizar o pagamento de R${removido.mens}")
        else:
          print("Cliente removido!")
      elif escolha==4:
        print("="*20)
        print("lista de clientes")
        print("="*20)
        cl.mostrarlista()
      elif escolha==5:
        print("\nSaindo...")
        break
      else:
        print("\nOpcao invalida, tente novamente")
        
  if __name__=='__main__':
    main()
