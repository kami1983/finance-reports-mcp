import pytest
from unittest.mock import Mock, patch
from dataclasses import dataclass
from typing import Any, Dict, Optional
from handlers import FinanceReportsHandler

@dataclass
class Request:
    query: Dict[str, str] = None

    def __post_init__(self):
        if self.query is None:
            self.query = {}

@dataclass
class Response:
    status: int = 200
    data: Any = None
    error: Optional[str] = None

@pytest.fixture
def config():
    return {
        "settings": {
            "base_url": "http://test-api.example.com",
            "timeout": 30
        }
    }

@pytest.fixture
def handler(config):
    return FinanceReportsHandler(config)

@pytest.mark.asyncio
async def test_get_companies_success(handler, mocker):
    # 模拟API响应
    mock_response = Mock()
    mock_response.json.return_value = ["公司A", "公司B", "公司C"]
    mock_response.raise_for_status.return_value = None
    mocker.patch('requests.get', return_value=mock_response)

    # 创建请求对象
    request = Request()
    
    # 执行测试
    response = await handler.get_companies(request)
    
    # 验证结果
    assert response.status == 200
    assert response.data == ["公司A", "公司B", "公司C"]

@pytest.mark.asyncio
async def test_get_companies_error(handler, mocker):
    # 模拟API错误
    mocker.patch('requests.get', side_effect=Exception("API错误"))

    # 创建请求对象
    request = Request()
    
    # 执行测试
    response = await handler.get_companies(request)
    
    # 验证结果
    assert response.status == 500
    assert "API错误" in response.error

@pytest.mark.asyncio
async def test_get_reports_success(handler, mocker):
    # 模拟API响应
    mock_response = Mock()
    mock_response.json.return_value = ["报表1", "报表2", "报表3"]
    mock_response.raise_for_status.return_value = None
    mocker.patch('requests.get', return_value=mock_response)

    # 创建请求对象
    request = Request(query={"company": "公司A"})
    
    # 执行测试
    response = await handler.get_reports(request)
    
    # 验证结果
    assert response.status == 200
    assert response.data == ["报表1", "报表2", "报表3"]

@pytest.mark.asyncio
async def test_get_reports_missing_company(handler):
    # 创建请求对象（没有company参数）
    request = Request()
    
    # 执行测试
    response = await handler.get_reports(request)
    
    # 验证结果
    assert response.status == 400
    assert "Company parameter is required" in response.error

@pytest.mark.asyncio
async def test_get_report_data_success(handler, mocker):
    # 模拟API响应
    mock_response = Mock()
    mock_response.json.return_value = {
        "data": [
            {"id": 1, "value": 100},
            {"id": 2, "value": 200}
        ]
    }
    mock_response.raise_for_status.return_value = None
    mocker.patch('requests.get', return_value=mock_response)

    # 创建请求对象
    request = Request(query={
        "company": "公司A",
        "name": "报表1"
    })
    
    # 执行测试
    response = await handler.get_report_data(request)
    
    # 验证结果
    assert response.status == 200
    assert response.data == {
        "data": [
            {"id": 1, "value": 100},
            {"id": 2, "value": 200}
        ]
    }

@pytest.mark.asyncio
async def test_get_report_data_missing_parameters(handler):
    # 创建请求对象（缺少必要参数）
    request = Request(query={"company": "公司A"})  # 缺少name参数
    
    # 执行测试
    response = await handler.get_report_data(request)
    
    # 验证结果
    assert response.status == 400
    assert "Both company and name parameters are required" in response.error 