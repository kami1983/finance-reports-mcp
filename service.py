import os
import json
import requests
from typing import Dict, List, Any, Optional

# 基础URL配置
BASE_URL = "http://97.74.94.7:3202"

def get_report_company_list() -> Dict[str, Any]:
    """
    获取所有可用的公司列表
    
    Returns:
        Dict[str, Any]: 包含公司列表的响应
    """
    try:
        # 调用真实API
        # 注意：这里保持/api前缀，与远程API保持一致
        response = requests.get(f"{BASE_URL}/api/get_report_company_list", timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        # 发生异常时返回错误信息
        return {
            "code": 500,
            "message": f"API调用失败: {str(e)}",
            "data": None
        }

def get_report_name_list(company: str) -> Dict[str, Any]:
    """
    获取指定公司的报表名称列表
    
    Args:
        company (str): 公司名称
        
    Returns:
        Dict[str, Any]: 包含报表名称列表的响应
    """
    try:
        # 调用真实API
        # 注意：这里保持/api前缀，与远程API保持一致
        response = requests.get(f"{BASE_URL}/api/get_report_name_list", params={"company": company}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {
                "code": 404,
                "message": f"公司 '{company}' 不存在",
                "data": None
            }
        return {
            "code": e.response.status_code,
            "message": f"API调用失败: {str(e)}",
            "data": None
        }
    except Exception as e:
        # 发生异常时返回错误信息
        return {
            "code": 500,
            "message": f"API调用失败: {str(e)}",
            "data": None
        }

def get_report_data_list(company: str, name: str) -> Dict[str, Any]:
    """
    获取指定公司和报表的具体数据
    
    Args:
        company (str): 公司名称
        name (str): 报表名称
        
    Returns:
        Dict[str, Any]: 包含报表数据的响应
    """
    try:
        # 调用真实API
        # 注意：这里保持/api前缀，与远程API保持一致
        response = requests.get(
            f"{BASE_URL}/api/get_report_data_list", 
            params={"company": company, "name": name}, 
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {
                "code": 404,
                "message": f"公司 '{company}' 或报表 '{name}' 不存在",
                "data": None
            }
        return {
            "code": e.response.status_code,
            "message": f"API调用失败: {str(e)}",
            "data": None
        }
    except Exception as e:
        # 发生异常时返回错误信息
        return {
            "code": 500,
            "message": f"API调用失败: {str(e)}",
            "data": None
        } 