import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request
from functions import lloyd_function, esmee_function, blanton_function, eliza_function, evan_function, angel_function

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set Slack API credentials for new apps or use this to set the default bot
def get_new_or_default_bot_config(bot_name):
    bot_token = os.environ.get(f"{bot_name}_SLACK_BOT_TOKEN")
    signing_secret = os.environ.get(f"{bot_name}_SLACK_SIGNING_SECRET")
    bot_user_id = os.environ.get(f"{bot_name}_SLACK_BOT_USER_ID")

    return bot_token, signing_secret, bot_user_id

def get_bot_user_id(bot_token):
    try:
        slack_client = WebClient(token=bot_token)
        response = slack_client.auth_test()
        return response["user_id"]
    except SlackApiError as e:
        print(f"Error: {e}")
        
# Get the config for a default bot and initialize the app
default_bot_name = 'LLOYD'
default_bot_token, default_signing_secret, default_bot_user_id = get_new_or_default_bot_config(default_bot_name)

bot_id_name_mapping = {
     os.environ.get('LLOYD_SLACK_BOT_USER_ID'): 'LLOYD',
    os.environ.get('ESMEE_SLACK_BOT_USER_ID'): 'ESMEE',
    os.environ.get('ANGEL_SLACK_BOT_USER_ID'): 'ANGEL',
    os.environ.get('ELIZA_SLACK_BOT_USER_ID'): 'ELIZA',
    os.environ.get('EVAN_SLACK_BOT_USER_ID'): 'EVAN',
    os.environ.get('BLANTON_SLACK_BOT_USER_ID'): 'BLANTON',
    # and so on
}

# Dictionary of bot functions, mapped by bot ID
bot_functions = {
    os.environ.get('LLOYD_SLACK_BOT_USER_ID'): lloyd_function,
    os.environ.get('ESMEE_SLACK_BOT_USER_ID'): esmee_function,
    os.environ.get('ANGEL_SLACK_BOT_USER_ID'): angel_function,
    os.environ.get('ELIZA_SLACK_BOT_USER_ID'): eliza_function,
    os.environ.get('EVAN_SLACK_BOT_USER_ID'): evan_function,
    os.environ.get('BLANTON_SLACK_BOT_USER_ID'): blanton_function,
}

def get_bot_config(bot_name):
    # Now you can get environment variables
    bot_token = os.environ.get(f"{bot_name}_SLACK_BOT_TOKEN")
    signing_secret = os.environ.get(f"{bot_name}_SLACK_SIGNING_SECRET")
    bot_user_id = os.environ.get(f"{bot_name}_SLACK_BOT_USER_ID")

    return bot_token, signing_secret, bot_user_id



# Initialize the Flask app
flask_app = Flask(__name__)
        
def my_function(text):
    
    """
    Custom function to process the text and return a response.
    In this example, the function converts the input text to uppercase.

    Args:
        text (str): The input text to process.

    Returns:
        str: The processed text.
    """
    response = text.upper()
    return response


bot_credentials = {}  # Global dictionary to store bot credentials



        
logging.basicConfig(level=logging.DEBUG)

bot_handlers = {}  # Dictionary to store SlackRequestHandler for each bot

# Initialize the SlackRequestHandler for each bot
for bot_name in ['LLOYD', 'ESMEE', 'BLANTON', 'ELIZA', 'EVAN', 'ANGEL']:
    bot_token, signing_secret, bot_user_id = get_bot_config(bot_name)
    app = App(token=bot_token, signing_secret=signing_secret)

    # Define the handle_mentions function
    def handle_mentions(body, say):
        text = body["event"]["text"]

        # Extract the bot ID from the message
        bot_id_mention = text.split()[0]
        bot_id = bot_id_mention.replace('<@', '').replace('>', '')  # Removes the '<@' and '>' around the bot ID

        # Remove the mention of the bot from the text
        text = text.replace(bot_id_mention, "").strip()

        # Retrieve bot function from the dictionary and call it
        bot_function = bot_functions.get(bot_id)
        if bot_function:
            response = bot_function(text)
            say(response)
        else:
            say("Sorry, I don't know how to respond to that.")

    # Register the function to handle app_mention events
    app.event("app_mention")(handle_mentions)

    handler = SlackRequestHandler(app)
    bot_handlers[bot_user_id] = handler


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    logging.info('Handling a new request in slack_events method')
    logging.debug(f'Request: {request}')
    
    # Extract the bot ID from the request's text field
    text = request.json['event']['text']
    bot_id_mention = text.split()[0]
    bot_id = bot_id_mention.replace('<@', '').replace('>', '')  # Removes the '<@' and '>' around the bot ID
    
    # Get the correct handler for the bot
    handler = bot_handlers.get(bot_id)
    if handler is not None:
        response = handler.handle(request)
        logging.debug(f'Response: {response}')
        return response
    else:
        logging.error(f'No handler found for bot {bot_id}')
        return make_response("No handler found for bot", 404)




# Run the Flask app
if __name__ == "__main__":
    flask_app.run(debug=True)
