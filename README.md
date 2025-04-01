# Finance Reports MCP Service

这是一个用于提供报表数据服务的MCP项目。该服务通过HTTP接口获取报表数据，并提供以下API端点：

## API 端点

1. 获取公司列表
   - 路径: `/api/companies`
   - 方法: GET
   - 描述: 获取所有可用的公司列表

2. 获取报表名称列表
   - 路径: `/api/reports`
   - 方法: GET
   - 参数: 
     - company: 公司名称
   - 描述: 获取指定公司的所有报表名称

3. 获取具体报表数据
   - 路径: `/api/report-data`
   - 方法: GET
   - 参数:
     - company: 公司名称
     - name: 报表名称
   - 描述: 获取指定公司和报表的具体数据

## 配置

在 `config.yaml` 文件中配置以下内容：

- base_url: API的基础URL
- timeout: 请求超时时间（秒）

## 安装和运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行服务：
```bash
mcp run
```

服务将在配置的端口（默认8080）上启动。 