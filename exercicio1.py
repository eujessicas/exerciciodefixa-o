preco = float(input('digite o preço do produto: '))
percentual =float(input('Digite o percentual do desconto: '))

desconto = preco * (percentual/100)
final = preco-desconto

print(f'o preço dp produto é{preco}. Desconto de {percentual}%')
print(f'Valor calculado de desconto:{desconto}. Valor final do Produto: {final}')