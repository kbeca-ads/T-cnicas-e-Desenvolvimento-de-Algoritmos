📘 Técnica e Desenvolvimento de Algoritmos

👨‍🎓 Alunos

John Lucas Garcia dos Santos

Vitor Daniel Dorea Santos

🗂 Gerenciador de Tarefas – Projeto Final

Este projeto foi desenvolvido como atividade prática da disciplina Técnicas de Desenvolvimento de Algoritmos, com foco em:

Organização e modularização de código

Manipulação de arquivos JSON

Persistência de dados

Boas práticas de programação

Sistema completo com ciclo de vida de tarefas

O sistema implementa um gerenciador de tarefas completo, incluindo criação, atualização, conclusão, arquivamento e exclusão lógica.

📌 Funcionalidades do Sistema

✔ Criar Tarefa

Solicita título, descrição, prioridade e origem.

Gera data automática de criação.

Validação dos campos obrigatórios.

Atribui ID único automaticamente.

✔ Verificar Urgência

Seleciona a tarefa mais urgente disponível.

Atualiza o status para "Fazendo".

✔ Atualizar Prioridade

Permite alterar a prioridade com validação.

✔ Concluir Tarefas

Define data de conclusão.

Calcula o tempo de execução no relatório.

✔ Arquivamento Automático

Tarefas concluídas há mais de 7 dias são movidas para
tarefas_arquivadas.json.

✔ Exclusão Lógica

Tarefa é marcada como Excluída, mas não removida do sistema.

✔ Relatórios

Relatório geral de tarefas.

Relatório apenas de tarefas arquivadas.

🗂 Estrutura de Arquivos do Projeto
Arquivo	Função
gerenciador_tarefas.py	Código principal do sistema
tarefas.json	Banco de dados principal
tarefas_arquivadas.json	Histórico de tarefas arquivadas
README.md	Documentação
.gitignore	Itens ignorados no Git
LICENSE	Licença MIT
🚀 Como Executar o Sistema

No terminal, execute:

python gerenciador_tarefas.py


Os arquivos tarefas.json e tarefas_arquivadas.json serão criados automaticamente caso não existam.

## 👨‍💻 Grupo

| Integrante | GitHub |
|-------------|---------|

| <img src="https://github.com/Vitorddorea.png" width="80" style="border-radius:50%"> <br> **Vitor Daniel Dorea Santos** <br> 📍 Desenvolvedor e estudante de Análise e Desenvolvimento de Sistemas <br> 💬 Entusiasta em tecnologia, sempre buscando novas formas de inovar e colaborar em equipe. | [github.com/Vitorddorea](https://github.com/Vitorddorea) |<br>
| <img src="https://github.com/kbeca-ads.png" width="80" style="border-radius:50%"> <br> **John Lucas Garcia dos Santos** <br> 📍 Desenvolvedor e estudante de Análise e Desenvolvimento de Sistemas <br> 💬 Entusiasta em tecnologia, sempre buscando novas formas de inovar e colaborar em equipe. | [github.com/kbeca-ads](https://github.com/kbeca-ads) |
