import os
import click
from flask import Flask
from app.config import config
from app.extensions import db, migrate, login_manager, csrf


def create_app(config_name: str | None = None) -> Flask:
    """Application factory — cria e configura a instância do Flask."""
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "development")

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    # Garante que a pasta instance/ existe (necessária para SQLite)
    os.makedirs(app.instance_path, exist_ok=True)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Carrega o user_loader para Flask-Login
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))

    # Importa todos os models (necessário para Flask-Migrate detectar as tabelas)
    from app import models  # noqa: F401

    # Registra blueprints
    from app.blueprints.main import main_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.properties import properties_bp
    from app.blueprints.bookings import bookings_bp
    from app.blueprints.reviews import reviews_bp
    from app.blueprints.messages import messages_bp
    from app.blueprints.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(properties_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(messages_bp)
    app.register_blueprint(admin_bp)

    # Registra o favoritar como rota avulsa no blueprint de propriedades
    _register_favorite_route(app)

    # Registra o comando CLI `flask seed`
    _register_cli_commands(app)

    return app


def _register_favorite_route(app: Flask) -> None:
    """Registra a rota de favoritar/desfavoritar."""
    from flask import jsonify, request, abort
    from flask_login import login_required, current_user
    from app.models.favorite import Favorite

    @app.route("/favorites/toggle/<int:property_id>", methods=["POST"])
    @login_required
    def toggle_favorite(property_id: int):
        """Favoritar ou desfavoritar uma propriedade."""
        # TODO: [BACKEND] Implementar toggle:
        #   favorite = Favorite.query.get((current_user.id, property_id))
        #   if favorite: db.session.delete(favorite)
        #   else: db.session.add(Favorite(user_id=current_user.id, property_id=property_id))
        #   db.session.commit()
        #   Retornar JSON { "favorited": true/false }
        return jsonify({"favorited": False, "message": "TODO: implementar"})


def _register_cli_commands(app: Flask) -> None:
    """Registra comandos customizados do Flask CLI."""

    @app.cli.command("seed")
    @click.option("--reset", is_flag=True, help="Apaga todos os dados antes de popular.")
    def seed_command(reset: bool) -> None:
        """Popula o banco de dados com dados de desenvolvimento."""
        from seeds.seed import run_seed
        run_seed(reset=reset)
