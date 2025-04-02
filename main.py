import os
import json
import service
from api import app

def load_config():
    """
    加载MCP配置文件
    """
    with open('mcp.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    # 加载配置
    config = load_config()
    settings = config.get('settings', {})
    
    # 获取配置中的主机和端口
    host = settings.get('host', 'localhost')
    port = settings.get('port', 8080)
    
    # 配置API基础URL（如果有）
    api_base_url = settings.get('api_base_url')
    if api_base_url:
        service.BASE_URL = api_base_url
        print(f"使用API基础URL: {api_base_url}")
    else:
        print(f"使用默认API基础URL: {service.BASE_URL}")
    
    # 启动服务器
    print(f"启动财务报表数据服务，监听地址: {host}:{port}")
    app.run(host=host, port=port) 