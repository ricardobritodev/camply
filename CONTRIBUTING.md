# Contributing — Camply

Obrigado por contribuir com o Camply! Siga este guia para garantir um fluxo de trabalho organizado e revisões de código eficientes.

---

## Fluxo de trabalho

### 1. Fork & Clone
```bash
# Faça um fork pelo GitHub, depois:
git clone https://github.com/<seu-usuario>/camply.git
cd camply
git remote add upstream https://github.com/<org>/camply.git
```

### 2. Criar branch
Use o padrão abaixo, sempre a partir de `main`:
```bash
git checkout main
git pull upstream main
git checkout -b feature/nome-da-funcionalidade
# ou
git checkout -b fix/descricao-do-bug
```

**Prefixos de branch:**
| Prefixo | Uso |
|---|---|
| `feature/*` | Nova funcionalidade |
| `fix/*` | Correção de bug |
| `docs/*` | Documentação |
| `refactor/*` | Refatoração sem mudança de comportamento |
| `test/*` | Adição/melhoria de testes |
| `chore/*` | Tarefas de manutenção (deps, config) |

### 3. Desenvolver
- Siga as convenções de código do projeto (ver abaixo)
- Execute os testes antes de commitar: `pytest`
- Verifique se a aplicação ainda roda: `flask run`

### 4. Commitar
Usamos **Conventional Commits**:

```
<tipo>(<escopo opcional>): <descrição curta em português>

[corpo opcional: contexto, motivação, detalhes]

[rodapé opcional: BREAKING CHANGE, closes #issue]
```

**Tipos:**
| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Apenas documentação |
| `style` | Formatação, sem lógica |
| `refactor` | Refatoração |
| `test` | Testes |
| `chore` | Build, dependências |

**Exemplos:**
```bash
git commit -m "feat(auth): implementa lógica de login com flask-login"
git commit -m "fix(booking): corrige cálculo de noites em reservas de fim de semana"
git commit -m "feat(properties): adiciona filtro de preço máximo na listagem"
git commit -m "docs(readme): atualiza instruções de setup para Windows"
```

### 5. Push & Pull Request
```bash
git push origin feature/nome-da-funcionalidade
```

Abra o PR pelo GitHub e preencha o template abaixo.

---

## Template de Pull Request

```markdown
## O que este PR faz?
<!-- Descrição clara e concisa da mudança -->

## Tipo de mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Refatoração
- [ ] Documentação

## Como testar?
<!-- Passo a passo para revisor reproduzir e testar -->
1. `flask run`
2. Acesse `/rota`
3. Verifique que...

## Checklist
- [ ] Código segue as convenções do projeto
- [ ] Testes passam (`pytest`)
- [ ] Não quebra funcionalidades existentes
- [ ] Adicionei/atualizei testes se necessário
- [ ] Atualizei o TODO.md se fechar algum item

## Issues relacionadas
Closes #XX
```

---

## Convenções de código

### Python
- **PEP 8** — use `black` para formatação automática: `black app/`
- **Type hints** em funções novas
- **Docstrings** em funções complexas
- Nomes em inglês para código, português para comentários explicativos
- Evite `SELECT *` — use queries específicas com SQLAlchemy

### Jinja2 / HTML
- Indentação de 2 espaços
- Use `{% include %}` para componentes reutilizáveis
- Prefixe partials com `_` (ex: `_card.html`)

### CSS (Tailwind)
- Mobile-first: comece sem prefixo, adicione `md:` e `lg:` para telas maiores
- Prefira classes utilitárias a CSS customizado
- Para animações simples, use Alpine.js em vez de CSS puro

---

## Estrutura de pastas (resumo)
```
app/blueprints/<nome>/routes.py  ← lógica de rotas (backend)
app/templates/<nome>/            ← templates Jinja2 (frontend)
app/models/<nome>.py             ← model SQLAlchemy
app/forms/<nome>_forms.py        ← formulário WTForms
tests/                           ← testes pytest
```

---

## Dúvidas?
Abra uma **Issue** no GitHub ou entre em contato com o time pelo grupo do projeto.
