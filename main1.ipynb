{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kuUDjQUVPW1W",
        "outputId": "5c946f02-176a-4b3b-f797-a18aac4f1b9d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rHit:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease\n",
            "\r0% [Connecting to archive.ubuntu.com (91.189.92.24)] [Waiting for headers] [Con\r                                                                               \rHit:2 https://cli.github.com/packages stable InRelease\n",
            "\r0% [Waiting for headers] [Waiting for headers] [Connected to r2u.stat.illinois.\r                                                                               \rHit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease\n",
            "Hit:4 https://r2u.stat.illinois.edu/ubuntu jammy InRelease\n",
            "Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu jammy-updates InRelease\n",
            "Hit:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease\n",
            "Hit:8 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease\n",
            "Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease\n",
            "Reading package lists... Done\n",
            "W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)\n",
            "Reading package lists... Done\n",
            "Building dependency tree... Done\n",
            "Reading state information... Done\n",
            "zstd is already the newest version (1.4.8+dfsg-3build1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.\n",
            ">>> Cleaning up old version at /usr/local/lib/ollama\n",
            ">>> Installing ollama to /usr/local\n",
            ">>> Downloading ollama-linux-amd64.tar.zst\n",
            "######################################################################## 100.0%\n",
            ">>> Adding ollama user to video group...\n",
            ">>> Adding current user to ollama group...\n",
            ">>> Creating ollama systemd service...\n",
            "\u001b[1m\u001b[31mWARNING:\u001b[m systemd is not running\n",
            "\u001b[1m\u001b[31mWARNING:\u001b[m Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.\n",
            ">>> The Ollama API is now available at 127.0.0.1:11434.\n",
            ">>> Install complete. Run \"ollama\" from the command line.\n",
            "\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\n",
            "\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\u001b[?2026h\u001b[?25l\u001b[1G\u001b[?25h\u001b[?2026l\n"
          ]
        }
      ],
      "source": [
        "# 0. Install zstd (required for Ollama installation)\n",
        "!apt-get update && apt-get install -y zstd\n",
        "\n",
        "# 1. Install Ollama\n",
        "!curl -fsSL https://ollama.com/install.sh | sh\n",
        "\n",
        "# 2. Start Ollama server in the background\n",
        "import subprocess\n",
        "import time\n",
        "\n",
        "# Use subprocess to run 'ollama serve' without blocking the cell\n",
        "subprocess.Popen([\"ollama\", \"serve\"])\n",
        "time.sleep(5) # Give it a few seconds to wake up\n",
        "\n",
        "# 3. Pull the models you need\n",
        "!ollama pull llama3\n",
        "!ollama pull nomic-embed-text"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -U langchain-ollama langchain-chroma langchain-core pypdf langchain-community"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PJuh18ASQrq-",
        "outputId": "a0135983-d7f6-4fd6-971d-4ef77543cd5c"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain-ollama in /usr/local/lib/python3.12/dist-packages (1.0.1)\n",
            "Requirement already satisfied: langchain-chroma in /usr/local/lib/python3.12/dist-packages (1.1.0)\n",
            "Requirement already satisfied: langchain-core in /usr/local/lib/python3.12/dist-packages (1.2.7)\n",
            "Requirement already satisfied: pypdf in /usr/local/lib/python3.12/dist-packages (6.6.2)\n",
            "Requirement already satisfied: langchain-community in /usr/local/lib/python3.12/dist-packages (0.4.1)\n",
            "Requirement already satisfied: ollama<1.0.0,>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from langchain-ollama) (0.6.1)\n",
            "Requirement already satisfied: chromadb<2.0.0,>=1.3.5 in /usr/local/lib/python3.12/dist-packages (from langchain-chroma) (1.4.1)\n",
            "Requirement already satisfied: numpy>=1.26.0 in /usr/local/lib/python3.12/dist-packages (from langchain-chroma) (2.0.2)\n",
            "Requirement already satisfied: jsonpatch<2.0.0,>=1.33.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (1.33)\n",
            "Requirement already satisfied: langsmith<1.0.0,>=0.3.45 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (0.6.4)\n",
            "Requirement already satisfied: packaging<26.0.0,>=23.2.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (25.0)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (2.12.3)\n",
            "Requirement already satisfied: pyyaml<7.0.0,>=5.3.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (6.0.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (9.1.2)\n",
            "Requirement already satisfied: typing-extensions<5.0.0,>=4.7.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (4.15.0)\n",
            "Requirement already satisfied: uuid-utils<1.0,>=0.12.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (0.13.0)\n",
            "Requirement already satisfied: langchain-classic<2.0.0,>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (1.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3.0.0,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.0.45)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.32.5 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.32.5)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (3.13.3)\n",
            "Requirement already satisfied: dataclasses-json<0.7.0,>=0.6.7 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (0.6.7)\n",
            "Requirement already satisfied: pydantic-settings<3.0.0,>=2.10.1 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.12.0)\n",
            "Requirement already satisfied: httpx-sse<1.0.0,>=0.4.0 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (0.4.3)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.5.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (2.6.1)\n",
            "Requirement already satisfied: aiosignal>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.4.0)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (25.4.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.8.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (6.7.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (0.4.1)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.22.0)\n",
            "Requirement already satisfied: build>=1.0.3 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.4.0)\n",
            "Requirement already satisfied: pybase64>=1.4.1 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.4.3)\n",
            "Requirement already satisfied: uvicorn>=0.18.3 in /usr/local/lib/python3.12/dist-packages (from uvicorn[standard]>=0.18.3->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.40.0)\n",
            "Requirement already satisfied: posthog<6.0.0,>=2.4.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (5.4.0)\n",
            "Requirement already satisfied: onnxruntime>=1.14.1 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.23.2)\n",
            "Requirement already satisfied: opentelemetry-api>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.39.1)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.39.1)\n",
            "Requirement already satisfied: opentelemetry-sdk>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.39.1)\n",
            "Requirement already satisfied: tokenizers>=0.13.2 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.22.2)\n",
            "Requirement already satisfied: pypika>=0.48.9 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.50.0)\n",
            "Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (4.67.1)\n",
            "Requirement already satisfied: overrides>=7.3.1 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (7.7.0)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (6.5.2)\n",
            "Requirement already satisfied: grpcio>=1.58.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.76.0)\n",
            "Requirement already satisfied: bcrypt>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (5.0.0)\n",
            "Requirement already satisfied: typer>=0.9.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.21.1)\n",
            "Requirement already satisfied: kubernetes>=28.1.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (35.0.0)\n",
            "Requirement already satisfied: mmh3>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (5.2.0)\n",
            "Requirement already satisfied: orjson>=3.9.12 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (3.11.5)\n",
            "Requirement already satisfied: httpx>=0.27.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.28.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (13.9.4)\n",
            "Requirement already satisfied: jsonschema>=4.19.0 in /usr/local/lib/python3.12/dist-packages (from chromadb<2.0.0,>=1.3.5->langchain-chroma) (4.26.0)\n",
            "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /usr/local/lib/python3.12/dist-packages (from dataclasses-json<0.7.0,>=0.6.7->langchain-community) (3.26.2)\n",
            "Requirement already satisfied: typing-inspect<1,>=0.4.0 in /usr/local/lib/python3.12/dist-packages (from dataclasses-json<0.7.0,>=0.6.7->langchain-community) (0.9.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.12/dist-packages (from jsonpatch<2.0.0,>=1.33.0->langchain-core) (3.0.0)\n",
            "Requirement already satisfied: langchain-text-splitters<2.0.0,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from langchain-classic<2.0.0,>=1.0.0->langchain-community) (1.1.0)\n",
            "Requirement already satisfied: requests-toolbelt>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from langsmith<1.0.0,>=0.3.45->langchain-core) (1.0.0)\n",
            "Requirement already satisfied: zstandard>=0.23.0 in /usr/local/lib/python3.12/dist-packages (from langsmith<1.0.0,>=0.3.45->langchain-core) (0.25.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain-core) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.41.4 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain-core) (2.41.4)\n",
            "Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain-core) (0.4.2)\n",
            "Requirement already satisfied: python-dotenv>=0.21.0 in /usr/local/lib/python3.12/dist-packages (from pydantic-settings<3.0.0,>=2.10.1->langchain-community) (1.2.1)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (2026.1.4)\n",
            "Requirement already satisfied: greenlet>=1 in /usr/local/lib/python3.12/dist-packages (from SQLAlchemy<3.0.0,>=1.4.0->langchain-community) (3.3.0)\n",
            "Requirement already satisfied: pyproject_hooks in /usr/local/lib/python3.12/dist-packages (from build>=1.0.3->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.2.0)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx>=0.27.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (4.12.1)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx>=0.27.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx>=0.27.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.16.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=4.19.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=4.19.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=4.19.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.30.0)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.12/dist-packages (from kubernetes>=28.1.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.17.0)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.12/dist-packages (from kubernetes>=28.1.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (2.9.0.post0)\n",
            "Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /usr/local/lib/python3.12/dist-packages (from kubernetes>=28.1.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.9.0)\n",
            "Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.12/dist-packages (from kubernetes>=28.1.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (2.0.0)\n",
            "Requirement already satisfied: durationpy>=0.7 in /usr/local/lib/python3.12/dist-packages (from kubernetes>=28.1.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.10)\n",
            "Requirement already satisfied: coloredlogs in /usr/local/lib/python3.12/dist-packages (from onnxruntime>=1.14.1->chromadb<2.0.0,>=1.3.5->langchain-chroma) (15.0.1)\n",
            "Requirement already satisfied: flatbuffers in /usr/local/lib/python3.12/dist-packages (from onnxruntime>=1.14.1->chromadb<2.0.0,>=1.3.5->langchain-chroma) (25.12.19)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.12/dist-packages (from onnxruntime>=1.14.1->chromadb<2.0.0,>=1.3.5->langchain-chroma) (5.29.5)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.12/dist-packages (from onnxruntime>=1.14.1->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.14.0)\n",
            "Requirement already satisfied: importlib-metadata<8.8.0,>=6.0 in /usr/local/lib/python3.12/dist-packages (from opentelemetry-api>=1.2.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (8.7.1)\n",
            "Requirement already satisfied: googleapis-common-protos~=1.57 in /usr/local/lib/python3.12/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.72.0)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-common==1.39.1 in /usr/local/lib/python3.12/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.39.1)\n",
            "Requirement already satisfied: opentelemetry-proto==1.39.1 in /usr/local/lib/python3.12/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.39.1)\n",
            "Requirement already satisfied: opentelemetry-semantic-conventions==0.60b1 in /usr/local/lib/python3.12/dist-packages (from opentelemetry-sdk>=1.2.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.60b1)\n",
            "Requirement already satisfied: backoff>=1.10.0 in /usr/local/lib/python3.12/dist-packages (from posthog<6.0.0,>=2.4.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (2.2.1)\n",
            "Requirement already satisfied: distro>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from posthog<6.0.0,>=2.4.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.9.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich>=10.11.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (4.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich>=10.11.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (2.19.2)\n",
            "Requirement already satisfied: huggingface-hub<2.0,>=0.16.4 in /usr/local/lib/python3.12/dist-packages (from tokenizers>=0.13.2->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.36.0)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.12/dist-packages (from typer>=0.9.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (8.3.1)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.12/dist-packages (from typer>=0.9.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.5.4)\n",
            "Requirement already satisfied: mypy-extensions>=0.3.0 in /usr/local/lib/python3.12/dist-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7.0,>=0.6.7->langchain-community) (1.1.0)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.12/dist-packages (from uvicorn[standard]>=0.18.3->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.7.1)\n",
            "Requirement already satisfied: uvloop>=0.15.1 in /usr/local/lib/python3.12/dist-packages (from uvicorn[standard]>=0.18.3->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.22.1)\n",
            "Requirement already satisfied: watchfiles>=0.13 in /usr/local/lib/python3.12/dist-packages (from uvicorn[standard]>=0.18.3->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.1.1)\n",
            "Requirement already satisfied: websockets>=10.4 in /usr/local/lib/python3.12/dist-packages (from uvicorn[standard]>=0.18.3->chromadb<2.0.0,>=1.3.5->langchain-chroma) (15.0.1)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=0.16.4->tokenizers>=0.13.2->chromadb<2.0.0,>=1.3.5->langchain-chroma) (3.20.3)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=0.16.4->tokenizers>=0.13.2->chromadb<2.0.0,>=1.3.5->langchain-chroma) (2025.3.0)\n",
            "Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<2.0,>=0.16.4->tokenizers>=0.13.2->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.2.0)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.12/dist-packages (from importlib-metadata<8.8.0,>=6.0->opentelemetry-api>=1.2.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (3.23.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (0.1.2)\n",
            "Requirement already satisfied: humanfriendly>=9.1 in /usr/local/lib/python3.12/dist-packages (from coloredlogs->onnxruntime>=1.14.1->chromadb<2.0.0,>=1.3.5->langchain-chroma) (10.0)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.12/dist-packages (from requests-oauthlib->kubernetes>=28.1.0->chromadb<2.0.0,>=1.3.5->langchain-chroma) (3.3.1)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from sympy->onnxruntime>=1.14.1->chromadb<2.0.0,>=1.3.5->langchain-chroma) (1.3.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.document_loaders import PyPDFLoader\n",
        "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
        "from langchain_chroma import Chroma\n",
        "from langchain_ollama import OllamaEmbeddings\n",
        "\n",
        "def ingest_pdf(file_path):\n",
        "    # 1. Load PDF\n",
        "    loader = PyPDFLoader(file_path)\n",
        "    data = loader.load()\n",
        "\n",
        "    # 2. Split text\n",
        "    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)\n",
        "    chunks = text_splitter.split_documents(data)\n",
        "\n",
        "    # 3. Create Vector DB\n",
        "    vector_db = Chroma.from_documents(\n",
        "        documents=chunks,\n",
        "        embedding=OllamaEmbeddings(model=\"nomic-embed-text\"),\n",
        "        persist_directory=\"../db\" # Save to root db folder\n",
        "    )\n",
        "    print(\"Vector database created and saved to /db\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    ingest_pdf(\"../data/system_analysis.pdf\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sa2IAEteQ2bc",
        "outputId": "a91a2f22-1915-4717-bed7-ac239323b539"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Vector database created and saved to /db\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2c936b34"
      },
      "source": [
        "### Uploading the PDF File\n",
        "\n",
        "To resolve the `ValueError`, please upload the `system_analysis.pdf` file to your Colab session. You can do this by:\n",
        "\n",
        "1.  Clicking the 'Files' icon (folder icon) on the left sidebar.\n",
        "2.  Clicking the 'Upload to session storage' icon (page with an arrow pointing up).\n",
        "3.  Selecting `system_analysis.pdf` from your local machine."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "74d50b0b",
        "outputId": "70c812a9-a3c7-4c7b-e12b-eb45aaa23838"
      },
      "source": [
        "import os\n",
        "import shutil\n",
        "\n",
        "file_name = \"system_analysis.pdf\"\n",
        "source_path = f\"/content/system_analysis.pdf\"\n",
        "dest_dir = \"../data\"\n",
        "dest_path = f\"{dest_dir}/{file_name}\"\n",
        "\n",
        "# Create the target directory if it doesn't exist\n",
        "if not os.path.exists(dest_dir):\n",
        "    os.makedirs(dest_dir)\n",
        "    print(f\"Created directory: {dest_dir}\")\n",
        "\n",
        "# Check if the file was uploaded to the root /content/ directory\n",
        "if os.path.exists(source_path):\n",
        "    shutil.move(source_path, dest_path)\n",
        "    print(f\"Moved {file_name} from {source_path} to {dest_path}\")\n",
        "    # Now call the ingest_pdf function from the previous cell\n",
        "    ingest_pdf(dest_path)\n",
        "else:\n",
        "    print(f\"Error: {file_name} not found at {source_path}. Please ensure the file is uploaded.\")"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error: system_analysis.pdf not found at /content/system_analysis.pdf. Please ensure the file is uploaded.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.runnables import RunnablePassthrough\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "from langchain_chroma import Chroma\n",
        "from langchain_ollama import OllamaEmbeddings\n",
        "from langchain_community.llms import Ollama # Corrected import path for Ollama\n",
        "\n",
        "# Reload the vector_db as it was created in a local scope previously\n",
        "embedding_model = OllamaEmbeddings(model=\"nomic-embed-text\")\n",
        "vector_db = Chroma(persist_directory=\"../db\", embedding_function=embedding_model)\n",
        "\n",
        "# Initialize the LLM\n",
        "llm = Ollama(model=\"llama3\")\n",
        "\n",
        "# Defining the chain using the pipe (|) operator\n",
        "template = \"\"\"Answer the question based only on the following context:\n",
        "{context}\n",
        "\n",
        "Question: {question}\n",
        "\"\"\"\n",
        "prompt = ChatPromptTemplate.from_template(template)\n",
        "\n",
        "chain = (\n",
        "    {\"context\": vector_db.as_retriever(), \"question\": RunnablePassthrough()}\n",
        "    | prompt\n",
        "    | llm\n",
        "    | StrOutputParser()\n",
        ")\n",
        "\n",
        "# Usage:\n",
        "# chain.invoke(\"What is the system analysis?\")"
      ],
      "metadata": {
        "id": "aDgFzESvWTA_"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Example usage:\n",
        "response = chain.invoke(\"What is the system analysis?\")\n",
        "print(response)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sk-S4DxlXNot",
        "outputId": "25c6030d-aa10-48c9-b2a8-eccd567cf2bb"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "According to the context, System Analysis is the very first step in any system development where developers come together to understand the problem, needs, and objectives of the project. Some of its key aspects are:\n",
            "\n",
            "* Problem Identification: identifying the issues that the system is aiming to address\n",
            "* Requirements Gathering: gathering and writing down the requirements, involving communication with customers and developers\n",
            "* Feasibility study: evaluating technical, operational, and financial aspects to determine the feasibility of the proposed solution\n"
          ]
        }
      ]
    }
  ]
}