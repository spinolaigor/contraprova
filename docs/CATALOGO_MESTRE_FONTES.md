# Catálogo mestre de fontes — Contraprova

**Status:** inventário inicial para auditoria; inclusão nesta lista NÃO comprova conteúdo, confiabilidade, existência atual ou autorização para scraping. URLs devem ser testadas individualmente. Atualizado: 2026-10-24.

## A. Checagem jornalística — prioridade editorial
| Fonte | URL inicial | Observação |
|---|---|---|
| Agência Lupa | https://www.agencialupa.org/checagem/2026/10/23/ao-vivo-checagem-do-ultimo-debate-entre-lula-e-flavio-bolsonaro-no-segundo-turno/ | Artigo localizado no projeto v0.3 |
| Aos Fatos | https://www.aosfatos.org/noticias/checamos-flavio-bolsonaro-lula-debate-globo/ | Confirmar atualização e itens individuais |
| UOL Confere | https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm | Confirmar itens e evidências |
| g1 Fato ou Fake | https://g1.globo.com/fato-ou-fake/ | Localizar artigo específico |
| Estadão Verifica | https://www.estadao.com.br/estadao-verifica/ | Localizar artigo específico |
| Projeto Comprova | https://projetocomprova.com.br/ | Localizar artigo específico |
| Terra / Aos Fatos | https://www.terra.com.br/ao-vivo/noticias/eleicoes/debate-da-globo-confira-a-checagem-realizada-pelo-terra-e-aos-fatos%2Cac675796e16b1783f2f970e8c4fbf4f8ppkgasp4.html | Possível republicação; não duplicar vereditos |

## B. Agregadores e análise automatizada — pistas, não autoridade factual
| Fonte | URL | Observação |
|---|---|---|
| Quem Mentiu? | https://quemmentiu.com.br/ | Conferir origem dos números do print |
| Voto por Ideias | https://www.votoporideias.com.br/debates-segundo-turno-2026/globo | Verificar proveniência de cada item |
| FlagCheck | https://flagcheck.com.br/eleicoes-2026/checagem-debate-globo/ | Verificar metodologia e itens |
| Debate da Globo Checado | https://checagem-debate.vercel.app/ | Distinguir IA de revisão humana |
| Verifique a Verdade | https://verifiqueaverdade.com.br/debates/globo-2026-10-23/ | Verificar metodologia |
| Debates.cc | https://www.debates.cc/ | Análise automatizada; não confundir com fact-check |

## C. Fontes primárias — evidências e contexto
| Fonte | URL | Uso |
|---|---|---|
| TSE resultados | https://www.tse.jus.br/eleicoes/resultados-eleicoes | Resultados oficiais |
| TSE PesqEle | https://pesqele-divulgacao.tse.jus.br/ | Registro de pesquisas |
| IBGE | https://www.ibge.gov.br/ | Indicadores estatísticos |
| Banco Central | https://www.bcb.gov.br/ | Séries econômicas |
| Tesouro Transparente | https://www.tesourotransparente.gov.br/ | Finanças públicas |
| Portal da Transparência | https://portaldatransparencia.gov.br/ | Gastos e transferências |
| TCU | https://portal.tcu.gov.br/ | Auditorias e fiscalização |
| Câmara dos Deputados | https://www.camara.leg.br/ | Projetos e legislação |
| Senado Federal | https://www25.senado.leg.br/web/atividade | Atividade legislativa |
| Planalto | https://www.planalto.gov.br/ccivil_03/ | Normas legais |

## D. Material de origem
- Gravação integral do debate, com data, emissora e minutagem a localizar e conferir.
- Transcrição com identificação de interlocutor e marcação temporal, revisada contra o vídeo.
- Planos de governo registrados no TSE, vinculados à candidatura e eleição correspondentes.

## Critérios obrigatórios de ingestão
1. Uma **afirmação única** pode possuir **múltiplas verificações** e evidências.
2. Guardar URL, editoria, autor (quando houver), data de publicação, consulta, versão e link para o trecho específico.
3. Preservar veredito original, metodologia, correções e discordâncias; jamais fundir classificações incompatíveis silenciosamente.
4. Não somar republicações de parceiros como checagens independentes.
5. Separar: `descoberto`, `coletado`, `em_auditoria`, `revisado`, `publicado`, `corrigido`.
6. Scraping somente quando permitido; preferir RSS, APIs, sitemaps e metadados; observar termos, robots.txt, limites e direitos autorais.
7. Não publicar automaticamente vereditos de IA como conclusões factuais.
8. Não inferir a taxa geral de mentiras a partir da seleção não aleatória dos checadores.
9. Não converter suspeitas ou alegações sobre pessoas em fatos comprovados sem evidência apropriada.
10. Todo gráfico deve declarar universo, fonte, data de corte e método de contagem.

## Próxima implementação
Ampliar o coletor de três URLs fixas para descoberta por feeds/sitemaps, registrar candidatos a artigos em fila de revisão, e testar conectores individualmente antes de ativá-los.
