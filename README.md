# ❄️ Ice Breaker - LangChain Agent App

A LangChain-powered project that generates personalized ice breakers based on a person's LinkedIn profile. Built using Gemini (Google Generative AI), OpenAI (optional), Tavily, and Scrapin.io — with both CLI and web UI support.

---

## 🚀 What It Does

Given a person's name:

1. 🔎 Searches Google to find their LinkedIn profile using Tavily.
2. 🌐 Scrapes public profile data via [Scrapin.io](https://scrapin.io).
3. 🤖 Feeds that data to Gemini or OpenAI to generate:
   - A short summary
   - Two interesting facts
4. ✅ Outputs a clean result via CLI or Flask API.

---

## 🧠 How It Works

1. **🔍 LinkedIn URL Lookup**
   - Uses Tavily's search API via a LangChain tool.
   - ReAct agent powered by Gemini chooses to trigger the tool when needed.

2. **🌐 LinkedIn Scraping**
   - Uses Scrapin.io to extract structured profile info.
   - Supports a `mock=True` mode using sample data for testing.

3. **💬 Ice Breaker Generation**
   - A Gemini (default) or OpenAI model receives structured profile data and returns:
     - One summary
     - Two interesting facts
   - Output is parsed with LangChain's `PydanticOutputParser`.

4. **🖥️ Interfaces**
   - Use via terminal or through a web-based Flask app.

---

## 🧪 Quickstart

### 1. Install dependencies

```bash
pipenv install
```

### 2. Then activate the shell

```bash
pipenv shell
```

### 2. Create your `.env` file

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
SCRAPIN_API_KEY=your_scrapin_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🔁 Switching Between LLMs

In `ice_breaker.py`, you can switch the model easily:

```python
# Gemini (default)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# OpenAI (optional)
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

Both are supported using LangChain interfaces.

---

## 🧾 Output Structure

The LLM output is parsed into a structured format using Pydantic:

```python
class Summary(BaseModel):
    summary: str
    facts: List[str]
```

Returned as:

```json
{
  "summary": "Saiful Islam is a software engineer with over 4 years of experience specializing in web development, focusing on building scalable and efficient web applications.",
  "facts": [
    "Saiful received a recommendation from a former colleague who praised his ability to develop brilliant, elegant, and cost-effective solutions to complex problems, highlighting his problem-solving skills and professional work ethic.",
    "Saiful has a strong interest in Generative AI & LLMs, indicating his commitment to staying updated with cutting-edge technologies and industry trends."
  ]
}
```

---

## 💻 CLI Usage

```bash
python ice_breaker.py
```

---

## 🌐 Web UI (Flask)

You can also use the Flask web app.

### Start the server:

```bash
python app.py
```

Visit: [http://localhost:5001](http://localhost:5001)

---

## 🧠 Technologies Used

- [LangChain](https://www.langchain.com/)
- [Gemini (Google AI)](https://ai.google.dev/)
- [OpenAI GPT-3.5 (Optional)](https://platform.openai.com/)
- [Tavily](https://www.tavily.com/)
- [Scrapin.io](https://scrapin.io/)
- [Flask](https://flask.palletsprojects.com/)
- [Pydantic](https://docs.pydantic.dev/)
