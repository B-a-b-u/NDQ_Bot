import os
from  dotenv import load_dotenv
from few_shots import few_shots
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts  import FewShotPromptTemplate
from langchain_community.utilities import SQLDatabase 
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain_experimental.sql import SQLDatabaseChain


# Load environment variables in .env
load_dotenv()

def get_chain():
    # Create palm llm
    # llm = GooglePalm(google_api_key = os.environ["api_key"], temperature = 0.3)
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["api_key"])


    # Creating Sql database object
    db_user = "root"
    db_password = "babu"
    db_host = "localhost"
    db_name = "pc_factory"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                                sample_rows_in_table_info=3)

    # Creating Embedding and store on Vector Database
    shot_data = [" ".join(f.values()) for f in few_shots]
    embedding = HuggingFaceHubEmbeddings()


    vector_store = FAISS.from_texts(texts = shot_data, embedding = embedding, metadatas = few_shots)
    print(vector_store)
    example = SemanticSimilarityExampleSelector(
        vectorstore= vector_store,
        k =2
    )

    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
        Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
        Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
        Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
        Pay attention to use CURDATE() function to get the current date, if the question involves "today".
        
        Use the following format:
        
        Question: Question here
        SQLQuery: Query to run with no pre-amble
        SQLResult: Result of the SQLQuery
        Answer: Final answer here
        
        No pre-amble.
        """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )


    # SQL Chain
    chain = SQLDatabaseChain.from_llm(llm=llm, db=db)
    return chain