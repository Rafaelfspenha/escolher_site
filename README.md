# escolher_site

Este é um script Python que usa a biblioteca PyAutoGUI para automatizar a abertura de um navegador da Web e a navegação para um site específico com base na entrada do usuário. 
O usuário é apresentado a um menu de opções para diferentes sites de mídia social e pode inserir um número correspondente à sua escolha. O script usa uma série de comandos PyAutoGUI para abrir uma nova instância do navegador Chrome e navegar até o site selecionado.

Aqui está uma breve visão geral do que o script faz:

1- Define uma função menu que imprime uma lista de opções e solicita que o usuário insira um número correspondente à sua escolha. A função retorna a entrada do usuário como um número inteiro.
2- Chama a função menu para obter a escolha do site do usuário.
3- Usa PyAutoGUI para simular o pressionamento da tecla Windows para abrir o menu Iniciar, espera 4 segundos e, em seguida, digita "chrome" e pressiona Enter para abrir uma nova instância do navegador Chrome.
4- Usa uma série de declarações condicionais para determinar para qual URL do site navegar com base na escolha do usuário e usa PyAutoGUI para digitar a URL e pressionar Enter para carregar o site.
5- Aguarda 4 segundos e, em seguida, pressiona Enter novamente para confirmar o carregamento do site.

Vale a pena notar que este script depende de um conjunto específico de condições para funcionar corretamente (por exemplo, o usuário deve ter o Chrome instalado e definido como seu navegador padrão, o menu Iniciar deve estar acessível por meio da tecla Windows etc.) funcionam como esperado em todos os ambientes.



