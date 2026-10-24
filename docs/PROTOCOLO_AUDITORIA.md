# Protocolo editorial — edição eleitoral de 24/10/2026

## Unidade de análise
Uma **afirmação verificável individual**, proferida por candidato em evento identificado. A mesma afirmação checada por três veículos deve permanecer **uma afirmação**, com três análises de fontes. Uma reportagem pode conter várias afirmações. Uma fala pode conter várias proposições.

## Campos do dossiê
- `claim_id`: identificador estável.
- `debate`: Globo 23/10/2026 ou Band 18/10/2026.
- `candidato`: pessoa que proferiu a frase, sem inferir intenção.
- `trecho_literal`: fala exata, ou null.
- `parafrase`: resumo, explicitamente marcado como paráfrase.
- `tempo_video`: link com marca temporal, ou null.
- `checagens`: lista de URLs, veículo, data, veredito literal, trecho de justificativa reescrito.
- `fontes_primarias`: links a dados/documentos originais.
- `conclusao_auditoria`: parecer sustentado em evidências, não simples voto majoritário.
- `status`: pendente, em_revisao, aprovado, rejeitado.
- `revisor`: identificador de revisão, quando houver.
- `revisado_em`: data da revisão, quando houver.
- `limites`: pontos não confirmados e divergências.

## Critérios de auditoria
1. **Identidade:** confirmar candidato, debate, dia e a frase. Não atribuir frase de terceiro.
2. **Escopo:** distinguir dado bruto, percentual, período, unidade, população e comparação.
3. **Fontes:** priorizar evidência primária (TSE, IBGE, BC, TCU, Tesouro etc.), com referência específica e data.
4. **Veredito:** preservar rótulo literal de cada veículo; não criar equivalências automáticas.
5. **Conflito:** registrar divergências e causas possíveis (recortes, períodos, definições).
6. **Revisão:** aprovação humana explícita antes de publicar. O Work prepara o dossiê, não se autoaprova.
7. **Correção:** corrigir mantendo histórico e data da alteração.

## Metodologia estatística
Exibir contagem de afirmações **selecionadas e verificadas**, não de todas as falas do debate. Sempre informar N por evento, candidato e fonte. Evitar comparar proporções quando os critérios de seleção diferem. Uma mesma frase checada por várias fontes não aumenta o N de afirmações únicas.

## Política de encerramento
Se o prazo não permitir checar a frase e a evidência, publicar **somente o link original** no guia de fontes, sem transformar o item em veredito do Contraprova.
