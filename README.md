# langchain-openai

This package contains the LangChain integrations for MoonshotAI through the `openai` SDK.

## Installation and Setup

- Install the LangChain partner package
```bash
pip install langchain-moonshot
```
- Get a Moonshot api key and set it as an environment variable (`MOONSHOT_API_KEY`)
- Get a Moonshot base url and set it as an environment variable (`MOONSHOT_API_BASE`)


## LLM

See a [usage example](http://python.langchain.com/docs/integrations/llms/openai).

```python
from langchain_moonshot import OpenAI
```

Obsolete: If you are using a model hosted on `Azure`, you should use different wrapper for that:
```python
from langchain_openai import AzureOpenAI
```
For a more detailed walkthrough of the `Azure` wrapper, see [here](http://python.langchain.com/docs/integrations/llms/azure_openai)


## Chat model

See a [usage example](http://python.langchain.com/docs/integrations/chat/openai).

```python
from langchain_moonshot import ChatOpenAI
```

Obsolete: If you are using a model hosted on `Azure`, you should use different wrapper for that:
```python
from langchain_openai import AzureChatOpenAI
```
For a more detailed walkthrough of the `Azure` wrapper, see [here](http://python.langchain.com/docs/integrations/chat/azure_chat_openai)


## Text Embedding Model

See a [usage example](http://python.langchain.com/docs/integrations/text_embedding/openai)

```python
from langchain_moonshot import OpenAIEmbeddings
```

Obsolete: If you are using a model hosted on `Azure`, you should use different wrapper for that:
```python
from langchain_openai import AzureOpenAIEmbeddings
```
For a more detailed walkthrough of the `Azure` wrapper, see [here](https://python.langchain.com/docs/integrations/text_embedding/azureopenai)