# ADR 005 — Descoberta estruturada sem comprometer a publicação

Data: 2026-10-24

## Decisão
Manter dashboard estático no GitHub Pages; coleta e transformação executadas em GitHub Actions; revisão editorial obrigatória antes de entrar na base pública.

## Alternativas consideradas
- Backend com PostgreSQL e API própria: flexível, mas introduz custo operacional, segurança, disponibilidade e manutenção cedo demais.
- Scraping integral de páginas e classificação por IA: frágil, sujeito a alterações de HTML e propenso a atribuições equivocadas.
- RSS/sitemaps + JSON-LD ClaimReview: descoberta progressiva e aproveitamento de estrutura publicada pelos próprios checadores.

## Implementação
`scripts/extrair_claimreview.py` lê HTML local autorizado e extrai candidatos de marcações JSON-LD, inclusive `@graph`. Preserva a classificação original, não a interpreta e marca todos os registros `pending_review`. O programa não acessa a rede nem modifica `data/publicados.json`.

## Próximas integrações
1. Validar disponibilidade e regras de acesso por fonte.
2. Acrescentar descoberta RSS/Atom e sitemap com limites por domínio.
3. Associar novos artigos a candidatos, evento e transcrição, sem assumir equivalência textual.
4. Testar fontes em execução real, registrar taxa de sucesso e duplicação.
5. Integrar API Fact Check Tools mediante chave/configuração apropriada.
6. Adotar revisão humana e exportação de registros aprovados.

## Limitações
Nem todos os veículos publicam ClaimReview. A ausência de marcação não significa ausência de checagem. A classificação textual de um veículo não é automaticamente equivalente à de outro. Registros encontrados não são publicados sem auditoria.

## Referências
- https://schema.org/ClaimReview
- https://developers.google.com/search/docs/appearance/structured-data/factcheck
- https://developers.google.com/fact-check/tools/api/reference/rest
