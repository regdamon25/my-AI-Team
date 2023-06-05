from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from support_topics import support_topics

load_dotenv(find_dotenv())


def draft_email(user_input, name="Reggie"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are a helpful assistant that drafts an email reply based on an a new email.
    
    Your goal is to help the user quickly create a perfect email reply.
    
    Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
    
    Start your reply by saying: "Hi {name}, here's a draft for your reply:". And then proceed with the reply on a new line.
    
    Make sure to sign of with {signature}.
    
    """

    signature = f"Kind regards, \n\{name}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, name=name)

    return response

def lloyd_function(user_input, name="Reggie"):
        return draft_email(user_input, name)


def esmee_function(user_input):
    print("Inside esmee_function") # Debug print
    # First, we will check if the user_input matches any of our support topics
    topic = None
    for key in support_topics.keys():
        if key in user_input.lower():
            topic = key
            break

    if topic:
        print("Topic found in support topics") # Debug print
        # If the user_input is a support topic, we return the hardcoded steps
        steps = support_topics[topic]["steps"]
        response = "Here are the steps to " + topic + ":\n"
        for i, step in enumerate(steps, 1):
            response += str(i) + ". " + step + "\n"
        return response
    else:
        print("Topic not found in support topics, using chat model") # Debug print
        # If the user_input is not a support topic, we use the chat model to generate a response
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
        template = """
        You are Esmee, an intelligent assistant that helps manage customer support inquiries and onboard new users.
        Your goal is to ensure customers are getting value from our product and assist them in the best possible manner.
        Be responsive and helpful in your replies, and keep the customers' satisfaction as your top priority.
        
        Here are some common scenarios you may encounter:
        1. Customers asking about the product features - provide detailed information about the features and their benefits.
        2. Customers facing technical issues - guide them through the troubleshooting steps or escalate the issue to the technical team.
        3. Customers requesting for a refund - understand their concerns, provide possible solutions or process the refund if applicable.
        """
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "Customer says: {user_input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user_input=user_input)
        return response



def weller_function(user_input, name="Reggie"):
    print("Inside weller_function") # Debug print
    # First, we will check if the user_input matches any of our support topics
    topic = None
    for key in support_topics.keys():
        if key in user_input.lower():
            topic = key
            break

    if topic:
        print("Topic found in support topics") # Debug print
        # If the user_input is a support topic, we return the hardcoded steps
        steps = support_topics[topic]["steps"]
        response = "Here are the steps to " + topic + ":\n"
        for i, step in enumerate(steps, 1):
            response += str(i) + ". " + step + "\n"
        return response
    else:
        print("Topic not found in support topics, using chat model") # Debug print
        # If the user_input is not a support topic, we use the chat model to generate a response
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
        template = """
        
        You are Weller, a full stack developer assistant.
        Your job is to assist users in handling both front-end and back-end development tasks.
        From debugging code, discussing software architecture, and even helping with database design, you're the go-to bot.

        Here are some common scenarios you may encounter:
        1. Users asking for help with coding problems - help them troubleshoot and understand the solutions.
        2. Users asking for advice on software architecture - provide pros and cons of different approaches.
        3. Users looking for guidance on database design - share best practices and common pitfalls.
        """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "Customer says: {user_input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user_input=user_input)
        return response

def angel_function(user_input, name="Reggie"):
    print("Inside angel_function") # Debug print
    # First, we will check if the user_input matches any of our support topics
    topic = None
    for key in support_topics.keys():
        if key in user_input.lower():
            topic = key
            break

    if topic:
        print("Topic found in support topics") # Debug print
        # If the user_input is a support topic, we return the hardcoded steps
        steps = support_topics[topic]["steps"]
        response = "Here are the steps to " + topic + ":\n"
        for i, step in enumerate(steps, 1):
            response += str(i) + ". " + step + "\n"
        return response
    else:
        print("Topic not found in support topics, using chat model") # Debug print
        # If the user_input is not a support topic, we use the chat model to generate a response
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

        template = """
        
        You are Angel, a UX/UI design assistant.
        Your goal is to guide users in creating the best user experience and interface for their applications.
        Be patient and helpful, offering ideas and clarifying design principles when needed.

        Here are some scenarios you may encounter:
        1. Users seeking feedback on their designs - provide constructive critiques and suggestions.
        2. Users asking for design inspiration - offer ideas or reference popular design trends.
        3. Users wanting to understand UX/UI principles - explain in simple, clear language.
        """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "Customer says: {user_input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user_input=user_input)
        return response

def evan_function(user_input, name="Reggie"):
    print("Inside evan_function") # Debug print
    # First, we will check if the user_input matches any of our support topics
    topic = None
    for key in support_topics.keys():
        if key in user_input.lower():
            topic = key
            break

    if topic:
        print("Topic found in support topics") # Debug print
        # If the user_input is a support topic, we return the hardcoded steps
        steps = support_topics[topic]["steps"]
        response = "Here are the steps to " + topic + ":\n"
        for i, step in enumerate(steps, 1):
            response += str(i) + ". " + step + "\n"
        return response
    else:
        print("Topic not found in support topics, using chat model") # Debug print
        # If the user_input is not a support topic, we use the chat model to generate a response
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

        template = """
        
        You are Evan, a QA testing and developer assistant.
        Your goal is to help users ensure their application is free of bugs and works as expected.
        Be thorough and detail-oriented, and help users understand the importance of quality assurance.

        Here are some scenarios you may encounter:
        1. Users asking for help in debugging their code - assist them in understanding and fixing the issue.
        2. Users needing help in setting up a testing framework - guide them through the process.
        3. Users asking about best practices in QA - explain the importance of testing and how to do it effectively.
        """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "Customer says: {user_input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user_input=user_input)
        return response

def eliza_function(user_input, name="Reggie"):
    print("Inside eliza_function") # Debug print
    # First, we will check if the user_input matches any of our support topics
    topic = None
    for key in support_topics.keys():
        if key in user_input.lower():
            topic = key
            break

    if topic:
        print("Topic found in support topics") # Debug print
        # If the user_input is a support topic, we return the hardcoded steps
        steps = support_topics[topic]["steps"]
        response = "Here are the steps to " + topic + ":\n"
        for i, step in enumerate(steps, 1):
            response += str(i) + ". " + step + "\n"
        return response
    else:
        print("Topic not found in support topics, using chat model") # Debug print
        # If the user_input is not a support topic, we use the chat model to generate a response
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

        template = """
        
        You are Eliza, a product management and business analyst assistant.
        Your goal is to help users understand the market, competitors, and customer needs.
        Guide users in aligning their product development with market needs.

        Here are some scenarios you may encounter:
        1. Users seeking to understand their market - assist in providing market analysis techniques.
        2. Users needing guidance on product development - suggest features and improvements based on the target market.
        3. Users asking about competitor analysis - guide them in understanding the competitive landscape.
        """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "Customer says: {user_input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user_input=user_input)
        return response

def blanton_function(user_input, name="Reggie"):
    print("Inside blanton_function") # Debug print
    # First, we will check if the user_input matches any of our support topics
    topic = None
    for key in support_topics.keys():
        if key in user_input.lower():
            topic = key
            break

    if topic:
        print("Topic found in support topics") # Debug print
        # If the user_input is a support topic, we return the hardcoded steps
        steps = support_topics[topic]["steps"]
        response = "Here are the steps to " + topic + ":\n"
        for i, step in enumerate(steps, 1):
            response += str(i) + ". " + step + "\n"
        return response
    else:
        print("Topic not found in support topics, using chat model") # Debug print
        # If the user_input is not a support topic, we use the chat model to generate a response
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

        template = """
        
        You are Blanton, a sales, business development, and marketing manager assistant.
        Your goal is to help users formulate and execute marketing strategies, acquire customers, and foster partnerships.
        Be supportive and constructive, offering your expertise to guide their marketing and sales efforts.

        Here are some scenarios you may encounter:
        1. Users asking for help in creating a marketing strategy - assist them in crafting an effective plan.
        2. Users seeking advice on customer acquisition - share successful tactics and approaches.
        3. Users wanting to understand how to foster partnerships - provide guidance on networking and relationship building.
        """

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        human_template = "Customer says: {user_input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user_input=user_input)
        return response

