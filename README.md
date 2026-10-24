# CONTRAPROVA ■

**Menos ruído. Mais dados.**

Observatório independente de checagens e evidências públicas. O objetivo é reunir informações rastreáveis sobre afirmações verificáveis, sem apresentar dados preliminares como conclusões.

**Site:** https://spinolaigor.github.io/contraprova/

## Como funciona

1. **Monitoramento:** fontes e publicações são acompanhadas em `data/monitoramento/`. O monitoramento inicial observa três URLs específicas e não descobre automaticamente todos os artigos.
2. **Auditoria:** registros são conferidos e documentados em `data/auditoria/registros.json`.
3. **Publicação:** `scripts/gerar_publicados.py` exporta somente registros aprovados para `data/publicados.json`.
4. **Dashboard:** `index.html` lê exclusivamente a base publicada; amostras demonstrativas e descobertas não entram nos indicadores.

**Verificado não significa verdadeiro:** significa que a auditoria da afirmação foi concluída. Vereditos originais podem ser verdadeiro, falso, impreciso, sem provas ou divergente, sempre atribuídos às fontes.

## Estado

- Dashboard público: disponível.
- Proteção dos dados publicados: implementada.
- Monitoramento inicial: workflow criado; verificar execuções no GitHub Actions.
- Checagens reais aprovadas: **nenhuma** nesta base inicial.
- Descoberta via RSS/sitemap/ClaimReview: planejada, ainda não implementada.
- Auditoria em escala: planejada, ainda não executada.

## Executar testes

Requer Python 3.12 ou compatível, sem bibliotecas externas para os módulos atuais:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/gerar_publicados.py
```

## Documentação

- [Política de publicação](docs/POLITICA_PUBLICACAO.md)
- [Catálogo de fontes](docs/CATALOGO_MESTRE_FONTES.md)
- [Coleta contínua](docs/COLETA_CONTINUA.md)
- [Roadmap](docs/ROADMAP.md)
- [Referências técnicas](docs/REFERENCIAS_OPEN_SOURCE.md)
- [Abertura e reutilização](docs/ABERTURA_E_REUTILIZACAO.md)

## Licenciamento

Código próprio sob [MIT](LICENSE). Dados estruturados originais elegíveis sob [CC0 1.0](data/README.md). Conteúdo de terceiros mantém seus próprios direitos e condições.

A consulta é pública, sem cadastro. O projeto não tem vínculo institucional com candidatos, partidos ou veículos de checagem.
