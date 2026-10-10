# Minha Barsa

## Ver o site no seu computador

Primeira vez (uma só): abra o prompt na pasta do projeto e rode

    python -m pip install -r requirements.txt

Depois, sempre que quiser ver o site: dê dois cliques em `abrir-site.bat`.
Ele abre o navegador sozinho. Para encerrar, feche a janela preta.

A página atualiza sozinha ao salvar um arquivo.

## O menu se monta sozinho

Não precisa mexer no `mkdocs.yml`. O menu segue as pastas dentro de `docs/`:

    docs/
      contabilidade/                 <- área
        index.md                     <- primeira linha: # Contabilidade
        matematica-financeira/       <- disciplina
          index.md                   <- primeira linha: # Matemática Financeira
          juros-compostos.md         <- assunto (primeira linha: # Juros Compostos)

## Adicionar uma disciplina nova

1. Crie uma pasta dentro da área, sem acento e sem espaço (ex.: `auditoria`).
2. Dentro dela, crie um `index.md` cuja primeira linha é o nome bonito:
   `# Auditoria Contábil`
3. Salve. A disciplina aparece no menu.

## Adicionar um assunto novo

1. Copie `modelo-de-topico.md` para a pasta da disciplina.
2. Troque o nome do arquivo (ex.: `papeis-de-trabalho.md`) e escreva.
3. A primeira linha (`# Título`) é o nome que aparece no menu.

## Mudar a ordem no menu

A ordem é alfabética pelo nome do arquivo ou da pasta. Para escolher a ordem,
coloque números na frente: `01-juros-compostos.md`, `02-amortizacao.md`.
O número não aparece no menu. A seta de "próximo" segue a mesma ordem.

## Apagar um assunto

Apague o arquivo. Ele some do menu.

## Data de "Última atualização"

No site publicado no GitHub, cada página mostra a data do último envio
daquele arquivo. No computador, a data mostrada é sempre a de hoje (é só
a pré-visualização).

## Publicar de graça (GitHub Pages)

1. Envie os arquivos para o repositório no GitHub.
2. Crie o arquivo `.github/workflows/deploy.yml` com o conteúdo de
   `github-deploy.yml` (está nesta pasta).
3. Em Settings > Pages, escolha a branch `gh-pages`.
