# Relatório de entrega — Contraprova, 24/10/2026

## Entregue

Pesquisa estruturada de 18 afirmações distintas, com cinco artigos originais, classificação literal quando recuperada, autorias, datas, evidências, divergências e limitações. [Leia os dossiês](https://github.com/spinolaigor/contraprova/blob/main/docs/DOSSIES_REVISAO_2026-10-24.md). Dados em `data/auditoria/dossies.json`; catálogo e acesso em `fontes_consultadas.json`. As entradas correspondentes em `registros.json` permanecem `em_auditoria`, com `revisao.aprovado=false`.

| Recorte | Afirmações selecionadas presentes no evento |
|---|---:|
| Globo, 23/10 | 12 |
| Band, 18/10 | 9 |
| União, sem repetir CP-005/007/008 | 18 |

Os números descrevem cobertura da pesquisa, não desempenho ou taxa de veracidade. As amostras de veículos são intencionais e seus critérios não foram combinados.

## Fila concreta de revisão

**Primeiro lote: documentação primária legível, ainda com limites — 9 IDs:** CP-003, CP-004, CP-005, CP-006, CP-009, CP-010, CP-014, CP-017 e CP-018.

**Segundo lote: complementar evidência antes de conclusão — 9 IDs:** CP-001 e CP-002 (extrair painel TCU com data-base); CP-007 (série DBGG do BC); CP-008 e CP-013 (série PIB vigente); CP-011 (tabela MDIC e unidades); CP-012 (origem MCom); CP-015 (ata nominal Alerj); CP-016 (reproduzir soma e filtros de viagens).

**Todos os 18:** conferir fala e contexto no audiovisual original, registrar link/minutagem e decisão humana. Nenhum está pronto para publicação irrestrita. A fila está pronta para essa revisão, com as lacunas documentadas.

## Achados que afetam a decisão

- CP-002: Lupa e UOL adotam rótulos distintos e descrevem competências diferentes para atualização do TCU. Sem extração histórica, não encerrar a auditoria.
- CP-007: rótulo da própria Lupa muda entre Band e Globo; preservar contexto da ocorrência. Não comparar DBGG com apenas dívida federal nem atribuir todo o estoque a um mandato.
- CP-009: PDF Focus de 07/10/2022 tem horizonte até 2025. O link citado pelo UOL como janeiro/2025 abre documento datado de 13/01/2023, que já possui coluna 2026. Não reproduzir a descrição incorreta da referência.
- CP-011: separar valor nominal em dólares, valor em reais e quantidade exportada. A redação consultada do UOL mistura moeda no acumulado/2026; o resumo Aos Fatos usa “volume”.
- CP-015: verificar a contagem nominal, pois fala transcrita e justificativa do Aos Fatos apresentam números diferentes de deputados.

Esses são achados de conferência de referências, não correções atribuídas formalmente pelos veículos. Nenhum foi convertido em veredito próprio.

## Interface e publicação

Mantidos preto, papel, verde ácido, roxo e tipografia brutalista; melhorados tamanhos para telas estreitas, grades, quebra de texto, foco de teclado, salto de navegação, áreas de toque, estado sem dados e alternativa sem JavaScript. O recorte tem data fixa para não continuar dizendo “amanhã” depois da eleição. As páginas têm metadados de compartilhamento.

O guia apresenta cinco links originais com data de consulta. Os links Folha e UOL AMP funcionam, mas foram substituídos no índice principal por origem e URL canônica. Agregadores sem validação individual saíram das chamadas públicas desta edição; as referências históricas não foram apagadas do Git.

O indicador antes chamado “divergências” passou a dizer “afirmações com rótulos distintos”: diferença de rótulo não prova contradição factual. Nenhuma equivalência entre categorias foi criada.

O Pages agora aguarda testes e integridade da base. O artefato não leva a fila de auditoria. O exportador exige booleano JSON literal para aprovação, rejeitando valores como a string `"false"`. Isso impede erros de tipo; **não autentica uma aprovação humana**. A decisão precisa existir no histórico editorial.

## Validação

18 testes passaram, incluindo exclusão de pendentes, vínculos entre fontes/ocorrências, exigência de aprovação explícita e isolamento do pacote Pages. Exportador executado sem alteração da base pública. Todos os JSON foram analisados; sintaxe JavaScript e links internos do pacote passaram. Os três workflows da implementação `74aa1e2` terminaram com sucesso; links no documento de estado. Dashboard e guia atualizados foram conferidos no navegador após o deploy.

QA visual inicial confirmou o site anterior; após o deploy, a nova versão do guia foi inspecionada por captura visual e a navegação a partir do painel foi conferida. A prévia local remota não pôde abrir por exigência de token. CSS mobile revisado; aparelho físico e emulação de viewport não testados. Não interpretar essas verificações como auditoria audiovisual ou editorial concluída.

## Sua decisão necessária

1. Revisar os IDs e as ocorrências escolhidas, incluindo as lacunas. Pode aprovar, rejeitar ou pedir correção individualmente; não é preciso aceitar o lote inteiro.
2. Para autorizar publicação, citar explicitamente os IDs/ocorrências e a decisão editorial. Aprovação de código não publica vereditos.
3. Escolher o identificador editorial de revisão, que pode ser impessoal. Não é necessário colocar nome do idealizador no site.

Até essas decisões, a edição pública entrega o guia de fontes e a política; o dashboard tem zero afirmações aprovadas. Sem cadastro, sem rastreamento adicionado, sem nome pessoal do idealizador no conteúdo do site. MIT e CC0 preservados nos respectivos escopos; textos de terceiros mantêm seus direitos.
