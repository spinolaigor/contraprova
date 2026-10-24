# Contraprova — fechamento eleitoral de 24/10/2026

## Resultado editorial desta entrega

- **18 afirmações únicas**, em **21 ocorrências**: 12 na Globo e 9 na Band. Três afirmações aparecem nos dois eventos (CP-005, CP-007, CP-008).
- Cinco artigos originais consultados, de três verificadores: Aos Fatos, Agência Lupa e UOL Confere. Folha/Lupa e UOL AMP abrem, mas não contam como verificadores adicionais.
- Nove dossiês com ao menos um documento primário relevante legível; nove com lacunas adicionais. Isso não mede verdade nem representa auditoria concluída.
- **18 pendentes de revisão, zero aprovados, zero vereditos no dashboard.**
- Todas as frases são paráfrases; a conferência audiovisual e a minutagem permanecem pendentes. Não foram inventadas transcrições.

[Dossiês para revisão humana](https://github.com/spinolaigor/contraprova/blob/main/docs/DOSSIES_REVISAO_2026-10-24.md) · [Relatório de entrega](RELATORIO_ENTREGA_2026-10-24.md).

## Estado técnico comprovado

Base da sessão: `506735e2fe41eaad2a7f3e7976f47c76d12556f5`, branch `main`.

- O deploy inicial observado foi concluído com sucesso: [run 40105523532](https://github.com/spinolaigor/contraprova/actions/runs/40105523532). A página e a base vazia foram confirmadas no navegador.
- Foram inspecionadas as 22 execuções disponíveis: 12 do Pages, 7 de qualidade e 3 de base pública. Não havia execução do monitor de fontes; funcionamento dele em fontes reais não foi comprovado.
- Workflows de qualidade e base pública tinham execuções anteriores bem-sucedidas. O Pages não dependia deles; corrigido com job de validação obrigatório no mesmo workflow.
- O gatilho do Pages agora inclui `fontes.html`, pesquisa, scripts e testes. O artefato contém uma lista explícita de arquivos públicos, sem a fila `data/auditoria/` nem o documento dos dossiês.
- A fila continua pública e versionada no GitHub. Separação do artefato não é controle de privacidade.
- A geração local preservou `data/publicados.json` sem alterações: total zero.
- 18 testes Python passaram; JSON, sintaxe JavaScript e links locais do pacote conferidos.
- Prévia local no navegador remoto indisponível: a conexão a localhost respondeu exigência de token, não o site. A verificação visual da nova versão deve usar o endereço publicado após o deploy.
- QA publicada: dashboard e guia abriram após deploy, navegação painel → guia conferida e estado zero confirmado. Layout desktop inspecionado por captura visual. A tentativa de teste por zoom não alterou o viewport; não foi contada como QA mobile.
- Limite de QA mobile: CSS responsivo e grades estreitas revisados; não houve teste em aparelho físico nem emulação de viewport nesta sessão.

## Pesquisa e limites

Ver `data/auditoria/fontes_consultadas.json`: cada URL tem estado de acesso, localizador e observação. Um HTTP bem-sucedido ou uma página vazia não confirmam seus dados. Resultados de busca são identificados como tal.

Acesso parcial ou falho: tabelas do TCU e BC; abertura de releases IBGE e tabela MDIC; PDF integral VIGISAN por tamanho; notícia original Wi-Fi por login; votação nominal Alerj não recuperada. Os estados foram registrados sem afirmar que as fontes não existem.

Diferenças de categorias foram preservadas por veículo e ocorrência. Detectadas referências que exigem revisão: competência do painel TCU; data do PDF Focus citado pelo UOL; unidade monetária no item exportações; contagem de votantes da Alerj; versões históricas do PIB. Não foi produzido consenso artificial.

## Encerramento

Congelada a expansão de funcionalidades. O guia de fontes é a entrega pública utilizável agora. O dashboard permanece sem vereditos até decisão humana explícita por ID e ocorrência. Não há autorização editorial inferida da aprovação de código ou de um deploy.

## Validação remota da edição 0.7.0

Commit de implementação: [`74aa1e2bb2ddf73e6531463fbf23c8b73b89454c`](https://github.com/spinolaigor/contraprova/commit/74aa1e2bb2ddf73e6531463fbf23c8b73b89454c).

- [Qualidade do projeto — sucesso](https://github.com/spinolaigor/contraprova/actions/runs/40107063761).
- [Validar base pública — sucesso](https://github.com/spinolaigor/contraprova/actions/runs/40107063706).
- [Pages, validação e publicação — sucesso](https://github.com/spinolaigor/contraprova/actions/runs/40107063710).
- A árvore enviada (`171e43d255d93e8f10e0e1d45dbe916d2cc24981`) é idêntica à árvore testada localmente.
- Site atualizado e guia confirmados no navegador após deploy. Base pública continua com total zero. Este adendo registra a execução já observada; alterações posteriores de documentação passam novamente pelo workflow Pages.
