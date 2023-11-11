"""
CURSO: BIG DATA E INTELIGÊNCIA ANALÍTICA
ALUNO: RICARDO GUIMARÃES SANTANA
SOMATIVA 2
"""

import json
import pandas as pd


# Classe para representar um estudante
class Estudante:
    def __init__(self, codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf

    # Método para criar a tupla estudante, formato que estudante será salvo na lista.
    def escrita_estudante(self):
        """
        Método para escrever a tupla com as informações do estudante.
        :return: Tupla com as informaçõs do estudante.
        """
        estudante = (self.codigo, self.nome, self.cpf)
        return estudante


# Classe para representar um professor
class Professor:
    def __init__(self, codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf

    # Método para criar a tupla professor, formato que professor será salvo na lista.
    def escrita_prof(self):
        """
        Método para escrever a tupla com as informações do professor.
        :return: Tupla com as informaçõs do professor.
        """
        prof = (self.codigo, self.nome, self.cpf)
        return prof


# Classe para representar uma disciplina
class Disciplina:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    # Método para criar a tupla disciplina, formato que a disciplina será salvo na lista.
    def escrita_disciplina(self):
        """
        Método para escrever a tupla com as informações da disciplina.
        :return: Tupla com as informaçõs da disciplina.
        """
        disciplina = (self.codigo, self.nome)
        return disciplina


# Classe para representar uma turma
class Turma:
    def __init__(self, codigo, professor, disciplina):
        self.codigo = codigo
        self.professor = professor
        self.disciplina = disciplina

    # Método para criar a tupla turma, formato que a turma será salvo na lista.
    def escrita_turma(self):
        """
        Método para escrever a tupla com as informações da turma.
        :return: Tupla com as informaçõs da turma.
        """
        turma = (self.codigo, self.professor, self.disciplina)
        return turma


# Classe para representar uma matrícula
class Matricula:
    def __init__(self, turma, estudante):
        self.turma = turma
        self.estudante = estudante

    # Método para criar a tupla matricula, formato que a matricula será salvo na lista.
    def escrita_matricula(self):
        """
        Método para escrever a tupla com as informações da matrícula.
        :return: Tupla com as informaçõs da matrícula.
        """
        matricula = (self.turma, self.estudante)
        return matricula


# Classe para fazer o sistema funcionar
def retorna_nome(lista, codigo):
    """
    Auxilia em retornar os dados corretos nos textos exibidos para o usuário.
    :param lista: Lista que devemos procurar o nome relacionado ao código
    :param codigo: o código do cadastro que queremos o nome
    :return: o nome ou a disciplina cadastrada com o código digitado pelo usário.
    """
    for contato in lista:
        if contato[0] == codigo:
            return contato[1]


class Sistema:
    # Elementos da classe
    def __init__(self):
        self.menu_principal = {1: "ESTUDANTES", 2: "PROFESSORES", 3: "DISCIPLINAS",
                               4: "TURMAS", 5: "MATRÍCULAS", 0: "SAIR"}
        self.menu_secundario = {1: "Incluir", 2: "Listar", 3: "Atualizar", 4: "Excluir",
                                0: "Voltar ao menu principal"}
        self.nomes_arquivos = {1: "estudantes.json", 2: "professores.json",
                               3: "disciplinas.json", 4: "turmas.json", 5: "matriculas.json"}
        self.opcao_principal = -1
        self.estudantes = self.recupera_lista_json(self.nomes_arquivos[1])
        self.professores = self.recupera_lista_json(self.nomes_arquivos[2])
        self.disciplinas = self.recupera_lista_json(self.nomes_arquivos[3])
        self.turmas = self.recupera_lista_json(self.nomes_arquivos[4])
        self.matriculas = self.recupera_lista_json(self.nomes_arquivos[5])

    # Método para exibir o menu principal
    def estrutura_menu(self):
        """
        Exibe o menu pricipal ao usuário.
        :return: Exibição gráfica do menu principal.
        """
        print("===== MENU PRINCIPAL =====")
        for key, value in self.menu_principal.items():
            print(f"({key}) Gerenciar {value}.")

    # Método para exibir o menu secundário
    def __estrutura_menu_secundario(self, opcao):
        """
            Exibe o menu secundário ao usuário, utilizando o dicionário menu_secundario.
            :return: Exibição gráfica do menu secundário.
        """
        print("******* [{}] MENU DE OPERAÇÕES *******".format(self.menu_principal[opcao]))
        for key, value in self.menu_secundario.items():
            print("({}) {}".format(key, value))

    # Método para o usuário fazer a escolha no menu secundário
    def menu_secundario_escolha(self, nome_arquivo):
        """
        Cria o loop para o menu secundário
        :param nome_arquivo:
        :return: Loop para o menu secundário
        """
        while True:
            self.__estrutura_menu_secundario(self.opcao_principal)
            opcao_sec = self.obter_numero_inteiro("Digite o número da opção desejada: ")
            print("")
            if opcao_sec == 0:
                break
            self.escolha_secundaria(opcao_sec)

    # Método para verificar se o número digitado pelo usuário é um número inteiro
    @staticmethod
    def obter_numero_inteiro(mensagem):
        """
        Verifica se o valor digitado pelo usário é um número inteiro.
        :param mensagem: mensagem que solicita para o usuário digitar um número.
        :return: o número digitado.
        """
        while True:
            try:
                numero = int(input(mensagem))
                return numero
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    # Método para salvar uma lista num arquivo JSON
    def salvar_arquivo_json(self):
        """
        Salvar uma lista com novas cadastros em arquivo JSON
        :return: None
        """
        with (open(self.nomes_arquivos[self.opcao_principal], "w", encoding="utf-8")
              as arquivo):
            json.dump(self.determinar_lista(), arquivo)

    # Método para recuparar os dados salvos em um arquivo JSON
    def recupera_lista_json(self, nome):
        """
        Recupera os dados salvos em um arquivo JSON.
        :param nome: nome do arquivo JSON em que vai recuperar os dados.
        :return: lista com os dados recuperados ou lista vazia
        """
        try:
            with (open(nome, "r", encoding="utf-8") as arquivo):
                try:
                    lista = json.load(arquivo)
                    return lista
                except:
                    lista = []
                    return lista
        except FileNotFoundError:
            lista = []
            with (open(nome, "w", encoding="utf-8") as arquivo):
                json.dump(lista, arquivo)
            return lista

    # Método para verificar qual foi a escolha secundário do usuário
    def escolha_secundaria(self, opcao_secundaria):
        """
        Auxilia na escolha secundário, distribuindo a opção selecionada para a função correta.
        :param opcao_secundaria: Valor digitado pelo usuário no menu secundário
        :return: lista atualizada após a devida alteração.
        """
        if opcao_secundaria in self.menu_secundario:
            if opcao_secundaria == 1:
                self.incluir_cadastro()
                return None
            elif opcao_secundaria == 2:
                self.listar_cadastros()
                return None
            elif opcao_secundaria == 3:
                self.editar_cadastro()
                return None
            elif opcao_secundaria == 4:
                self.excluir_cadastro()
                return None
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.\n")

    # Método para incluir cadastros no sistema
    def incluir_cadastro(self):
        """
        Inclui cadastro em uma lista (estudantes, professores, etc).
        :return: retorna a lista atualizada com o novo cadastro.
        """
        if self.opcao_principal == 1 or self.opcao_principal == 2 or self.opcao_principal == 3:
            self.incluir_prof_est_disc()
        elif self.opcao_principal == 4:
            self.incluir_turmas()
        else:
            self.incluir_matriculas()
        self.salvar_arquivo_json()
        return None

    # Método para retornar a lista que deve ser utilizada.
    def determinar_lista(self):
        if self.opcao_principal == 1:
            return self.estudantes
        elif self.opcao_principal == 2:
            return self.professores
        elif self.opcao_principal == 3:
            return self.disciplinas
        elif self.opcao_principal == 4:
            return self.turmas
        else:
            return self.matriculas

    # Método para verificar se um código já está salvo no sistema
    def verificar_codigo(self, mensagem):
        """
        Verifica se um código digitado pelo usário está cadastrado no sistema.
        :param mensagem: mensagem que o usuário deve receber para digitar o código
        :return: código
        """
        while True:
            codigo = self.obter_numero_inteiro(mensagem)
            codigo_existente = False
            for cadastro in self.determinar_lista():
                if cadastro[0] == codigo:
                    print("Código já cadastrado. Favor insira um novo código.\n")
                    codigo_existente = True
                    break
            if not codigo_existente:
                return codigo

    # Método para verificar se o CPF é valor (apenas considerando a quantidade de dígitos)
    @staticmethod
    def cpf_valido(mensagem):
        while True:
            cpf = input(mensagem)
            if len(cpf) == 11:
                return cpf
            else:
                print("CPF inválido! Verifique a quantidade de dígitos.")
    # Método para auxiliar na inclusão de professores, estudantes e disciplinas
    def incluir_prof_est_disc(self):
        """
        Método para auxiliar na inclusão de cadastros de professores, estudante e disciplinas
        :return: None
        """
        cod = self.verificar_codigo("Informe o código: ")
        name = str(input("Informe o nome que deve ser cadastrado: "))
        if self.opcao_principal == 1 or self.opcao_principal == 2:
            documento = self.cpf_valido("Informe o CPF que deve ser cadastrado: ")
            if self.opcao_principal == 1:
                estudante = Estudante(cod, name, documento)
                self.estudantes.append(estudante.escrita_estudante())
                input("\nCadastro realizado. Pressione ENTER para continuar.\n")
                return None
            elif self.opcao_principal == 2:
                professor = Professor(cod, name, documento)
                self.professores.append(professor.escrita_prof())
                input("\nCadastro realizado. Pressione ENTER para continuar.\n")
                return None
        else:
            disciplina = Disciplina(cod, name)
            self.disciplinas.append(disciplina.escrita_disciplina())
            input("\nCadastro realizado. Pressione ENTER para continuar.\n")
            return None

    # Método para auxiliar na inclusão de turmas
    def incluir_turmas(self):
        """
        Método utilizado para auxiliar na inclusão de novas turmas ao sistema.
        :return: None
        """
        if len(self.professores) == 0 or len(self.disciplinas) == 0:
            print("Erro, não existem cadastros de professores e\ou disciplinas.")
            input("\nPressione ENTER para continuar.\n")
            return None
        cod = self.verificar_codigo("Informe o código da turma: ")

        cod_professor = self.verificar_existencia_codigo("Informe o código do "
                                                         "professor responsável: ", self.professores)
        cod_disciplina = self.verificar_existencia_codigo("Informe o código da "
                                                          "disciplina: ", self.disciplinas)
        turma = Turma(cod, cod_professor, cod_disciplina)
        self.turmas.append(turma.escrita_turma())
        input("\nCadastro realizado. Pressione ENTER para continuar.\n")
        return None

    # Método para auxiliar na inclusão de matrículas
    def incluir_matriculas(self):
        """
        Método para auxiliar na inclusão de novas matrículas.
        :return: None
        """
        if len(self.turmas) == 0 or len(self.estudantes) == 0:
            print("Erro, não existem cadastros de alunos e\ou turmas cadastradas.")
            input("\nPressione ENTER para continuar.\n")
            return None
        cod_turma = self.verificar_existencia_codigo("Informe o código da turma: ",
                                                     self.turmas)
        cod_estudante = self.verificar_existencia_codigo("Informe o código do "
                                                         "estudante: ", self.estudantes)
        matricula = Matricula(cod_turma, cod_estudante)
        for cadastro in self.matriculas:
            if cadastro == matricula.escrita_matricula():
                input("\nEstudante já está matriculado nessa turma. Pressione ENTER.\n")
                return None
        self.matriculas.append(matricula.escrita_matricula())
        input("\nCadastro realizado. Pressione ENTER para continuar.\n")
        return None

    # Método para listar cadastrados de uma lista e verificar o código
    def verificar_existencia_codigo(self, mensagem, lista):
        """
        Lista os cadastros de uma lista, para facilitar o usuário de lembrar os código
        já cadastrados
        e retorna o código escolhido pelo usuário;
        :param mensagem: texto que deve explicar ao usuário o que deve digitar
        :param lista: Lista com os cadastros que deve-se verificar o código.
        :return: Mensagem de cadastro inválido ou o código digitado.
        """
        if lista == self.professores:
            print("Selecione um(a) dos(as) professores cadastrados(as) no sistema:\n")
            tabela = pd.DataFrame(lista, columns=["CÓDIGO", "NOME", "CPF"]).to_string(index=False)
            print(tabela)
        elif lista == self.disciplinas:
            print("Selecione uma das disciplinas cadastradas no sistema:\n")
            tabela = pd.DataFrame(lista, columns=["CÓDIGO", "NOME"]).to_string(index=False)
            print(tabela)
        elif lista == self.estudantes:
            print("Selecione um(a) dos(as) estudantes cadastrados(as) no sistema:\n")
            tabela = pd.DataFrame(lista, columns=["CÓDIGO", "NOME", "CPF"]).to_string(index=False)
            print(tabela)
        elif lista == self.turmas:
            self.listar_turmas()
        while True:
            codigo = self.obter_numero_inteiro(mensagem)
            for cadastro in lista:
                if cadastro[0] == codigo:
                    return codigo
            print("Código não cadastrado. Insira um código válido.\n")

    # Método para listar os professores e estudantes
    def listar_prof_est(self):
        """
        Cria tabela com as informações dos professores ou estudantes cadastrados.
        :return: None
        """
        if len(self.determinar_lista()) == 0:
            print("SEM CADASTRO")
            return None
        else:
            print("CADASTROS REALIZADOS:")
            tabela = pd.DataFrame(self.determinar_lista(), columns=["CÓDIGO", "NOME", "CPF"]).to_string(index=False)
            print(tabela)
        input("Pressione ENTRER para continuar.\n")
        return None

    # Método para auxiliar na listagem das disciplinas
    def listar_disciplinas(self):
        """
        Cria uma tabela com as disciplinas cadastradas.
        :return: None
        """
        if len(self.determinar_lista()) == 0:
            print("SEM CADASTRO")
        else:
            print("DISCIPLINAS CADASTRADAS NO SISTEMA:")
            tabela = pd.DataFrame(self.determinar_lista(), columns=["CÓDIGO", "DISCIPLINA", ]).to_string(index=False)
            print(tabela)
        input("Pressione ENTRER para continuar.\n")

    # Método para verificar se um código já existe no sistema.
    @staticmethod
    def retorna_codigo(lista, codigo):
        """
        Método para auxiliar nos textos exibidos para o usuário, mostrando o código de um
        determinado cadastro.
        :param lista: Lista em que se deve verificar o código.
        :param codigo: o código que deve ser verificado a existência
        :return: código se for existente
        """
        for contato in lista:
            if codigo == contato[0]:
                return contato[0]

    # Método para auxiliar na listagem turmas cadastradas
    def listar_turmas(self):
        """
        Método para criar uma tabela com as turmas cadastradas no sistema.
        :return: None
        """
        lista_aux = []  # Lista para criar a tabela, com nomes dos professores e disciplinas
        for cadastro in self.turmas:
            cadastro_aux = (cadastro[0], retorna_nome(self.professores, cadastro[1]),
                            retorna_nome(self.disciplinas, cadastro[2]))
            lista_aux.append(cadastro_aux)
        if len(lista_aux) == 0:
            print("SEM CADASTRO")
            return None
        else:
            print("TURMAS CADASTRADAS NO SISTEMA:")
            tabela = pd.DataFrame(lista_aux, columns=["CÓDIGO", "PROFESSOR", "DISCIPLINA"]).to_string(index=False)
            print(tabela)
        input("Pressione ENTRER para continuar.\n")
        return None

    # Método para auxiliar na listagem das matrículas de uma turma
    def listar_matriculas(self):
        """
        Método para criar tabela os nomes e códigos dos estudantes matriculados em uma turma
        :return: None
        """
        print("TURMAS CADASTRADADAS")
        self.listar_turmas()
        cod_turma = self.obter_numero_inteiro("Escolha o código da turma que deseja listar os "
                                              "matriculados: ")
        print("\nESTUDANTES MATRICULADOS NA TURMA:")
        lista_aux = []  # Lista para criar tabela
        for cadastro in self.determinar_lista():
            if cod_turma == cadastro[0]:
                cadastro_aux = (self.retorna_codigo(self.estudantes, cadastro[1]), retorna_nome(self.estudantes,
                                                                                                cadastro[1]))
                lista_aux.append(cadastro_aux)
        if len(lista_aux) == 0:
            print("\n\t\t\tTurma sem estudantes matriculados.\n")
            return None
        else:
            tabela = pd.DataFrame(lista_aux, columns=["CÓDIGO", "NOME"]).to_string(index=False)
            print(tabela)
        input("Pressione ENTRER para continuar.\n")
        return None

    # Método para listar cadastrados
    def listar_cadastros(self):
        """
        Lista os cadastros contidos numa lista.
        :return: None
        """
        if self.opcao_principal == 1 or self.opcao_principal == 2:
            self.listar_prof_est()
            return None
        elif self.opcao_principal == 3:
            self.listar_disciplinas()
            return None
        elif self.opcao_principal == 4:
            self.listar_turmas()
            return None
        else:
            self.listar_matriculas()
            return None

    # Método para auxiliar na edição de matrículas
    def editar_matriculas(self, cod):
        """
         Método para editar matrículas de uma turma, transfere o estudante de uma turma para a outra
        :param cod: Código da matrícula que deve ser atualizada.
        :returns: Tupla com cadastro atualizado, cadastro antigo e valor boleano.
        """
        for cadastro in self.matriculas:
            if cadastro[1] == cod:
                confirmacao = input(f"Deseja editar a matricula do(a) estudante: "
                                    f"{retorna_nome(self.estudantes, cadastro[1])}? (s/n) ")
                if confirmacao.lower() == "s":
                    confirmacao = input(f"Estudante matriculado na turma de "
                                        f"{retorna_nome(self.disciplinas, cadastro[0])}, deseja alterar? (s/n) ")
                    if confirmacao.lower() == "s":
                        codigo = self.verificar_existencia_codigo("Informe o código da nova turma do "
                                                                  "estudante: ", self.turmas)
                else:
                    print("Erro ao atualizar")
                    return cadastro, cadastro, False
                cadastro_atualizado = (codigo, cadastro[1])
                return cadastro_atualizado, cadastro, True
        print("Código não cadastrado. \n")
        return None, None, False

    # Método para auxiliar para editar turmas cadastradas no sistema
    def editar_turmas(self, cod):
        """
        Edita as turmas cadastradas no sistema.
        :param cod: Código da turma que deve ser editada.
        :returns: Tupla com cadastro atualizado, cadastro antigo e valor boleano.
        """
        for cadastro in self.turmas:
            if cod == cadastro[0]:
                print("DADOS DA TURMA SELECIONADA:")
                print("CÓDIGO: {}".format(cadastro[0]))
                print("PROFESSOR: {}".format(retorna_nome(self.professores, cadastro[1])))
                print("DISCIPLINA: {}".format(retorna_nome(self.disciplinas, cadastro[2])))
                confirmacao = input(f"Deseja editar o cadastro selecionado? (s/n) ")
                if confirmacao.lower() == "s":
                    confirmacao = input(f"Deseja alterar o código da turma? (s/n) ")
                    if confirmacao.lower() == "s":
                        codigo = self.verificar_codigo("Digite o novo código: ")
                    else:
                        codigo = cadastro[0]
                    confirmacao = input(f"Deseja alterar o professor responsável pela turma? (s/n) ")
                    if confirmacao.lower() == "s":
                        cod_prof = self.verificar_existencia_codigo("Digite o código do novo professor: ",
                                                                    self.professores)
                    else:
                        cod_prof = cadastro[1]
                    confirmacao = input(f"Deseja alterar a disciplina cadastrada? (s/n) ")
                    if confirmacao.lower() == "s":
                        cod_disc = self.verificar_existencia_codigo("Digite o código da nova disciplina: ",
                                                                    self.disciplinas)
                    else:
                        cod_disc = cadastro[2]
                    cadastro_atualizado = (codigo, cod_prof, cod_disc)
                    return cadastro_atualizado, cadastro, True
                else:
                    print("Erro ao atualizar. Por favor, tente novamente.\n")
                    return None, None, False
        print("Código não cadastrado. \n")
        return None, None, False

    # Método para auxiliar na edição de professores, estudantes e disciplinas
    def editar_prof_est_disc(self, cod):
        """
        Métidi para auxiliar na edição do cadastro de professores, estudantes e disciplinas cadastradas.
        :param cod: Código do cadastro que deve ser atualizado
        :returns: Nova cadastro atualizado, cadastro que deve ser excluido e teste para a função principal
                    saber se deve atualizar a lista ou não.
        """
        for cadastro in self.determinar_lista():
            if cod == cadastro[0]:
                print("DADOS DO CADASTRO SELECIONADO:")
                print("CÓDIGO: {}".format(cadastro[0]))
                print("NOME: {}".format(cadastro[1]))
                if len(cadastro) == 3:
                    print("CPF: {}".format(cadastro[2]))
                confirmacao = input(f"Deseja editar o cadastro? (s/n) ")
                if confirmacao.lower() == "s":
                    confirmacao = input(f"O código cadastrado é {cadastro[0]}, deseja alterar? (s/n) ")
                    if confirmacao.lower() == "s":
                        codigo = self.verificar_codigo("Digite o novo código: ")
                    else:
                        codigo = cadastro[0]
                    confirmacao = input(f"O nome cadastrado é: {cadastro[1]}, deseja editar o nome cadastrado? (s/n) ")
                    if confirmacao.lower() == "s":
                        nome = input("Digite o novo nome: ")
                    else:
                        nome = cadastro[1]
                    if self.opcao_principal == 1 or self.opcao_principal == 2:
                        confirmacao = input(f"O CPF cadastrado é: {cadastro[2]} Deseja editar o CPF cadastrado? (s/n) ")
                        if confirmacao.lower() == "s":
                            cpf = self.cpf_valido("Digite o CPF nome: ")
                        else:
                            cpf = cadastro[2]
                        cadastro_atualizado = (codigo, nome, cpf)
                        return cadastro_atualizado, cadastro, True
                    else:
                        cadastro_atualizado = (codigo, nome)
                        return cadastro_atualizado, cadastro, True
                else:
                    print("Erro ao atualizar. Por favor, tente novamente.\n")
                    return None, None, False
        print("Código não cadastrado. \n")
        return None, None, False

    # Método para editar estudantes e professores cadastrados
    def editar_cadastro(self):
        """
        Edita um cadastro realizada numa determinada lista.
        :return: Lista com o cadastro atualizado.
        """
        if self.opcao_principal == 5 and len(self.matriculas):
            self.listar_matriculas()
            cod = self.obter_numero_inteiro("Digite o código do cadastro que deseja alterar: ")
            cadastro_atualizado, cadastro, teste = self.editar_matriculas(cod)
        elif self.opcao_principal == 4 and len(self.turmas) != 0:
            self.listar_turmas()
            cod = self.obter_numero_inteiro("Digite o código da turma que deseja alterar: ")
            cadastro_atualizado, cadastro, teste = self.editar_turmas(cod)
        elif self.opcao_principal == 3 and len(self.disciplinas) != 0:
            self.listar_disciplinas()
            cod = self.obter_numero_inteiro("Digite o código da disciplina deseja alterar: ")
            cadastro_atualizado, cadastro, teste = self.editar_prof_est_disc(cod)
        elif self.opcao_principal == 2 and len(self.professores) != 0:
            self.listar_prof_est()
            cod = self.obter_numero_inteiro("Digite o código do professor deseja alterar: ")
            cadastro_atualizado, cadastro, teste = self.editar_prof_est_disc(cod)
        elif self.opcao_principal == 1 and len(self.estudantes) != 0:
            self.listar_prof_est()
            cod = self.obter_numero_inteiro("Digite o código do estudante que deseja alterar: ")
            cadastro_atualizado, cadastro, teste = self.editar_prof_est_disc(cod)
        else:
            input("SEM CADASTROS NO SISTEMA\nPRESSIONE ENTRER.\n")
            return None
        if teste:
            self.determinar_lista().remove(cadastro)
            self.determinar_lista().append(cadastro_atualizado)
            self.salvar_arquivo_json()
            print("Atualizado com sucesso.\n")
            return None
        else:
            return None

    # Método para excluir uma turma do sistema
    def excluir_turmas(self, cod):
        """
        Método para auxiliar na exclusão de turmas cadastradas no sistema
        :param cod: Código da turma que deve ser exlcluida.
        :return: None
        """
        for cadastro in self.turmas:
            if cod == cadastro[0]:
                if input(f"Deseja excluir a turma de {retorna_nome(self.turmas, cadastro[2])}, do professor(a) "
                         f"{retorna_nome(self.professores, cadastro[1])}? (s/n) ").lower() == "s":
                    self.turmas.remove(cadastro)
                    self.salvar_arquivo_json()
                    input("\nCadastro removido com sucesso. Pressione ENTER para continuar.\n")
                    return None
                else:
                    input("\nFalha ao excluir cadastro. Pressione ENTER para continuar.\n")
                    return None

    # Método para auxiliar na exclusão de matrículas
    def exluir_matriculas(self, cod):
        """
        Método para auxiliar na exclusão de estudantes matriculados em alguma turma.
        :param cod: Código do aluno que deve ser excluido
        :return: None
        """
        for estudante in self.matriculas:
            if cod == estudante[1]:
                self.matriculas.remove(estudante)
                input("\nCadastro removido com sucesso. Pressione ENTER para continuar.\n")
                self.salvar_arquivo_json()
                return None
        input("\nFalha ao excluir cadastro. Pressione ENTER para continuar.\n")
        return None

    # Método para auxiliar na exclusão de estudante, professores e disciplinas
    def excluir_prof_est_disc(self, cod):
        """
        Método para auxiliar na exclusão de professores, estudantes e disciplinas.
        :param cod: Código do cadastro que deve ser excluido
        :return: None
        """
        for cadastro in self.determinar_lista():
            if cod == cadastro[0]:
                if input(f"Deseja excluir {cadastro[1]}? (s/n) ").lower() == "s":
                    self.determinar_lista().remove(cadastro)
                    input("\nCadastro removido com sucesso. Pressione ENTER para continuar.\n")
                    self.salvar_arquivo_json()
                    return None
                else:
                    input("\nFalha ao excluir cadastro. Pressione ENTER para continuar.\n")
                    return None

    # Método para excluir estudantes, professores e disciplinas cadastradas
    def excluir_cadastro(self):
        """
        Exclui um cadastro numa lista.
        :return: None
        """
        if self.opcao_principal == 4 and len(self.turmas) != 0:
            self.listar_turmas()
            cod = self.obter_numero_inteiro("Informe o código da turma que deve ser excluida: ")
            self.excluir_turmas(cod)
            return None
        elif self.opcao_principal == 5 and len(self.matriculas) != 0:
            self.listar_matriculas()
            cod = self.obter_numero_inteiro("Informe o código do estudante que deve ser excluido(a): ")
            self.exluir_matriculas(cod)
            return None
        elif self.opcao_principal == 1 or self.opcao_principal == 2 or self.opcao_principal == 3:
            if len(self.determinar_lista()) == 0:
                input("SEM CADASTROS! PRESSIONE ENTER.")
                return None
            else:
                self.listar_cadastros()
                cod = self.obter_numero_inteiro("Informe o código do cadastro que deve ser excluido(a): ")
                self.excluir_prof_est_disc(cod)
                return None
        else:
            input("SEM CADASTROS! \nPRESSIONE ENTER.\n")
            return None