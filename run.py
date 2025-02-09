from app import create_app
from flask_caching import Cache
from flask_talisman import Talisman
from flask import render_template

# 使用 create_app() 创建 Flask 实例
app = create_app()

# 配置缓存
cache = Cache(app, config={
    'CACHE_TYPE': 'simple'  # 或使用 redis
})

# "123456"


# 定义首页路由
@app.route('/')
def index():
    return render_template('app/templates/index.html')



# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
