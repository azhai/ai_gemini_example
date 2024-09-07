# ai_gemini

首先，我们需要在 [Google Cloud](https://console.cloud.google.com/apis/dashboard) 中创建一个项目，接着在 
[Google AiStudio](https://aistudio.google.com/app/apikey) 中为其创建 Gemini API 密钥。

把密钥、代理写入当前环境中 ，优先级低于代码中的配置
```bash
export GEMINI_API_KEY='AImaSoCuABaA......-...zXaEDeT9'
export http_proxy='http://127.0.0.1:1087'
python3 app.py
```