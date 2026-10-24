# CONTRAPROVA — Instruções operacionais para ChatGPT Work

**Prazo editorial:** 24 de outubro de 2026. Segundo turno em 25/10/2026.
**Missão:** finalizar um recorte auditável dos debates Globo (23/10) e Band (18/10) antes da votação.
**Não expandir a infraestrutura sem necessidade.** Priorizar registros reais, links verificáveis, revisão e visualização.

## Comece aqui
1. Ler `docs/STATUS_ENTREGA_2026-10-24.md`, `docs/POLITICA_PUBLICACAO.md` e `docs/PROTOCOLO_AUDITORIA.md`.
2. Verificar estado do GitHub Actions, páginas públicas e `data/publicados.json`.
3. Validar URLs da lista `data/auditoria/fontes_prioritarias.json` em navegador. **Nunca assumir que um link está correto só porque consta no repositório.**
4. Coletar até 30 afirmações distintas, priorizando 15 Globo e 15 Band, ou menos caso o material não permita auditoria suficiente.
5. Preencher `data/auditoria/registros.json` segundo o contrato do exportador e documentação; usar o modelo de dossiê `data/auditoria/modelo_dossie.json`.
6. Confrontar cada checagem com fonte primária, fala original e data quando possível. Guardar URLs exatas e indicar lacunas.
7. Publicar apenas registros efetivamente aprovados por revisão humana. Se o Work não obtiver essa aprovação, **preparar dossiês e deixar status pendente**, sem forçar publicação.
8. Executar testes, validar JSON, gerar `data/publicados.json` apenas quando autorizado, registrar alterações no changelog e entregar relatório com pendências.

## Limites
- Não criar vereditos próprios sem documentação de evidências.
- Não somar classificações heterogêneas entre agências como se fossem equivalentes.
- Não contar republicações sindicadas como fontes independentes.
- Não inferir uma taxa de mentira de candidato a partir da amostra selecionada pelos checadores.
- Não publicar amostras fictícias ou resultados automatizados como auditados.
- Não remover avisos de limitações do dashboard.
- Não criar contas nem exigir identificação do público.
- Não divulgar a identidade pessoal do idealizador no site.
- Não fazer deploy sem verificar CI e integridade dos dados.

## Critérios de entrega
- Fonte original abre e corresponde à afirmação.
- Data e debate identificados.
- Trecho da fala reproduzido fielmente ou marcado como paráfrase.
- Classificação original atribuída ao veículo.
- Evidência primária e justificativa verificáveis.
- Decisão de auditoria e responsável editorial documentados.
- Duplicatas identificadas.
- Cada indicador informa o denominador e a cobertura.
- README, STATUS e CHANGELOG atualizados no mesmo conjunto de mudanças.

## Fluxo rápido
`fontes.html` é o índice público inicial; `index.html` é o painel auditado. Não confundir.
A coleta automatizada e os parsers RSS/ClaimReview são auxiliares e **não** substituem a revisão humana.
