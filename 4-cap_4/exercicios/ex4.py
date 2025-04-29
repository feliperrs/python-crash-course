# ---------------------------------------------------------------------------- #
#!                                4.4 Um milhão                                #
# ---------------------------------------------------------------------------- #

#? Crie uma lista com números de um a um milhão e, em seguida, utilize um loop para exibi-los.
#? (Se a saída estiver demorando muito, interrompa-a pressionando CTRL+C ou fechando a janela de saída.)

one_million = list(range(1, 1_000_001))

for value in one_million:
    print(value)