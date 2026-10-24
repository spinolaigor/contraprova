# CONTRAPROVA ■

**Menos ruído. Mais dados.**

Observatório independente de checagens e evidências públicas. O objetivo é reunir informações rastreáveis sobre afirmações verificáveis, sem apresentar dados preliminares como conclusões.

**Site:** https://spinolaigor.github.io/contraprova/

## Como funciona

1. **Monitoramento:** fontes e publicações são acompanhadas em `data/monitoramento/`. O monitoramento inicial observa três URLs específicas e não descobre automaticamente todos os artigos.
2. **Auditoria:** dossiês em `data/auditoria/dossies.json`, catálogo em `fontes_consultadas.json` e fila de publicação em `registros.json`.
3. **Publicação:** `scripts/gerar_publicados.py` exporta somente registros aprovados para `data/publicados.json`.
4. **Dashboard:** `index.html` lê exclusivamente a base publicada; amostras demonstrativas e descobertas não entram nos indicadores.

**Verificado não significa verdadeiro:** significa que a auditoria da afirmação foi concluída. Vereditos originais podem ser verdadeiro, falso, impreciso, sem provas ou divergente, sempre atribuídos às fontes.

## Edição eleitoral · 24/10/2026

- [Guia de fontes públicas](https://spinolaigor.github.io/contraprova/fontes.html): cinco artigos originais consultados, de três verificadores.
- [18 dossiês para revisão](docs/DOSSIES_REVISAO_2026-10-24.md), com 21 ocorrências entre Globo e Band; nenhuma aprovação humana inferida.
- **Base pública: zero vereditos aprovados.** Os dossiês ficam fora dos indicadores e do artefato Pages.
- [Relatório e decisões pendentes](docs/RELATORIO_ENTREGA_2026-10-24.md) · [Estado comprovado](docs/STATUS_ENTREGA_2026-10-24.md).
- RSS/Atom e ClaimReview têm extratores offline testados; não foram integrados à descoberta em produção. O monitor observa URLs fixas e só gera artefatos para revisão.
- O prazo desta edição encerra expansão de funcionalidades. O trabalho restante é editorial, incluindo audiovisual e evidência primária indicada em cada dossiê.

## Executar testes

Requer Python 3.12 ou compatível, sem bibliotecas externas para os módulos atuais:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/gerar_publicados.py
python scripts/preparar_site.py
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
