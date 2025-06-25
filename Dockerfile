# ---- 第一阶段：构建器 (Builder Stage) ----
# 使用一个标准的Python 3.10 slim镜像作为基础，并给它起个别名 `builder`
FROM python:3.10-slim AS builder

# 设置一些环境变量来配置Poetry，让它在自动化环境中更好地工作
# 告诉Poetry不要问任何交互式问题
ENV POETRY_NO_INTERACTION=1 

# 设置工作目录，后续的命令都会在这个目录下执行
WORKDIR /app

# 只复制项目定义文件，而不是整个项目代码
# 这是为了利用Docker的缓存机制。只要这些文件不变，Docker就不会重新执行下面的安装步骤。
COPY pyproject.toml poetry.lock ./

# 安装Poetry本身，配置Poetry在项目目录内创建.venv，然后安装项目的所有依赖
RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root --only main

# ---- 第二阶段：最终镜像 (Final Stage) ----
# 再次使用轻量的Python镜像作为最终产品的“包装盒”
FROM python:3.10-slim

# 创建一个普通用户`appuser`来运行应用，而不是用有最高权限的`root`用户，这样更安全
RUN useradd --create-home appuser
USER appuser

# 设置新的工作目录
WORKDIR /home/appuser/app

# 从第一阶段(builder)的/app目录中，复制出已经安装好的生产依赖到当前目录
# 这是多阶段构建最关键的一步！
COPY --from=builder /app/.venv ./.venv

# 复制我们自己的应用代码
COPY ./app ./app

# 将虚拟环境的bin目录添加到PATH环境变量中，这样可以直接运行gunicorn等命令
ENV PATH="/home/appuser/app/.venv/bin:$PATH"

# 告诉外界，这个容器内的应用会监听8000端口
EXPOSE 8000

# 容器启动时要执行的默认命令：
# 使用 gunicorn 服务器来启动我们的应用 (app.main 文件里的 app 对象)
# --bind 0.0.0.0:8000 表示监听所有网络接口的8000端口
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.main:app"]
