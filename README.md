# 财务报表数据服务 (Finance Reports MCP)

这是一个基于MCP架构的财务报表数据服务，提供公司财务报表数据的查询接口。服务直接连接实际API获取数据。

## 功能特点

- 获取公司列表
- 获取指定公司的报表名称列表
- 获取指定公司和报表的详细数据

## 实际API

服务使用部署在 http://97.74.94.7:3202 的API获取数据，包括：
- 获取公司列表：`/api/get_report_company_list`
- 获取报表名称列表：`/api/get_report_name_list?company=公司名称`
- 获取报表数据：`/api/get_report_data_list?company=公司名称&name=指标名称`

## 安装与配置

1. 克隆本仓库
2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 配置：编辑 `mcp.json` 文件，根据需要修改主机和端口设置

## 启动服务

```bash
python main.py
```

## API接口

服务提供以下API接口：

### 1. 获取公司列表

- **URL**: `/api/get_report_company_list`
- **方法**: `GET`
- **参数**: 无
- **返回示例**:
  ```json
  {
    "code": 200,
    "message": "success",
    "data": ["网易-HK9999"]
  }
  ```

### 2. 获取报表名称列表

- **URL**: `/api/get_report_name_list`
- **方法**: `GET`
- **参数**: 
  - `company`: 公司名称
- **返回示例**:
  ```json
  {
    "code": 200,
    "message": "success",
    "data": ["收入报表", "资产负债表"]
  }
  ```

### 3. 获取报表数据

- **URL**: `/api/get_report_data_list`
- **方法**: `GET`
- **参数**: 
  - `company`: 公司名称
  - `name`: 报表名称
- **返回示例**:
  ```json
  {
    "code": 200,
    "message": "success",
    "data": [
      {"年份": "2022", "季度": "Q1", "收入": "1000万", "支出": "800万", "净利润": "200万"},
      {"年份": "2022", "季度": "Q2", "收入": "1200万", "支出": "850万", "净利润": "350万"}
    ]
  }
  ```

## 错误码说明

- 200: 成功
- 400: 请求参数错误
- 404: 资源不存在
- 500: 服务器内部错误

## 许可证

MIT 