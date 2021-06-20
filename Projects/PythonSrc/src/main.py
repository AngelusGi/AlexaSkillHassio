import logging
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
import requests
import random


skillBuilder = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

print("ciao")

@skillBuilder.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    speech = "Hi, welcome to Showertime Thoughts."
    asktext = "Would you like to hear one?"
    handler_input.response_builder.speak(
    speech + " " + asktext).ask(asktext)
    return handler_input.response_builder.response

@skillBuilder.request_handler(can_handle_func=is_intent_name("GetShowerThoughtIntent"))


def whats_my_color_intent(handler_input):
    url = 'https://www.reddit.com/rand/showerthoughts.json?limit=100'
    response = requests.get(url,headers={'User-agent':'showertimethoughts'})
    rand = random.randint(1, 100)
    showerthought = response.json()['data']['children'][rand]['data']['title']
    asktext = "Wanna hear one more?"
    handler_input.response_builder.speak(showerthought).ask(asktext)
    return handler_input.response_builder.response
