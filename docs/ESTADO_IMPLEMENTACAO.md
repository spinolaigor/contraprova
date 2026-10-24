# Estado real da implementação

Atualizado em 2026-10-24.

## Implementado no repositório
- Dashboard responsivo brutalista (`index.html`), sem dependências externas.
- Leitura exclusiva de `data/publicados.json`, com validação básica da base.
- Filtros por autor, evento e texto; exportação CSV e links diretos para checagens.
- Exportador Python de registros revisados, com testes e workflow de validação.
- Catálogo mestre de fontes e política editorial.
- Workflow de publicação GitHub Pages (depende de configuração e execução bem-sucedida no GitHub).

## Ainda não implementado / não confirmado
- Importação integral da v0.3 original, incluindo o coletor e seus testes.
- Descoberta contínua por RSS/sitemaps e integração de todas as fontes.
- Auditoria de afirmações reais e revisão humana.
- Execução bem-sucedida dos workflows no GitHub.
- URL pública do GitHub Pages funcionando.
- Visualizações avançadas e gráficos comparativos (dependem de dados revisados).

## Regras de interpretação
- Total zero significa zero registros publicados no Contraprova, não zero afirmações checadas na imprensa.
- Nenhum veredito automatizado entra nos totais sem revisão humana documentada.
- Atribuições e classificações permanecem vinculadas à fonte original.
- Não interpretar amostra de checagens como taxa de veracidade de todas as falas.

## Próxima entrega
Importar o restante da aplicação v0.3, testar a coleta em ambiente real, corrigir falhas de workflow e ampliar indicadores sem sacrificar rastreabilidade.
