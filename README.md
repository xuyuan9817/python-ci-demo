# Python CI Demo

Python 项目 CI/CD 流水线演示

## 流水线状态

![CI](https://github.com/xuyuan9817/python-ci-demo/actions/workflows/ci.yml/badge.svg)

## 7步流水线

| 步骤 | 工具 | 说明 |
|------|------|------|
| 构建 | pip, compileall | 语法验证+依赖安装 |
| 测试 | pytest, pytest-cov | 单元测试+覆盖率 |
| 质量 | flake8, black, SonarQube | 代码规范+类型检查 |
| 安全 | bandit, safety, pip-audit | 漏洞扫描 |
| 打包 | python-build | Wheel包构建 |
| 部署 | GitHub Actions | 自动部署到测试环境 |
| 通知 | GitHub Summary | 报告汇总+告警 |

## 配置说明

### GitHub Secrets
Settings - Secrets and Variables - Actions:

| Secret | 值 |
|--------|-----|
| SONAR_TOKEN | SonarCloud Token |
| SONAR_HOST_URL | https://sonarcloud.io |

### SonarCloud配置
1. https://sonarcloud.io 用GitHub账号登录
2. 创建组织 -> 创建项目 -> 选择 python-ci-demo
3. 生成Token并填入 GitHub Secret

## 项目结构
```
python-ci-demo/
├── .github/workflows/ci.yml
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── sonar-project.properties
├── requirements.txt
└── README.md
```
