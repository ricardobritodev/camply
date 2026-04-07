# 🏡 Camply

Plataforma SaaS de locação de sítios, chácaras, casas de campo e fazendas — inspirada no Airbnb/Booking, focada em propriedades rurais e de lazer brasileiras.

> **Projeto acadêmico em grupo.** Esqueleto inicial pronto para contribuições via Pull Requests.

---

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.11+ · Flask 3.x · Blueprints |
| ORM | SQLAlchemy · Flask-SQLAlchemy |
| Migrations | Flask-Migrate (Alembic) |
| Banco | MySQL (produção) · SQLite (desenvolvimento) |
| Auth | Flask-Login · Werkzeug |
| Forms | Flask-WTF · WTForms · email-validator |
| Frontend | Jinja2 · TailwindCSS (CDN) · Alpine.js |
| Env | python-dotenv |
| Testes | pytest |

---

## Pré-requisitos

- Python 3.11+
- MySQL 8+ (opcional — SQLite funciona sem configuração)
- Git

---

## Setup — macOS

```bash
# 1. Clone o repositório
git clone https://github.com/<org>/camply.git
cd camply

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Edite .env com seu editor favorito (opcional para SQLite)

# 5. Execute as migrations
flask db upgrade

# 6. Popule com dados de desenvolvimento
flask seed

# 7. Inicie o servidor
flask run
# Acesse: http://localhost:5000
```

## Setup — Windows

```powershell
# 1. Clone o repositório
git clone https://github.com/<org>/camply.git
cd camply

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
copy .env.example .env
# Edite .env com Notepad ou VS Code

# 5. Execute as migrations
flask db upgrade

# 6. Popule com dados de desenvolvimento
flask seed

# 7. Inicie o servidor
flask run
# Acesse: http://localhost:5000
```

### Configurando MySQL (opcional)

```bash
# No .env, altere DATABASE_URL:
DATABASE_URL=mysql+pymysql://root:sua_senha@localhost:3306/camply

# Crie o banco no MySQL:
mysql -u root -p -e "CREATE DATABASE camply CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Execute as migrations normalmente:
flask db upgrade
```

---

## Credenciais do Seed

| Role | E-mail | Senha |
|---|---|---|
| Admin | admin@camply.com | admin123 |
| Host | carlos@host.com | host123 |
| Guest | ana@guest.com | guest123 |

---

## Comandos úteis

```bash
# Migrations
flask db migrate -m "descrição da mudança"   # gera nova migration
flask db upgrade                              # aplica migrations
flask db downgrade                            # reverte última migration

# Seed
flask seed                  # popula sem apagar dados
flask seed --reset          # apaga tudo e repopula

# Testes
pytest                      # roda todos os testes
pytest -v                   # modo verbose
pytest tests/test_smoke.py  # roda apenas smoke tests

# Formatar código
black app/ seeds/ tests/
```

---

## Estrutura de pastas

```
camply/
├── app/
│   ├── __init__.py              # Application factory
│   ├── extensions.py            # db, login_manager, migrate, csrf
│   ├── config.py                # Config Dev/Prod/Test
│   ├── models/                  # SQLAlchemy models (100% implementados)
│   │   ├── user.py              # User (autenticação + roles)
│   │   ├── property.py          # Property (anúncio)
│   │   ├── property_image.py    # Fotos da propriedade
│   │   ├── amenity.py           # Comodidades (N:N com Property)
│   │   ├── booking.py           # Reserva
│   │   ├── payment.py           # Pagamento
│   │   ├── review.py            # Avaliação (com event hooks)
│   │   ├── favorite.py          # Favoritos
│   │   └── message.py           # Mensagens host ↔ guest
│   ├── blueprints/              # Rotas organizadas por domínio
│   │   ├── auth/                # /auth/login, /auth/register, /auth/logout
│   │   ├── main/                # /, /sobre
│   │   ├── properties/          # /properties, /properties/<slug>
│   │   ├── bookings/            # /bookings, /bookings/me
│   │   ├── reviews/             # /reviews (POST)
│   │   ├── messages/            # /messages
│   │   └── admin/               # /admin (protegido)
│   ├── forms/                   # WTForms (stubs com TODOs)
│   ├── templates/               # Jinja2 + Tailwind (layout completo)
│   └── static/                  # CSS, JS, imagens
├── migrations/                  # Alembic migrations
├── tests/
│   └── test_smoke.py            # Smoke tests (estrutura + 7 testes)
├── seeds/
│   └── seed.py                  # 1 admin + 3 hosts + 5 guests + 8 propriedades
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
├── TODO.md                      # 35 tarefas divididas em BACKEND e FRONTEND
└── CONTRIBUTING.md              # Fluxo de contribuição + Conventional Commits
```

---

## Diagrama ER (simplificado)

```
users ──────────────────────────────────────────┐
  │ id, name, email, password_hash              │
  │ role: admin|host|guest                      │
  │                                             │
  │ 1:N                  1:N (sent/received)    │
  ▼                      ▼                      │
properties          messages                    │
  │ id, owner_id FK      sender_id FK           │
  │ title, slug          receiver_id FK         │
  │ property_type        property_id FK         │
  │ city, state          booking_id FK          │
  │ price_per_night                             │
  │ status: draft|published|suspended           │
  │ avg_rating, reviews_count                   │
  │                                             │
  ├── 1:N ──► property_images                   │
  │            id, url, is_cover, position      │
  │                                             │
  ├── N:N ──► amenities (via property_amenities)│
  │            id, name, icon, category         │
  │                                             │
  ├── 1:N ──► bookings ◄──────────────── users  │
  │            id, property_id FK, guest_id FK  │
  │            check_in, check_out, status      │
  │            total_price                      │
  │            │                                │
  │            ├── 1:1 ──► payments             │
  │            │            amount, method      │
  │            │            status: pending|paid│
  │            │                                │
  │            └── 1:1 ──► reviews ─────────────┘
  │                         rating (1-5)
  │                         comment
  │                         host_reply
  │
  └── 1:N ──► favorites (user_id PK, property_id PK)
```

---

## Como contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o guia completo.

**Resumo:**
1. Fork o repositório
2. Crie uma branch: `git checkout -b feature/minha-funcionalidade`
3. Veja o [TODO.md](TODO.md) para tarefas disponíveis
4. Commit com Conventional Commits: `feat(auth): implementa login`
5. Abra um Pull Request com o template

---

## Licença

MIT © Camply — Projeto acadêmico
