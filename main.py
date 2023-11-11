'''
CURSO: BIG DATA E INTELIGÊNCIA ANALÍTICA
ALUNO: RICARDO GUIMARÃES SANTANA
SOMATIVA 2
'''
import Sistema as sis

# Início do programa
menu = sis.Sistema()
while True:
    menu.estrutura_menu()
    menu.opcao_principal = menu.obter_numero_inteiro("Digite o número da opção desejada: ")
    print("")
    if menu.opcao_principal in menu.menu_principal:
        if menu.opcao_principal == 0:
            print("Saindo da aplicação.")
            break
        elif menu.opcao_principal == 1:
            menu.menu_secundario_escolha(menu.nomes_arquivos[menu.opcao_principal])
        elif menu.opcao_principal == 2:
            menu.menu_secundario_escolha(menu.nomes_arquivos[menu.opcao_principal])
        elif menu.opcao_principal == 3:
            menu.menu_secundario_escolha(menu.nomes_arquivos[menu.opcao_principal])
        elif menu.opcao_principal == 4:
            menu.menu_secundario_escolha(menu.nomes_arquivos[menu.opcao_principal])
        elif menu.opcao_principal == 5:
            menu.menu_secundario_escolha(menu.nomes_arquivos[menu.opcao_principal])
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")