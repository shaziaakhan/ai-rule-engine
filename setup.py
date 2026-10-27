from setuptools import setup, find_packages

setup(
    name="ai_rule_agent",
    version="0.1.1",
    author="Shazia Khan",
    author_email="shazia.khan@nihilent.com",
    description="Reusable Business Rule Engine with Azure Semantic Kernel integration",
    packages=find_packages(include=["ai_rule_agent", "ai_rule_agent.*"]),
    install_requires=[
        "PyYAML",
        "fastapi",
        "uvicorn",
        "semantic-kernel>=1.14.0",
        "openai>=1.3.0",
    ],
    extras_require={
        "dev": [
            "black",            # code formatter
            "isort",            # import sorter (PEP8)
            "flake8",           # linting
            "build",            # packaging utilities
            "twine",            # for PyPI uploads
        ],
        "test": [
            "pytest",
            "pytest-asyncio",
            "httpx",            # for API testing
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ],
    },
    classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Libraries"
    ],
    python_requires=">=3.8",
)
