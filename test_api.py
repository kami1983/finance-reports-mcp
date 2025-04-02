import unittest
import json
from api import app

class TestFinanceReportAPI(unittest.TestCase):
    """财务报表API测试类"""
    
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
    
    def test_get_report_company_list(self):
        """测试获取公司列表API"""
        response = self.client.get('/api/get_report_company_list')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 200)
        self.assertEqual(data["message"], "success")
        self.assertIsNotNone(data["data"])
        self.assertIsInstance(data["data"], list)
        self.assertTrue(len(data["data"]) > 0)
    
    def test_get_report_name_list_valid(self):
        """测试有效参数获取报表名称列表API"""
        response = self.client.get('/api/get_report_name_list?company=公司A')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 200)
        self.assertEqual(data["message"], "success")
        self.assertIsNotNone(data["data"])
        self.assertIsInstance(data["data"], list)
        self.assertTrue(len(data["data"]) > 0)
    
    def test_get_report_name_list_missing_param(self):
        """测试缺少参数获取报表名称列表API"""
        response = self.client.get('/api/get_report_name_list')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 400)
        self.assertIn("缺少必要参数", data["message"])
        self.assertIsNone(data["data"])
    
    def test_get_report_name_list_invalid(self):
        """测试无效参数获取报表名称列表API"""
        response = self.client.get('/api/get_report_name_list?company=不存在的公司')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 404)
        self.assertIn("不存在", data["message"])
        self.assertIsNone(data["data"])
    
    def test_get_report_data_list_valid(self):
        """测试有效参数获取报表数据API"""
        response = self.client.get('/api/get_report_data_list?company=公司A&name=收入报表')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 200)
        self.assertEqual(data["message"], "success")
        self.assertIsNotNone(data["data"])
        self.assertIsInstance(data["data"], list)
        self.assertTrue(len(data["data"]) > 0)
    
    def test_get_report_data_list_missing_company(self):
        """测试缺少公司参数获取报表数据API"""
        response = self.client.get('/api/get_report_data_list?name=收入报表')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 400)
        self.assertIn("缺少必要参数", data["message"])
        self.assertIsNone(data["data"])
    
    def test_get_report_data_list_missing_name(self):
        """测试缺少报表名称参数获取报表数据API"""
        response = self.client.get('/api/get_report_data_list?company=公司A')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 400)
        self.assertIn("缺少必要参数", data["message"])
        self.assertIsNone(data["data"])
    
    def test_get_report_data_list_invalid_company(self):
        """测试无效公司参数获取报表数据API"""
        response = self.client.get('/api/get_report_data_list?company=不存在的公司&name=收入报表')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 404)
        self.assertIn("不存在", data["message"])
        self.assertIsNone(data["data"])
    
    def test_get_report_data_list_invalid_name(self):
        """测试无效报表名称参数获取报表数据API"""
        response = self.client.get('/api/get_report_data_list?company=公司A&name=不存在的报表')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data["code"], 404)
        self.assertIn("不存在", data["message"])
        self.assertIsNone(data["data"])

if __name__ == "__main__":
    unittest.main() 