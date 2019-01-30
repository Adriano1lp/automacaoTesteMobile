#language: pt
Funcionalidade: Nova simulacao
        Simular Emprestimos

        Contexto: Abrir App
            Dado que eu abra o app na pagina principal

        Esquema do Cenario: Tentar Simulação 
            
            Quando eu coloco <valor> e <prazo>
            E clico em "contratar agora"
            Então devo ver a seguinte tela <resposta>

        Exemplos: Valores
            |   valor   |   prazo   | resposta   |
            |   1000    |   6       | contratar  |
            |   100     |   6       | Mensagem   |
            |   1000    |   5       | Mensagem   |
            |   21000   |   6       | Mensagem   |
            |   1000    |   19      | Mensagem   |
          
       