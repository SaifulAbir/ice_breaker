from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from third_parties.linkedin import scrape_linkedin_profile

# from langchain_anthropic import ChatAnthropic
# from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")

    summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # llm = ChatOllama(model="mistral")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # Free tier available
        temperature=0
    )

    # Claude 3.5 Haiku
    # llm = ChatAnthropic(
    #     model="claude-3-5-haiku-20241022",
    #     temperature=0
    # )

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/saifulislamcse/")

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
