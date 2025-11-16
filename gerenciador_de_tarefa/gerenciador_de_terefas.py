# ===========================
# GERENCIAMENTO DE TAREFAS
# Sistema pronto para GitHub
# ===========================

import json
import os
import datetime

# -------------------- VARIÁVEIS GLOBAIS -------------------- #

LISTA_TAREFAS = []
LISTA_ARQUIVADAS = []
PROXIMO_ID_TAREFA = 1

ARQ_TAREFAS = "tarefas.json"
ARQ_ARQUIVADAS = "tarefas_arquivadas.json"

OPCOES_PRIORIDADE = ["Urgente", "Alta", "Média", "Baixa"]
OPCOES_STATUS = ["Pendente", "Fazendo", "Concluída", "Arquivado", "Excluída"]
OPCOES_ORIGEM = ["E-mail", "Telefone", "Chamado do Sistema"]

TAREFA_EM_EXECUCAO = None


# -------------------- FUNÇÕES JSON -------------------- #

def criar_arquivos_json():
    """Verifica e cria arquivos JSON necessários caso não existam."""
    print("Executando a função criar_arquivos_json")

    for arquivo in [ARQ_TAREFAS, ARQ_ARQUIVADAS]:
        if not os.path.exists(arquivo):
            with open(arquivo, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
            print(f"Arquivo criado automaticamente: {arquivo}")


def carregar_dados():
    """Carrega dados dos arquivos JSON para as listas globais."""
    print("Executando a função carregar_dados")
    global LISTA_TAREFAS, LISTA_ARQUIVADAS, PROXIMO_ID_TAREFA

    with open(ARQ_TAREFAS, "r", encoding="utf-8") as f:
        LISTA_TAREFAS = json.load(f)

    with open(ARQ_ARQUIVADAS, "r", encoding="utf-8") as f:
        LISTA_ARQUIVADAS = json.load(f)

    if LISTA_TAREFAS:
        PROXIMO_ID_TAREFA = max(t["id"] for t in LISTA_TAREFAS) + 1
    else:
        PROXIMO_ID_TAREFA = 1


def salvar_dados():
    """Salva lista de tarefas e arquivadas em seus arquivos JSON."""
    print("Executando a função salvar_dados")

    with open(ARQ_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(LISTA_TAREFAS, f, indent=4, ensure_ascii=False)

    with open(ARQ_ARQUIVADAS, "w", encoding="utf-8") as f:
        json.dump(LISTA_ARQUIVADAS, f, indent=4, ensure_ascii=False)


# -------------------- FUNÇÕES DE VALIDAÇÃO -------------------- #

def validar_opcao(pergunta, opcoes_validas):
    """Valida opções pré-definidas (prioridade, origem, status)."""
    print("Executando a função validar_opcao")

    while True:
        print(f"Opções válidas: {', '.join(opcoes_validas)}")
        entrada = input(pergunta + ": ").strip().title()

        if entrada in opcoes_validas:
            return entrada

        print("ERRO: valor inválido!")


def validar_titulo(titulo):
    """Verifica se o título já existe e não está vazio."""
    print("Executando a função validar_titulo")

    if not titulo.strip():
        print("ERRO: Título não pode ser vazio.")
        return False

    for t in LISTA_TAREFAS:
        if t["título"].lower() == titulo.lower():
            print("ERRO: Já existe uma tarefa com esse título.")
            return False

    return True


def buscar_tarefa_por_id(id_tarefa):
    """Busca uma tarefa pelo ID."""
    print("Executando a função buscar_tarefa_por_id")

    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None


# -------------------- CRUD DE TAREFAS -------------------- #

def criar_tarefa():
    """Cria uma nova tarefa completa com todos os campos."""
    print("Executando a função criar_tarefa")
    global PROXIMO_ID_TAREFA

    while True:
        titulo = input("Título da tarefa: ")
        if validar_titulo(titulo):
            break

    descricao = input("Descrição da tarefa: ").strip()
    prioridade = validar_opcao("Informe a Prioridade", OPCOES_PRIORIDADE)
    origem = validar_opcao("Informe a Origem da Tarefa", OPCOES_ORIGEM)

    nova = {
        "id": PROXIMO_ID_TAREFA,
        "título": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Pendente",
        "origem": origem,
        "data_criacao": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "data_conclusao": None
    }

    LISTA_TAREFAS.append(nova)
    PROXIMO_ID_TAREFA += 1

    print(f"Tarefa '{titulo}' criada com sucesso!")


def verificar_e_iniciar_tarefa():
    """Seleciona a tarefa mais urgente e inicia sua execução."""
    print("Executando a função verificar_e_iniciar_tarefa")
    global TAREFA_EM_EXECUCAO

    if TAREFA_EM_EXECUCAO:
        print(f"Tarefa já em execução: ID {TAREFA_EM_EXECUCAO['id']}")
        return

    prioridades = ["Urgente", "Alta", "Média", "Baixa"]

    for p in prioridades:
        for tarefa in LISTA_TAREFAS:
            if tarefa["prioridade"] == p and tarefa["status"] == "Pendente":
                tarefa["status"] = "Fazendo"
                TAREFA_EM_EXECUCAO = tarefa
                print(f"Iniciando tarefa: {tarefa['título']}")
                return

    print("Nenhuma tarefa pendente disponível.")


def atualizar_prioridade():
    """Atualiza a prioridade de uma tarefa existente."""
    print("Executando a função atualizar_prioridade")

    try:
        id_t = int(input("ID da tarefa: "))
    except:
        print("ERRO: Digite um número válido!")
        return

    tarefa = buscar_tarefa_por_id(id_t)
    if not tarefa:
        print("Tarefa não encontrada.")
        return

    nova_pri = validar_opcao("Nova prioridade", OPCOES_PRIORIDADE)
    tarefa["prioridade"] = nova_pri

    print("Prioridade atualizada!")


def concluir_tarefa():
    """Marca tarefa como concluída e registra data de conclusão."""
    print("Executando a função concluir_tarefa")
    global TAREFA_EM_EXECUCAO

    try:
        id_t = int(input("ID da tarefa: "))
    except:
        print("ERRO: ID inválido.")
        return

    tarefa = buscar_tarefa_por_id(id_t)
    if not tarefa:
        print("Tarefa não encontrada.")
        return

    tarefa["status"] = "Concluída"
    tarefa["data_conclusao"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    if TAREFA_EM_EXECUCAO and TAREFA_EM_EXECUCAO["id"] == id_t:
        TAREFA_EM_EXECUCAO = None

    print("Tarefa concluída!")


def arquivar_tarefas_antigas():
    """Arquiva tarefas concluídas há mais de 7 dias."""
    print("Executando a função arquivar_tarefas_antigas")
    global LISTA_TAREFAS, LISTA_ARQUIVADAS

    novas = []
    agora = datetime.datetime.now()

    for tarefa in LISTA_TAREFAS:
        if tarefa["status"] == "Concluída" and tarefa["data_conclusao"]:
            data = datetime.datetime.strptime(tarefa["data_conclusao"], "%d/%m/%Y %H:%M")
            if agora - data > datetime.timedelta(days=7):
                tarefa["status"] = "Arquivado"
                LISTA_ARQUIVADAS.append(tarefa)
                continue
        novas.append(tarefa)

    LISTA_TAREFAS = novas
    print("Arquivamento finalizado.")


def excluir_tarefa():
    """Exclusão lógica: muda status para 'Excluída'."""
    print("Executando a função excluir_tarefa")

    try:
        id_t = int(input("ID da tarefa: "))
    except:
        print("ERRO: ID inválido.")
        return

    tarefa = buscar_tarefa_por_id(id_t)
    if not tarefa:
        print("Tarefa não encontrada.")
        return

    tarefa["status"] = "Excluída"
    print("Tarefa excluída logicamente.")

def parse_data(data_str):
    """
    Converte datas usadas no sistema, aceitando:
    - Formato manual: '%d/%m/%Y %H:%M'
    - Formato ISO automático gerado pelo Python
    """
    formatos = [
        "%d/%m/%Y %H:%M",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S"
    ]

    for f in formatos:
        try:
            return datetime.datetime.strptime(data_str, f)
        except ValueError:
            pass

    raise ValueError(f"Formato de data inválido: {data_str}")

def exibir_tabela(tarefas):
    """
    Exibe todas as tarefas em formato de tabela organizada.
    """
    print("Executando a função exibir_tabela")

    if not tarefas:
        print("\nNenhuma tarefa encontrada.\n")
        return

    # Cabeçalho da tabela
    print("\n" + "="*120)
    print(f"{'ID':<5} | {'Título':<20} | {'Prioridade':<10} | {'Status':<12} | {'Origem':<12} | {'Criação':<20} | {'Conclusão':<20}")
    print("-"*120)

    for t in tarefas:

        data_conc = t.get("data_conclusao", "")
        if data_conc is None:
            data_conc = ""

        print(f"{t['id']:<5} | "
              f"{t['titulo']:<20} | "
              f"{t['prioridade']:<10} | "
              f"{t['status']:<12} | "
              f"{t['origem']:<12} | "
              f"{t['data_criacao']:<20} | "
              f"{data_conc:<20}")

    print("="*120 + "\n")

# -------------------- RELATÓRIOS -------------------- #

def gerar_relatorio():
    exibir_tabela(LISTA_TAREFAS)


def relatorio_arquivadas():
    """Exibe apenas tarefas arquivadas."""
    print("Executando a função relatorio_arquivadas")

    if not LISTA_ARQUIVADAS:
        print("Nenhuma tarefa arquivada.")
        return

    print("="*80)
    print("TAREFAS ARQUIVADAS")
    print("="*80)

    for t in LISTA_ARQUIVADAS:
        print(f"ID: {t['id']}")
        print(f"Título: {t['título']}")
        print(f"Descrição: {t['descricao']}")
        print(f"Prioridade: {t['prioridade']}")
        print(f"Origem: {t['origem']}")
        print(f"Status: {t['status']}")
        print(f"Data criação: {t['data_criacao']}")
        print(f"Data conclusão: {t['data_conclusao']}")
        print("-"*80)


# -------------------- MENU PRINCIPAL -------------------- #

def exibir_menu():
    print("""
========= MENU =========
1. Criar tarefa
2. Iniciar tarefa urgente
3. Atualizar prioridade
4. Concluir tarefa
5. Arquivar tarefas antigas
6. Excluir tarefa (lógica)
7. Relatório geral
8. Relatório arquivadas
0. Sair
""")


def main():
    criar_arquivos_json()
    carregar_dados()

    while True:
        exibir_menu()

        try:
            opcao = int(input("Opção: "))
        except:
            print("ERRO: digite um número!")
            continue

        match opcao:
            case 1:
                criar_tarefa()
            case 2:
                verificar_e_iniciar_tarefa()
            case 3:
                atualizar_prioridade()
            case 4:
                concluir_tarefa()
            case 5:
                arquivar_tarefas_antigas()
            case 6:
                excluir_tarefa()
            case 7:
                gerar_relatorio()
            case 8:
                relatorio_arquivadas()
            case 0:
                salvar_dados()
                print("Dados salvos. Encerrando...")
                exit()
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()

