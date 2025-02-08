while True:
  try:
    valor_da_compra = float(input('Insira o valor da compra: '))
    discount = 0
    
    if valor_da_compra >= 500:
      discount = 0.25
    elif valor_da_compra > 100:
      base_discount = 0.05
      discount = ((valor_da_compra - 1) // 100) * 0.05 + base_discount;
      
    print(f"Desconto de {(discount * 100):.2f}% na sua compra de R${valor_da_compra:.2f}")
    print(f"Total: R${(valor_da_compra * (1 - discount)):.2f}")
    
    break
  except ValueError:
    print('Insira um número válido')
    continue