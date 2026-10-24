# Referências técnicas para o Contraprova

Pesquisa inicial: 2026-10-24. Referências externas são inspiração, não componentes instalados ou validados.

## Projetos
- Meedan Fetch — https://github.com/meedan/fetch — agregação de checagens e conectores por fonte. Avaliar arquitetura de adaptadores, sem adotar stack pesada no MVP.
- AFP MediaLab De Facto — https://github.com/medialab/defacto-enrichment-public — dados estruturados ClaimReview e enriquecimento.
- FEAT — https://github.com/GONZOsint/FEAT — exploração de dados de fact-checking.
- ClaimBuster — https://claimbuster.org/ — triagem de alegações verificáveis; saída automatizada nunca é veredito.
- FactChecks.br — https://github.com/fake-news-UFG/FactChecks.br — benchmarks em português.
- Data Commons Fact Check — https://datacommons.org/factcheck/download — base histórica estruturada; verificar licenças por origem.
- OpenErrata — https://openerrata.com/ — referência de transparência e rastreabilidade, não adoção automática do método.
- Schema.org ClaimReview — https://schema.org/ClaimReview — modelo interoperável.

## Decisões propostas
1. Usar esquema interno para alegações, checagens, fontes, evidências e revisões; mapear campos compatíveis com ClaimReview na exportação.
2. Implementar conectores independentes por fonte, preferindo RSS, sitemaps e metadados JSON-LD.
3. Preservar URL canônica, origem, data, licença, estado de revisão e trilha de correções.
4. Detectar duplicatas e republicações sem perder verificações independentes.
5. Manter triagem por IA e auditoria editorial separadas.
6. Não usar classificação de credibilidade de veículos como substituto de evidência.
7. Investigar discussões no Reddit como inspiração e descoberta de conjuntos de dados, nunca como prova factual.

## Aviso
Este documento não afirma que APIs, licenças, feeds ou compatibilidade foram testados. Cada integração exige verificação específica.
