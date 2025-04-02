from flask import Flask, request, jsonify
import service

app = Flask(__name__)

@app.route('/api/get_report_company_list', methods=['GET'])
def api_get_report_company_list():
    """处理获取公司列表的API请求"""
    result = service.get_report_company_list()
    return jsonify(result)

@app.route('/api/get_report_name_list', methods=['GET'])
def api_get_report_name_list():
    """处理获取报表名称列表的API请求"""
    company = request.args.get('company')
    if not company:
        return jsonify({
            "code": 400,
            "message": "缺少必要参数: company",
            "data": None
        })
    
    result = service.get_report_name_list(company)
    return jsonify(result)

@app.route('/api/get_report_data_list', methods=['GET'])
def api_get_report_data_list():
    """处理获取报表数据的API请求"""
    company = request.args.get('company')
    name = request.args.get('name')
    
    if not company:
        return jsonify({
            "code": 400,
            "message": "缺少必要参数: company",
            "data": None
        })
    
    if not name:
        return jsonify({
            "code": 400,
            "message": "缺少必要参数: name",
            "data": None
        })
    
    result = service.get_report_data_list(company, name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 