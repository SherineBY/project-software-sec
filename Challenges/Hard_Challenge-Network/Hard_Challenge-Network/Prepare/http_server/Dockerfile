# 使用指定版本的 Python 镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的 /app 目录
COPY . /app

# 安装 pip 的指定版本
RUN pip install --upgrade pip==22.3.1

# 创建虚拟环境并激活，确保路径正确
RUN python -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# 设置环境变量，确保虚拟环境被正确使用
ENV PATH="/app/venv/bin:$PATH"

# 默认启动命令
CMD ["python", "app.py"]

