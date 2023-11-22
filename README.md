# Documentação do Código

Código em python para retornar a autenticação necessária para todas as requisições dentro do catálogo de APIs do Portal único de Comércio Exterior.
> **Documentação oficial:** [clique aqui](https://api-docs.portalunico.siscomex.gov.br/)

## Dependências

É necessário instalação das seguintes bibliotecas:

#### Para realizar a requisição a API
```
pip install requests_pkcs12
```

#### Para leitura do arquivo .env (onde você irá colocar a senha do certificado)

```
pip install python-dotenv
```

#### Para auxilio nos caminhos dinâmicos
```
pip install os
```

## Configuração do certificado e senha

Para usar este script, você precisa ter um certificado digital válido no formato `.pfx` e a senha correspondente. O certificado deve estar na pasta `arquivo certificado` e a senha deve estar armazenada em uma variável de ambiente no arquivo `.env`.

#### Local do arquivo .pfx
![image](https://github.com/leogsantos/autenticacao-pucomex/assets/64739776/9157fe7a-8215-47f6-a3ee-36d9879bc19c)

> **Necessário alterar no código o nome do seu arquivo**
    ![image](https://github.com/leogsantos/autenticacao-pucomex/assets/64739776/a3e6f0af-4441-4f7b-a6fa-c2c1203862a6)



#### Configuração da senha

![image](https://github.com/leogsantos/autenticacao-pucomex/assets/64739776/2da1c901-3c73-4569-873f-c8165160711e)


## Outputs

O script imprime os valores das variáveis 'Set-Token' e 'X-CSRF-Token' que são obtidos da resposta da requisição POST, onde essas variavéis devem ser usadas em todas as requisições do .

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/leogsantos" title="Perfil do Github">
        <img src="https://avatars.githubusercontent.com/u/64739776?v=4" width="100px;" alt="Foto do Leonardo no GitHub"/><br>
        <sub>
          <b>Leonardo Gomes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Pedrohds7" title="Perfil do Github">
        <img src="https://avatars.githubusercontent.com/u/49046215?v=4" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Pedro Henrique</b>
        </sub>
      </a>
    </td>
    
  </tr>
</table>
