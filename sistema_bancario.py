menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "d":
    while True:
      try:
          deposito = float(input('Digite o valor do depósito: '))
          if deposito <= 0:
              raise ValueError
          break
      except ValueError:
          print('Valor incorreto, digite novamente:')
    saldo = saldo + deposito
    extrato.append(('depósito',deposito))
    
  elif opcao == "s":
    while True:
      if numero_saques >= LIMITE_SAQUES:
              print('Limite de saques alcançado')
              break
      try:
          saque = float(input('Digite o valor do saque: '))
          if saque > 500:
              raise ValueError('Limite máximo de saque é R$ 500,00')
          if saque > saldo:
              raise ValueError(f'Saldo insuficiente, saldo disponível: {saldo}')
          
          break
      except ValueError as error:
        print(f'Erro: {error}. Digite novamente.')
    numero_saques += 1
    saldo = saldo - saque
    extrato.append(('saque',-saque))

  elif opcao == "e":
    print("Extrato:")
    for transacao in extrato:
      valor_formatado = '{:.2f}'.format(transacao[1])
      print(f'{transacao[0]}: R${valor_formatado}')
      saldo_formatado = '{:.2f}'.format(saldo)
    print(f"Saldo: R${saldo_formatado}")
  
  elif opcao == "q":
    break
  
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
