# Contrato exato de publicação — referência para o Work

**Leia antes de editar `data/auditoria/registros.json`.** O dossiê de pesquisa (`modelo_dossie.json`) não é o mesmo esquema usado pelo exportador.

## Formato de entrada
`data/auditoria/registros.json` deve ser uma lista JSON. Para cada registro destinado ao dashboard, `scripts/gerar_publicados.py` exige:

- `id`: string única, não vazia.
- `afirmacao`: texto da afirmação.
- `autor`: nome do autor da fala.
- `evento`: nome do debate.
- `data`: data do debate.
- `status`: exatamente `publicado`.
- `demonstrativo`: exatamente `false`.
- `verificacoes`: lista não vazia; cada item com `fonte`, `url` HTTPS, `veredito`, `data`. Se `tipo=automatizada`, deve haver `revisao_humana=true` (booleano JSON literal).
- `revisao`: objeto com `aprovado=true` (booleano JSON literal), `data` e `responsavel` não vazios.

Registros pendentes podem existir na lista com `status` diferente de `publicado`, mas precisam ter `id` único.

## Fluxo
1. Produzir dossiês de pesquisa separadamente, sem inventar campos nem aprovações.
2. Submeter a decisão humana.
3. Converter apenas registros aprovados para o esquema acima.
4. Executar `python scripts/gerar_publicados.py`.
5. Executar `python -m unittest discover -s tests -p 'test_*.py' -v`.
6. Conferir `data/publicados.json`, indicadores, links e rastreabilidade.

**O Work não pode preencher `revisao.aprovado=true` por conta própria.** Quando não houver aprovação humana, deixar o registro pendente e entregar o dossiê para revisão.

Este documento registra o contrato existente do código; não altera a política editorial.

## Fila de pesquisa desta edição

`data/auditoria/dossies.json` guarda os dossiês e as ocorrências. `registros.json` contém somente entradas pendentes com vínculo ao dossiê. A aprovação deve citar o ID e a ocorrência: uma decisão sobre a Band não autoriza automaticamente um julgamento sobre a Globo. O responsável pode usar identificador editorial sem expor nome pessoal no site. Os testes não autenticam quem aprovou; o histórico da decisão humana deve ser preservado no GitHub antes de mudar o estado.
