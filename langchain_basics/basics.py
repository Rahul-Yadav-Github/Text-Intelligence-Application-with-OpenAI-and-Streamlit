# Import necessary modules
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.agents import initialize_agent, load_tools, AgentType
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.chains import ConversationChain

# Initialize an LLM with a given temperature
llm = OpenAI(temperature=0.9)

# Create a prompt template for generating restaurant names
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

# Generate a restaurant name for Indian cuisine
chain = LLMChain(llm=llm, prompt=prompt_template_name)
name = chain.run("Indian")
print(name)

# Create a sequential chain to generate a restaurant name and menu items
llm = OpenAI(temperature=0.6)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}"
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)
chain = SimpleSequentialChain(chains=[name_chain, food_items_chain])

# Generate restaurant name and menu items for Indian cuisine
content = chain.run("Indian")
print(content)

# Initialize and run an agent with specific tools
llm = OpenAI(temperature=0.7)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
result = agent.run("What was the GDP of US in 2022 plus 5?")
print(result)

# Run a conversation chain
convo = ConversationChain(llm=OpenAI(temperature=0.7))
response = convo.run("Who won the first cricket world cup?")
print(response)

# Run a conversation chain with memory
memory = ConversationBufferMemory()
chain_with_memory = LLMChain(llm=llm, prompt=prompt_template_name, memory=memory)
name_with_memory = chain_with_memory.run("Mexican")
print(name_with_memory)

# Print the conversation memory buffer
print(chain_with_memory.memory.buffer)

# Use conversation buffer window memory
memory_window = ConversationBufferWindowMemory(k=1)
convo_window = ConversationChain(llm=OpenAI(temperature=0.7), memory=memory_window)
response_window = convo_window.run("How much is 5+5?")
print(response_window)
