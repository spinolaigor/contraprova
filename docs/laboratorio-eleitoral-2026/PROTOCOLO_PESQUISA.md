# Contraprova | Laboratório Eleitoral 2026 — protocolo de pesquisa v0.1
Data: 26/10/2026. Status: **protocolo exploratório; resultados subnacionais pendentes de processamento**.

## Questão principal
Que parcelas da mudança da margem presidencial entre os turnos de 2026 são descritivamente associadas a (a) comparecimento, (b) votos válidos versus brancos/nulos, (c) redistribuição de votos de outras candidaturas, e (d) alterações territoriais? Nenhum agregado identifica a escolha individual.

## Linha de base verificada
TSE, 2º turno: Lula 64.256.232 (51,79% dos válidos), Flávio Bolsonaro 59.826.041 (48,21%); comparecimento ~128,2 milhões; abstenção ~19,2%, contra 21,08% no 1º turno.
Fonte: https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/presidente-do-tse-anuncia-reeleicao-de-lula-e-faz-balanco-do-2o-turno-das-eleicoes-2026
Totais do 1º turno reportados por agregador baseado no TSE (validar novamente no CSV oficial): Lula 53.879.538; Flávio 56.104.503.
Fonte secundária: https://eleicoes.radioplfm.com.br/
Crescimentos nominais aritméticos: Lula +10.376.694; Flávio +3.721.538. **Não são fluxos individuais de voto**.

## Hipóteses registradas antes do teste
H1: municípios com maior queda na abstenção apresentam maior mudança de margem pró-Lula, condicionando por margem inicial e características territoriais.
H2: a associação de H1 é heterogênea por UF, tamanho municipal e renda.
H3: mudança na proporção de votos brancos/nulos ajuda a explicar parte da variação de votos válidos.
H4: mudança territorial da margem em 2026 difere da observada em 2022.
H5: diferenças entre pesquisas e urnas dependem, em parte, de estimativas de comparecimento e momento da coleta.
Hipóteses concorrentes: mobilização simétrica, realocação de votos de terceiros, mudança de preferência entre turnos, efeitos de composição, artefatos de agregação.

## Dados e unidade
Fonte primária: https://dadosabertos.tse.jus.br/dataset/resultados-2026
Baixar CSV de votação presidencial por seção e detalhe da apuração; 1º e 2º turnos; equivalentes de 2022. Preservar ZIP/CSV bruto, URL, data, tamanho, SHA-256, dicionário e licença.
Unidade principal: município × turno; unidade secundária: seção eleitoral × turno **somente após verificar correspondência e mudanças de seção**.
IBGE: indicadores censitários municipais; nunca imputar renda/religião de um eleitor a partir de média municipal.
Pesquisas: instituto, contratante, período de campo, população-alvo, modo, ponderação, pergunta, indecisos, margem de erro e divulgação.

## Métricas
Comparecimento = comparecentes/eleitorado apto.
Abstenção = abstinentes/eleitorado apto.
Taxa de válidos = votos válidos/comparecentes.
Participação do candidato = votos nominais do candidato/votos válidos.
Margem de votos = votos Lula - votos Flávio; margem percentual = participação Lula - participação Flávio.
Variação de margem = margem 2º turno - margem 1º turno, preferencialmente em votos e com definição explícita do universo de candidatos.
Crescimento absoluto = votos nominais no 2º - votos nominais no 1º.
Separar sempre pontos percentuais de variação percentual relativa.

## Análises
1. Conferência nacional e por UF: soma de candidatos + brancos + nulos = comparecimento; verificar categorias de anulados; checar denominadores.
2. Painel de decomposição descritiva dos dois turnos com gráfico de barras e waterfall dos totais.
3. Mapas de variação por município, com normalização pelo eleitorado, e destaque MG/BH.
4. Regressões multivariadas com efeitos fixos de UF, ponderação pré-registrada e erros robustos; comparar especificações; tratar associações como não causais.
5. Sensibilidade a tamanho de município, ausência de dados, seções não pareadas e ponderação.
6. Inferência ecológica somente com premissas explícitas, intervalos e análises de sensibilidade. Nunca publicar fluxos individuais como observados.
7. Pesquisas: erro absoluto por candidato, erro na margem, viés médio e calibração; não comparar institutos com janelas/populações distintas sem ressalvas.
8. Teoria: voto retrospectivo, clivagens sociais, polarização afetiva, mobilização e realinhamento como modelos concorrentes, não conclusões.

## Visualização pública
Home: resultado, diferença em votos, abstenção e gráficos dos dois turnos com legenda e denominadores.
Abas: Anatomia da virada; Mapa; MG e Belo Horizonte; Pesquisas; Teorias; Fontes e Método.
Cada visual deve ter fonte, data de extração, unidade, definição, amostra N, incerteza quando aplicável e botão de download de dados.
Estética: brutalismo editorial, cores contrastantes e padrões redundantes; acessibilidade e versão mobile; sem login.
Separar **fato oficial**, **cálculo reproduzido**, **estimativa**, **hipótese** e **não identificado**.

## Critérios de publicação
- Nunca declarar que a queda da abstenção causou a vitória apenas por correlação agregada.
- Revisão humana para interpretações causais e correções públicas versionadas.
- CI valida schemas, somas, URLs de fonte, dados faltantes e artefatos reproduzíveis.
- Este estudo não modifica os vereditos editoriais dos debates nem o dataset de checagens.
- Não publicar dados de seção identificáveis por eleitor; voto individual é secreto.

## Próxima execução
Extrair CSVs oficiais, validar checksums e totais, produzir tabelas municipio_turno.parquet e secao_turno.parquet, gerar análise exploratória, revisar divergências e somente então ativar gráficos subnacionais.
