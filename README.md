<!DOCTYPE html>
<html>
<head>
    <title>Documentação do Código</title>
</head>
<body>
    <h1>Documentação do Código</h1>
    <p>Este script Python autentica e obtém tokens de um serviço web usando um certificado digital.</p>

    <h2>Dependências</h2>
    <ul>
        <li>requests_pkcs12</li>
        <li>python-dotenv</li>
        <li>os</li>
    </ul>

    <h2>Descrição do Código</h2>
    <p>O script começa importando os módulos necessários. Em seguida, ele define o caminho para o certificado digital e o arquivo .env que contém a senha do certificado.</p>

    <h2>Uso</h2>
    <p>Para usar este script, você precisa ter um certificado digital válido e a senha correspondente. O certificado deve estar na pasta 'arquivo certificado' e a senha deve estar armazenada em uma variável de ambiente no arquivo .env.</p>

    <h2>Funções</h2>
    <ul>
        <li><strong>configurar_api:</strong> Esta função é usada para configurar a API. Ela define os headers da requisição e faz uma requisição GET para a URL da API.</li>
    </ul>

    <h2>Outputs</h2>
    <p>O script imprime os valores das variáveis 'Set-Token' e 'X-CSRF-Token' que são obtidos da resposta da requisição POST.</p>
</body>
</html>
