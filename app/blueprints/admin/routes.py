from functools import wraps
from flask import render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.blueprints.admin import admin_bp
from app.models.user import User
from app.models.property import Property
from app.models.booking import Booking


def admin_required(f):
    """Decorator que restringe acesso a administradores."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route("/")
@login_required
@admin_required
def dashboard():
    """Dashboard administrativo com métricas gerais."""
    # TODO: [BACKEND] Calcular métricas reais:
    #   - total_users, total_properties, total_bookings, total_revenue
    #   - Gráfico de reservas por mês (últimos 6 meses)
    #   - Propriedades pendentes de aprovação
    stats = {
        "total_users": User.query.count(),
        "total_properties": Property.query.count(),
        "total_bookings": Booking.query.count(),
        "total_revenue": 0,  # TODO: somar payments com status='paid'
    }
    return render_template("admin/dashboard.html", stats=stats)


@admin_bp.route("/users")
@login_required
@admin_required
def users():
    """Listagem de usuários com filtros."""
    # TODO: [BACKEND] Implementar filtro por role, is_active, busca por nome/email
    # TODO: [BACKEND] Implementar paginação
    all_users = User.query.order_by(User.created_at.desc()).limit(50).all()
    return render_template("admin/users.html", users=all_users)


@admin_bp.route("/properties")
@login_required
@admin_required
def properties():
    """Listagem e moderação de propriedades."""
    # TODO: [BACKEND] Filtrar por status (draft/published/suspended)
    # TODO: [BACKEND] Implementar ação de aprovar/suspender propriedade
    all_properties = Property.query.order_by(Property.created_at.desc()).limit(50).all()
    return render_template("admin/properties.html", properties=all_properties)


@admin_bp.route("/bookings")
@login_required
@admin_required
def bookings():
    """Listagem de reservas."""
    # TODO: [BACKEND] Filtrar por status, período, propriedade
    all_bookings = Booking.query.order_by(Booking.created_at.desc()).limit(50).all()
    return render_template("admin/bookings.html", bookings=all_bookings)
