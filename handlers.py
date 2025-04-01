import requests
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Request:
    """HTTP请求的数据类
    
    用于模拟HTTP请求对象，包含查询参数等信息
    
    Attributes:
        query: 请求的查询参数字典
    """
    query: Dict[str, str] = None

    def __post_init__(self):
        if self.query is None:
            self.query = {}

@dataclass
class Response:
    """HTTP响应的数据类
    
    用于模拟HTTP响应对象，包含状态码、数据和错误信息
    
    Attributes:
        status: HTTP状态码，默认为200
        data: 响应数据
        error: 错误信息，如果有的话
    """
    status: int = 200
    data: Any = None
    error: Optional[str] = None

class FinanceReportsHandler:
    """财务报表处理器
    
    处理与财务报表相关的HTTP请求，包括获取公司列表、报表名称和报表数据。
    所有数据都通过调用外部API获取。
    
    Attributes:
        base_url: API的基础URL
        timeout: 请求超时时间（秒）
    """

    def __init__(self, config: Dict[str, Any]):
        """初始化处理器
        
        Args:
            config: 配置字典，必须包含 settings.base_url 和 settings.timeout
        """
        self.base_url = config["settings"]["base_url"]
        self.timeout = config["settings"]["timeout"]

    async def get_companies(self, request: Request) -> Response:
        """获取所有可用的公司列表
        
        通过调用外部API获取所有可用的公司列表。
        
        Args:
            request: 请求对象，不需要任何参数
            
        Returns:
            Response: 包含公司列表的响应对象
            
        Raises:
            当API调用失败时，返回500状态码和错误信息
        """
        try:
            response = requests.get(
                f"{self.base_url}/api/get_report_company_list",
                timeout=self.timeout
            )
            response.raise_for_status()
            return Response(data=response.json())
        except Exception as e:
            return Response(status=500, error=str(e))

    async def get_reports(self, request: Request) -> Response:
        """获取指定公司的报表名称列表
        
        通过调用外部API获取指定公司的所有可用报表名称。
        
        Args:
            request: 请求对象，必须包含 company 查询参数
            
        Returns:
            Response: 包含报表名称列表的响应对象
            
        Raises:
            当缺少 company 参数时，返回400状态码
            当API调用失败时，返回500状态码和错误信息
        """
        company = request.query.get("company")
        if not company:
            return Response(status=400, error="Company parameter is required")

        try:
            response = requests.get(
                f"{self.base_url}/api/get_report_name_list",
                params={"company": company},
                timeout=self.timeout
            )
            response.raise_for_status()
            return Response(data=response.json())
        except Exception as e:
            return Response(status=500, error=str(e))

    async def get_report_data(self, request: Request) -> Response:
        """获取指定公司和报表的具体数据
        
        通过调用外部API获取特定公司和报表的详细数据。
        
        Args:
            request: 请求对象，必须包含 company 和 name 查询参数
            
        Returns:
            Response: 包含报表数据的响应对象
            
        Raises:
            当缺少必要参数时，返回400状态码
            当API调用失败时，返回500状态码和错误信息
        """
        company = request.query.get("company")
        report_name = request.query.get("name")

        if not company or not report_name:
            return Response(
                status=400,
                error="Both company and name parameters are required"
            )

        try:
            response = requests.get(
                f"{self.base_url}/api/get_report_data_list",
                params={"company": company, "name": report_name},
                timeout=self.timeout
            )
            response.raise_for_status()
            return Response(data=response.json())
        except Exception as e:
            return Response(status=500, error=str(e)) 