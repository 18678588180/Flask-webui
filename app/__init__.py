from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 注册蓝图
    from app.routes.main import main_bp
    # from app.routes.api import api_bp
    
    app.register_blueprint(main_bp)
    # app.register_blueprint(api_bp, url_prefix='/api')
    
    return app 