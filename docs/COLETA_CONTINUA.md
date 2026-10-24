# Coleta contínua — implementação inicial

A cada seis horas, o GitHub Actions executa `scripts/coletar.py` sobre as três URLs habilitadas em `data/monitoramento/fontes.json`.

**Importante:** isto é um monitor de alterações de páginas específicas, não um descobridor de todos os artigos novos. Não extrai afirmações individuais, não faz checagem de fatos e não publica vereditos. As URLs ainda precisam ser validadas por execuções reais.

O coletor consulta `robots.txt`, limita tamanho da resposta e armazena apenas URL, título, datas disponíveis e impressão digital do HTML. Os resultados são guardados como artefato do workflow para revisão, sem alterar a base pública.

A próxima evolução é acrescentar descoberta via RSS, sitemaps e JSON-LD `ClaimReview`, com deduplicação e revisão editorial. Sites que proíbem coleta automática devem ser excluídos.

O dashboard continua lendo exclusivamente `data/publicados.json`, que só pode conter registros aprovados.
