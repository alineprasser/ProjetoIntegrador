# ProjetoIntegrador
 Projeto feito com Arduino UNO, MySQL 5.5 e Python 3.6
 
 1 - Para que o documento em python possa realizar a leitura serial, é necessário que o código "Ler_NFC.ino" esteja carregado no arduíno.
 
 2 - O arquivo "main.py" é o principal para que este projeto seja executado.
 
 3 - Ao iniciar este arquivo, será dado a opção para iniciar a chamada ou para abrir o menu de configuração das tags NFC.
 
 4 - Caso a opção selecionada seja a chamada, o arquivo "LeitorNfcPython.py" é iniciado. O arquivo "Ler_NFC.ino" efetuará a leitura das tags e registrará seu UID (Unique Identifier) na porta serial em que o arduíno está conectado. O arquivo em Python, por sua vez, se encarrega de receber essa informação através da leitura serial e fazer o tratamento desta informação, conferindo sua autenticidade no banco de dados até que o professor responsável encerre a chamada. Esse arquivo retorna a lista de alunos presentes na aula. Se nenhum aluno estiver presente, o arquivo retorna uma lista vazia e exibe uma mensagem no console.
 
 5 - Caso a opção de configuração seja selecionada, o arquivo "ifcbanco.py" é iniciado. Este arquivo abrirá um menu, onde o usuário poderá escolher dentre quatro opções: registrar um professor no banco de dados, registrar um aluno no banco de dados, deletar uma tag ou voltar ao menu inicial, do arquivo "main.py".
 
 6 - Para registrar tanto aluno quanto professor no banco de dados é necessário que uma tag em branco (não cadastrada) seja aproximada ao leitor. Caso uma tag que já está cadastrada seja aproximada, o programa não efetuará atualização das informações, mas sim retornará ao menu anterior. Os dados que se deseja registrar no banco de dados serão feitos via input no Python, para que o próprio usuário os registre. Para deletar uma tag basta aproximá-la do leitor e uma confirmação será pedida. Esta opção só pode ser concluída com o uso de uma tag configurada como ADMINISTRADOR, para que não haja risco de uma ação não-intencional.
 
 Ao fim dos casos, basta inserir o número 0 para sair e encerrar a operação.
