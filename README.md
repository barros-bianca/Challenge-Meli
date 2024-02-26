Challenge Meli

1- Objetivo

O objetivo deste projeto é construir um dashboard na ferramenta de data visualization Tableau. 
O dashboard inclui gráficos que demonstram o crescimento da internet na Argentina, ritmo de evolução, perfil dos usuários, assinaturas de banda larga e internet fixa, bem como possíveis causas do cenário apresentado.

2- Fonte de Dados

A principal fonte de dados utilizada foi a data.worldbank.org, sendo coletadas as seguintes tabelas, todas em nível de detalhamento global:

Indivíduos que utilizam a internet 
Assinaturas de Banda Larga Fixas 
Assinaturas de Celular Móvel 

Complementarmente, foram coletados os seguintes dados do Instituto Nacional de Estadística y Censos (INDEC), órgão oficial da Argentina:

Tabelas do Módulo Acesso e Utilização de Tecnologias de Informação e Comunicação. Tabelas do quarto trimestre de 2022

Essa tabela traz dados demográficos dos usuários de internet, como por exemplo: forma de acesso (se por computador ou celular), sexo, idade e escolaridade.

3- Modelagem

Após a coleta dos dados, foi observada a necessidade de uma modelagem prévia, antes da ingestão pelo Tableu. Essa modelagem envolveu a:

Retirada de cabeçalhos que impedia a correta identificação das colunas 
Filtro de informações, pois uma mesma sheet do excel pode conter diversas tabelas

Após a ingestão houve uma segunda etapa de adequação dos dados, como a aplicação da função “dinamização” de tabelas presente no Tableu e a mudança dos data types visando a construção das visualizações.

4 - Gráficos

Considerando os indicadores objetivados no projeto, foram geradas as seguintes visualizações:

Global X ARG - Compara a % de usuários de internet na Argentina com a % global, entre os anos 2000 a 2022.
Porcent. Atual - Traz a informação da % da população que utiliza a internet mundialmente e na Argentina, segundos os dados mais atuais (2022) 
Taxa de Cresc - Traz a % do crescimento ano a ano de usuários de internet.
Comp/Cel - Compara a % de acessos feitos por celular e computadores.
Banda Larga - Compara o número de assinaturas de banda larga fixa e telefonia móvel na Argentina.
Escolaridade - Mostra a % de usuários Argentinos conforme o nível de escolaridade.
Idade - Mostra a % de usuários Argentinos conforme a faixa etária.

A etapa de criação da visualização envolveu processos como criação de campo, adição de títulos, escolha do melhor tipo de visualização, cores, organização das informações, filtro de datas (anos), relacionamento entre tabelas, etc.

5- Insigths

Após a geração das visualizações foi possível obter os principais insights:

A porcentagem da população que acessa a internet na Argentina passou a ser maior que média global a partir de 2009, mantendo-se assim até os dias atuais com uma taxa de 88% no país mencionado e 85% na média global em 2022.
A porcentagem de população que acessa a internet vem crescendo tanto na Argentina quanto globalmente, embora o ritmo venha se desacelerando desde 2010.
Atualmente a maior parte da população Argentina acessa a internet por meio do celular (92%), observando-se uma queda no uso de computadores. O acesso por meio do celular também pode estar relacionado a democratização e consequente aumento do número de usuários da rede.
Tanto as assinaturas de banda larga fixa quanto internet móvel na Argentina tem crescido nos últimos 10 anos. Porém as assinaturas de banda larga tem crescido de forma mais consistente, enquanto as assinaturas de internet móvel sofrem mais oscilações e apresentam crescimento desacelerado.
Quanto mais escolarizada, maior é a porcentagem da população Argentina que acessa a internet, principalmente se tratando de ensino secundário ou universitário completo.
A maior parte da população Argentina que utiliza a internet possui entre 13 e 64 anos.

6- Conclusão

A partir dos insights obtidos, é possível utilizá-los de forma estratégica, considerando o modelo de negócios do Mercado Livre:

Com um acesso bem consolidado no país e até maior que média global, o Mercado Livre pode manter a segurança na sua atuação de mercado focada em e-commece, utilizado tanto por empresas que vendem seus produtos, quanto por usuários físicos que buscam por essas mercadorias.
Sabendo que a maior parte dos acessos é feita por celular, é possível adaptar o layout do site Mercado Livre visando melhor navegação em smartphones e consequentemente melhor experiência do usuário.
Com o número de assinaturas de banda larga em crescimento consistente, é possível enxergar oportunidades de expansão das parcerias com streaming, que possui o consumo viabilizado pela internet de alta velocidade.
Os dados de escolaridade e idade dos usuários viabilizam a segmentação de campanhas de marketing e oferta de produtos, oferecendo uma experiência mais personalizada ao consumidor final.

7- Referências:

https://data.worldbank.org/indicator/IT.NET.USER.ZS

https://data.worldbank.org/indicator/IT.CEL.SETS

https://data.worldbank.org/indicator/IT.NET.BBND

https://www.indec.gob.ar/indec/web/Nivel4-Tema-4-26-71
