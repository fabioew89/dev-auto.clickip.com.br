from .auth_routes import auth_bp
from .user_routes import user_bp
from .device_routes import device_bp
from .network_routes import network_bp

__all__ = ['user_bp', 'device_bp', 'network_bp', 'auth_bp']
