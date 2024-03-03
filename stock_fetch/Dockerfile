# 将官方 Python 运行时用作父镜像
FROM python:3.7
# 将工作目录设置为 /myapps
WORKDIR /myapps
# 将当前目录内容复制到位于 /myapps 中的容器中
ADD . .
# 安装 requirements.txt 中指定的任何所需软件包
EXPOSE 8000
RUN pip install -r requirements.txt
# 在容器启动时运行 app.py
CMD ["python3", "/myapps/fetch_stock.py"]
