import unittest
import service

class TestFinanceReportService(unittest.TestCase):
    """财务报表服务测试类"""
    
    def test_get_report_company_list(self):
        """测试获取公司列表"""
        result = service.get_report_company_list()
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIsNotNone(result["data"])
        self.assertIsInstance(result["data"], list)
        self.assertTrue(len(result["data"]) > 0)
    
    def test_get_report_name_list_valid_company(self):
        """测试获取有效公司的报表列表"""
        result = service.get_report_name_list("公司A")
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIsNotNone(result["data"])
        self.assertIsInstance(result["data"], list)
        self.assertTrue(len(result["data"]) > 0)
    
    def test_get_report_name_list_invalid_company(self):
        """测试获取无效公司的报表列表"""
        result = service.get_report_name_list("不存在的公司")
        self.assertEqual(result["code"], 404)
        self.assertIn("不存在", result["message"])
        self.assertIsNone(result["data"])
    
    def test_get_report_data_list_valid(self):
        """测试获取有效公司和报表的数据"""
        result = service.get_report_data_list("公司A", "收入报表")
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIsNotNone(result["data"])
        self.assertIsInstance(result["data"], list)
        self.assertTrue(len(result["data"]) > 0)
    
    def test_get_report_data_list_invalid_company(self):
        """测试获取无效公司的报表数据"""
        result = service.get_report_data_list("不存在的公司", "收入报表")
        self.assertEqual(result["code"], 404)
        self.assertIn("不存在", result["message"])
        self.assertIsNone(result["data"])
    
    def test_get_report_data_list_invalid_report(self):
        """测试获取无效报表的数据"""
        result = service.get_report_data_list("公司A", "不存在的报表")
        self.assertEqual(result["code"], 404)
        self.assertIn("不存在", result["message"])
        self.assertIsNone(result["data"])

if __name__ == "__main__":
    unittest.main() 