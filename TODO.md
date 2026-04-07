# TODO — Camply

> Prioridades: **P0** = crítico/bloqueante | **P1** = importante | **P2** = melhoria

---

## BACKEND

### P0 — Funcionalidades críticas

- [ ] **[B-01] Lógica de registro de usuário** — Implementar `auth/routes.py::register()` com validação de e-mail duplicado, criação do User e redirect com flash. _Pesquise: "Flask-WTF validate_on_submit"_

- [ ] **[B-02] Lógica de login** — Implementar `auth/routes.py::login()` com busca por e-mail, `check_password()`, `login_user()` e redirect para `next`. _Pesquise: "Flask-Login login_user next parameter"_

- [ ] **[B-03] Criação de reserva** — Implementar `bookings/routes.py::create_booking()`: verificar disponibilidade, calcular valores, criar Booking + Payment. _Pesquise: "SQLAlchemy overlapping date ranges query"_

- [ ] **[B-04] Filtros de propriedades** — Implementar filtros em `properties/routes.py::list_properties()`: cidade, tipo, preço, datas, hóspedes. _Pesquise: "SQLAlchemy dynamic filters"_

### P1 — Funcionalidades importantes

- [ ] **[B-05] Geração de slug** — Implementar geração automática de slug único em `properties/routes.py::new_property()`. _Pesquise: "python-slugify library"_

- [ ] **[B-06] Criar review** — Implementar `reviews/routes.py::create_review()`: validar booking completed, sem review duplicada. _Pesquise: "SQLAlchemy unique constraint check"_

- [ ] **[B-07] Toggle favorito** — Implementar `app/__init__.py::toggle_favorite()` com resposta JSON. _Pesquise: "Flask JSON response jsonify"_

- [ ] **[B-08] Cancelamento de reserva** — Implementar `bookings/routes.py::cancel_booking()`: política de cancelamento, atualizar payment, notificar host.

- [ ] **[B-09] Paginação** — Adicionar paginação em listagens de propriedades, reservas e admin. _Pesquise: "Flask-SQLAlchemy paginate"_

- [ ] **[B-10] Upload de imagens** — Implementar upload de fotos de propriedades. _Pesquise: "Flask file upload Werkzeug secure_filename"_ ou _"Cloudinary Flask integration"_

- [ ] **[B-11] Ações admin** — Implementar publicar/suspender propriedade e desativar/promover usuário no painel admin.

### P2 — Melhorias e extras

- [ ] **[B-12] Verificação de e-mail** — Enviar e-mail de confirmação após cadastro. _Pesquise: "Flask-Mail itsdangerous timed token"_

- [ ] **[B-13] Reset de senha** — Fluxo completo de recuperação de senha por e-mail.

- [ ] **[B-14] Integração de pagamento** — Integrar com Mercado Pago ou Asaas para PIX/cartão. _Pesquise: "Mercado Pago Python SDK"_

- [ ] **[B-15] Webhook de pagamento** — Endpoint para receber notificações do gateway e atualizar status.

- [ ] **[B-16] Geolocalização** — Busca por propriedades próximas usando latitude/longitude. _Pesquise: "SQLAlchemy Haversine formula"_

- [ ] **[B-17] Validações de modelo** — Adicionar `CheckConstraint` nos models (rating 1-5, price >= 0, etc).

- [ ] **[B-18] Testes unitários** — Expandir `tests/test_smoke.py` com testes de models, forms e rotas autenticadas.

- [ ] **[B-19] Disponibilidade de datas** — Retornar datas bloqueadas para o calendário do frontend em JSON.

- [ ] **[B-20] API REST básica** — Criar blueprint `/api/v1` com endpoints JSON para propriedades e disponibilidade (para integração futura com app mobile).

---

## FRONTEND

### P0 — Funcionalidades críticas

- [ ] **[F-01] Formulário de reserva dinâmico** — Calcular total (subtotal + limpeza + serviço) ao alterar datas/hóspedes usando Alpine.js. _Pesquise: "Alpine.js watchers x-effect"_

- [ ] **[F-02] Validação client-side** — Adicionar validação de datas (check_out > check_in) e hóspedes antes de submeter. _Pesquise: "Alpine.js form validation"_

### P1 — Funcionalidades importantes

- [ ] **[F-03] Galeria de fotos** — Implementar lightbox/modal para expandir fotos na página de detalhe. _Pesquise: "Alpine.js image gallery modal"_

- [ ] **[F-04] Seleção de estrelas** — Substituir input numérico por estrelas interativas no formulário de review. _Pesquise: "Alpine.js star rating component"_

- [ ] **[F-05] Mapa interativo** — Integrar Leaflet.js na página de detalhe com pin da propriedade. _Pesquise: "Leaflet.js CDN Flask Jinja2"_

- [ ] **[F-06] Upload com preview** — Adicionar preview de imagens antes do upload no formulário de propriedade. _Pesquise: "Alpine.js file input preview"_

- [ ] **[F-07] Calendário de disponibilidade** — Mostrar datas bloqueadas no card de reserva. _Pesquise: "Flatpickr.js disable dates"_

- [ ] **[F-08] Favoritar com animação** — Animar o botão de favoritar (coração) com Alpine.js e atualizar via fetch. _Pesquise: "Alpine.js fetch toggle"_

- [ ] **[F-09] Filtros com URL params** — Sincronizar estado dos filtros de busca com a URL. _Pesquise: "URLSearchParams JavaScript"_

### P2 — Melhorias e extras

- [ ] **[F-10] Modo escuro** — Adicionar suporte a dark mode com Tailwind + Alpine.js. _Pesquise: "Tailwind CSS dark mode class strategy"_

- [ ] **[F-11] Toast notifications** — Substituir flash messages por toasts animados (Alpine.js). _Pesquise: "Alpine.js toast notification"_

- [ ] **[F-12] Skeleton loading** — Adicionar skeleton screens nas listagens enquanto carrega. _Pesquise: "Tailwind CSS skeleton loading animation"_

- [ ] **[F-13] Página de mensagens** — Criar interface de chat simples para troca de mensagens. _Pesquise: "Flask polling messages"_

- [ ] **[F-14] PWA** — Transformar em Progressive Web App com service worker para uso offline básico.

- [ ] **[F-15] SEO** — Adicionar meta tags Open Graph, Twitter Cards e JSON-LD para propriedades.
