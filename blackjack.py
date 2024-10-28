import random

def criar_mazo():
  naipes = ['♥', '♦', '♣', '♠']
  valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  return [(valor, naipe) for valor in valores for naipe in naipes]

def valor_carta(carta):
  if carta[0] in ['J', 'Q', 'K']:
    return 10
  elif carta [0] == 'A':
    return 11
  else:
    return int(carta[0])

def calcular_pontuacao(mao):
  total = sum(valor_carta(carta) for carta in mao)
  aces = sum(1 for carta in mao if carta[0] == 'A')
  while total > 21 and aces:
    total -= 10
    aces -= 1
  return total

def jogar_blackjack():
  mazo = criar_mazo()
  random.shuffle(mazo)

  jogador = [mazo.pop(), mazo.pop()]
  dealer = [mazo.pop(), mazo.pop()]

  print(f"Mão do Jogador: {jogador} | Pontuação {calcular_pontuacao(jogador)}")
  print(f"Mão do Dealer: [{dealer[0]}, ?]")

      # Turno do jogador
    while True:
        escolha = input("Deseja 'HIT' para pegar outra carta ou 'STAND' para manter a mão? ").upper()
        if escolha == 'HIT':
            jogador.append(mazo.pop())
            pontuacao_jogador = calcular_pontuacao(jogador)
            print(f"Mão do Jogador: {jogador} | Pontuação {pontuacao_jogador}")
            if pontuacao_jogador > 21:
                print("Você estourou! Dealer venceu.")
                return
        elif escolha == 'STAND':
            break
        else:
            print("Escolha inválida. Digite 'HIT' ou 'STAND'.")

    # Turno do dealer
    print(f"Mão do Dealer: {dealer} | Pontuação {calcular_pontuacao(dealer)}")
    while calcular_pontuacao(dealer) < 17:
        dealer.append(mazo.pop())
        print(f"Mão do Dealer: {dealer} | Pontuação {calcular_pontuacao(dealer)}")
        if calcular_pontuacao(dealer) > 21:
            print("Dealer estourou! Você venceu.")
            return

    # Comparação final
    pontuacao_jogador = calcular_pontuacao(jogador)
    pontuacao_dealer = calcular_pontuacao(dealer)
    print(f"Pontuação Final - Jogador: {pontuacao_jogador} | Dealer: {pontuacao_dealer}")
    if pontuacao_jogador > pontuacao_dealer:
        print("Você venceu!")
    elif pontuacao_jogador < pontuacao_dealer:
        print("Dealer venceu!")
    else:
        print("Empate!")

# Iniciar o jogo
jogar_blackjack()
