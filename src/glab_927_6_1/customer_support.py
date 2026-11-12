import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from langchain_groq import ChatGroq

# Assign your API Key

# Load environment variables from .env
load_dotenv()

# Initialize LangChain with Groq Llama LLM

llm = ChatGroq(

    # model="llama3-8b-8192"
    model="openai/gpt-oss-20b"
)


# Create a prompt template for FAQs

messages = [

    ("system", "You customer support representative. Your goal is to efficiently handle queries."),

    ("human", "What are your business hours?"),

]

result = llm.invoke(messages)

print(result.content)

# Step 1: Create the first prompt template to retrieve customer query details

first_prompt_template = PromptTemplate(

    input_variables=["customer_query"],

    template="Extract the key information from the following customer query: {customer_query}"

)


# Step 2: Create the second prompt template to fetch order details based on extracted information

second_prompt_template = PromptTemplate(

    input_variables=["extracted_info"],

    template="Using the extracted information: {extracted_info}, retrieve the relevant order details."

)

# Step 3: Create the third prompt template to generate a detailed response for the customer

third_prompt_template = PromptTemplate(

    input_variables=["order_details"],

    template="Based on the following order details: {order_details}, generate a detailed response to address the customer's query."

)

# Step 4: Define the chains

first_chain = LLMChain(llm=llm, prompt=first_prompt_template)

second_chain = LLMChain(llm=llm, prompt=second_prompt_template)

third_chain = LLMChain(llm=llm, prompt=third_prompt_template)

# Input to start the prompt chain (example customer query)

initial_input = "Can you help me with the status of my order #12345 placed last week?"

# Run the first chain to extract key information from the query

extracted_info = first_chain.run(initial_input)

print("Extracted Info:", extracted_info)

# Run the second chain to retrieve order details based on the extracted information

order_details = second_chain.run(extracted_info)

print("Order Details:", order_details)

# Run the third chain to generate a detailed response based on the order details

customer_response = third_chain.run(order_details)

print("Customer Response:", customer_response)

# Prompt 1
# Original
# template = "Extract the key information from the following customer query: {customer_query}"

# New
template = (
    "You are an AI data extraction assistant for an e-commerce platform. "
    "From the following customer query, extract the key entities: Order ID, Customer Name, and Issue Type. "
    "Format the output clearly as bullet points or key-value pairs.\n\n"
    "Customer Query: {customer_query}"
)

# Prompt 2
# Original
# template = "Using the extracted information: {extracted_info}, retrieve the relevant order details."
# New
template = (
    "Using the extracted information: {extracted_info}, simulate querying the company's "
    "order management database to retrieve relevant order details (including shipping status, "
    "tracking number, carrier, and estimated delivery date). "
    "If the Order ID is missing or invalid, explicitly state that order lookup could not be completed."
)

# Prompt 3
# Original
# template = "Based on the following order details: {order_details}, generate a detailed response to address the customer's query."

# New
template = (
    "You are a professional, empathetic customer support representative. "
    "Based on the following order details: {order_details}, write a polite, clear, "
    "and helpful response addressing the customer's initial concern. "
    "Include a professional greeting, the exact status of their order, and next steps."
)
