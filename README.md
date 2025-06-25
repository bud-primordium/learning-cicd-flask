# 学习现代CI/CD与Flask (`learning-cicd-flask`)

[![CI/CD Pipeline Status](https://github.com/bud-primordium/learning-cicd-flask/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/bud-primordium/learning-cicd-flask/actions)
[![codecov](https://codecov.io/github/bud-primordium/learning-cicd-flask/graph/badge.svg?token=GF3D0FKDU9)](https://codecov.io/github/bud-primordium/learning-cicd-flask)

一个用于学习和演示如何为Python Flask项目搭建现代化CI/CD流水线的项目。

---

## ✨ 项目特点

* **依赖管理**: 使用 [Poetry](https://python-poetry.org/) 进行精确、可复现的依赖管理。
* **Web框架**: 一个简单的 [Flask](https://flask.palletsprojects.com/) 应用作为示例。
* **自动化CI/CD**: 使用 [GitHub Actions](https://github.com/features/actions) 搭建了完整的自动化流水线。
* **全面的代码质量检查**:
  * 格式化检查: `black`
  * 风格与错误检查: `flake8`
  * 静态类型检查: `mypy`
* **自动化测试**: 使用 `pytest` 编写单元测试，并用 `pytest-cov` 生成测试覆盖率报告，通过 [Codecov](https://about.codecov.io/) 进行可视化。
* **容器化**: 提供了一个优化的、多阶段构建的 `Dockerfile`，用于构建轻量、安全的生产镜像。
* **持续交付**: 自动将通过测试的应用构建成Docker镜像，并推送到 [GitHub容器仓库(GHCR)](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)。

## 🚀 开始使用

### 1. 克隆仓库

```bash
git clone https://github.com/bud-primordium/learning-cicd-flask.git
cd learning-cicd-flask
```

### 2. 安装依赖

确保你已经安装了 [Poetry](https://python-poetry.org/docs/#installation)。

```bash
poetry install
```

此命令将创建一个虚拟环境并安装所有生产和开发依赖。

### 3. 激活虚拟环境

```bash
poetry shell
```

## 🛠️ 本地开发

### 运行Web应用

```bash
flask --app app/main run
```

应用将在 `http://127.0.0.1:5000` 上运行。

### 运行测试

```bash
pytest
```

### 运行所有代码质量检查

```bash
# 格式化检查
black --check .

# 风格和错误检查
flake8 .

# 静态类型检查
mypy .
```

---
