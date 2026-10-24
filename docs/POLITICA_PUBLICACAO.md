# Política de publicação e indicadores — Contraprova

Versão: 0.3 — decisão editorial de 2026-10-24.

## Princípio
**Coletar amplamente; publicar indicadores apenas com registros auditados.** A palavra “verificado” significa que o processo de auditoria foi concluído e documentado, NÃO que a afirmação foi julgada verdadeira.

## Estados
- `descoberto`: referência detectada automaticamente.
- `coletado`: metadados e fonte preservados.
- `em_auditoria`: vínculo com fala original e evidências sendo conferidos.
- `revisado`: auditoria concluída, fontes e método registrados, divergências documentadas.
- `publicado`: elegível para indicadores públicos.
- `corrigido`: publicação alterada com histórico e justificativa.

## Requisitos para entrar no dashboard principal
1. Texto fiel da afirmação, candidato, data e evento.
2. Link direto para checagem jornalística identificada; registrar autor, data e classificação ORIGINAL.
3. Evidências e suas URLs específicas, preferencialmente primárias; registrar lacunas.
4. Identificador único da afirmação e desduplicação de republicações.
5. Divergências entre verificadores preservadas, sem criar consenso artificial.
6. Revisão editorial concluída e data de corte explícita.
7. Distinção entre afirmação falsa, imprecisa, verdadeira, sem provas e não avaliável; respeitar categorias originais.
8. Não converter acusações ou investigações em fatos comprovados.
9. Não interpretar proporções entre falas selecionadas como taxas de mentira de toda a campanha.
10. Revisões posteriores devem ser rastreáveis e recalcular gráficos.

## O que NÃO entra nos totais principais
- Checagens exclusivamente automatizadas sem revisão humana.
- Totais de agregadores sem links para itens e proveniência individual.
- Registros demonstrativos da v0.1–v0.3.
- Afirmações descobertas, mas ainda sem auditoria.
- Contagens duplicadas por republicação.

## Métricas do dashboard
- Número de afirmações únicas auditadas por evento e candidato.
- Distribuição dos vereditos **por fonte**; não somar categorias incompatíveis.
- Cobertura: afirmações coletadas, em auditoria e publicadas (fora do gráfico de vereditos).
- Divergências entre checadores, revisões e evidências primárias.
- Sempre declarar data de corte, escopo, metodologia e denominador.

## Automação
A coleta pode abrir PRs para novos registros e alterações de fontes. Publicação de vereditos e inclusão nos indicadores principais dependem de revisão e testes. O dashboard deve ler exclusivamente um conjunto de dados explicitamente marcado `publicado` / `auditado`, e nunca um arquivo de descobertas.

## Próximos passos técnicos
1. Importar aplicação v0.3 e workflows completos.
2. Introduzir exportador `data/publicados.json` com filtro estrito por estado e testes.
3. Ativar coleta de fontes individualmente validadas, respeitando limites de acesso.
4. Configurar GitHub Pages e testar visualização de dados revisados.
