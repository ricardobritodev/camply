from flask import render_template
from app.blueprints.main import main_bp
from app.models.property import Property


@main_bp.route("/")
def index():
    """Home — hero + busca + propriedades em destaque."""
    # TODO: [BACKEND] Substituir dados mockados por query real:
    #   featured = Property.query.filter_by(status='published')
    #               .order_by(Property.avg_rating.desc()).limit(8).all()
    featured_properties = []  # placeholder — seed populará isso
    return render_template("main/index.html", featured_properties=featured_properties)


@main_bp.route("/sobre")
def about():
    """Página institucional sobre o Camply."""
    # TODO: [FRONTEND] Criar template about.html com conteúdo institucional
    return render_template("main/about.html")
