# -*- coding: utf-8 -*-

import google.generativeai as genai
import os, random


# 密钥，在环境变量中为 GENEMINI_API_KEY 或 GOOGLE_API_KEY
cfg_api_key = ""
# 代理，在环境变量中为 http_proxy 或 HTTP_PROXY
# 可参考 proxy_info_from_environment 函数
cfg_http_proxy = ""


def init_environ(api_key: str, http_proxy: str = "") -> None:
    """
    初始化环境，使用 API 密钥和 HTTP 代理。

    参数:
    api_key (str): API 密钥字符串。如果为空，将从环境变量中获取。
    http_proxy (str): HTTP 代理服务器地址。如果不为空，将设置为环境变量。
    """
    if api_key == "":
        api_key = os.environ.get("GEMINI_API_KEY", "")
    if http_proxy != "":
        os.environ["http_proxy"] = http_proxy
    genai.configure(api_key=api_key)


class GeminiModel(object):
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        """
        初始化 Gemini 类的实例。

        参数：
        - model_name (str): 生成模型的名称。主要有：
            - gemini-1.5-flash
            - gemini-1.5-pro
            - gemini-1.0-pro
        """
        self.model = genai.GenerativeModel(model_name)

    def get_answer(self, question: str) -> str:
        """
        使用模型获取问题答案。
        """
        response = self.model.generate_content(question)
        return response.text


if __name__ == "__main__":
    questions = [
        "地球上最大的植物是什么？",
        "正念冥想如何进行？",
        "相似度最高的国旗是哪几个国家的？",
        "唐高祖李渊有几个儿子，各自的结局如何？",
        "请向中学生科普一下拓扑学的主要知识。",
    ]
    init_environ(cfg_api_key, cfg_http_proxy)
    gem = GeminiModel("gemini-1.5-flash")
    # 随机选择一个问题
    question = random.choice(questions)
    print(question)
    print(gem.get_answer(question))
