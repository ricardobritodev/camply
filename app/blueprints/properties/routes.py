from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.blueprints.properties import properties_bp
from app.extensions import db
from app.models.property import Property
from app.models.favorite import Favorite
from app.forms.property_forms import PropertyForm


@properties_bp.route("/")
def list_properties():
    """Listagem de propriedades com filtros."""
    # TODO: [BACKEND] Implementar filtros:
    #   - city (request.args.get('city'))
    #   - property_type
    #   - price_min / price_max
    #   - check_in / check_out (verificar disponibilidade)
    #   - guests
    #   Usar query builder com .filter() encadeado
    #   Implementar paginação com .paginate(page, per_page=12)

    properties = Property.query.filter_by(status="published").limit(12).all()
    return render_template("properties/list.html", properties=properties)


@properties_bp.route("/<slug>")
def detail(slug: str):
    """Detalhes de uma propriedade."""
    property = Property.query.filter_by(slug=slug, status="published").first_or_404()

    # TODO: [BACKEND] Buscar avaliações paginadas
    # TODO: [BACKEND] Buscar datas bloqueadas para o calendário
    # TODO: [BACKEND] Verificar se current_user favoritou esta propriedade

    return render_template("properties/detail.html", property=property)


@properties_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_property():
    """Criar nova propriedade (somente host/admin)."""
    if not current_user.is_host:
        abort(403)

    form = PropertyForm()

    # TODO: [BACKEND] Implementar criação de propriedade:
    #   1. Validar form
    #   2. Gerar slug único a partir do título (slugify)
    #   3. Salvar imagens no storage
    #   4. Associar amenities selecionadas
    #   5. Redirecionar para detail da propriedade criada

    return render_template("properties/form.html", form=form, action="new")


@properties_bp.route("/<int:property_id>/edit", methods=["GET", "POST"])
@login_required
def edit_property(property_id: int):
    """Editar propriedade existente."""
    property = Property.query.get_or_404(property_id)

    # Apenas o dono ou admin pode editar
    if property.owner_id != current_user.id and not current_user.is_admin:
        abort(403)

    form = PropertyForm(obj=property)

    # TODO: [BACKEND] Pré-popular form com dados existentes
    # TODO: [BACKEND] Lidar com upload de novas imagens e remoção de antigas
    # TODO: [BACKEND] Atualizar slug se título mudar (garantir unicidade)

    return render_template("properties/form.html", form=form, action="edit", property=property)
