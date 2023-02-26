#IMPORT BUILT-IN LIBRARIES
import json
import os
import platform

#LOAD SETTINGS FROM SETTINGS.JSON
with open('settings.json') as f:
    settings = json.load(f)

#SETUP TERMINAL NAME
TERMINAL_NAME = os.environ.get("TERMINAL_NAME") or str(settings['general']['terminal_name'])

#NAME TERMINAL BASED ON OPERATING SYSTEM
if platform.system() == 'Windows':
    os.system(f'title {TERMINAL_NAME}')
else:
    os.system(f'echo -ne "\033]0;{TERMINAL_NAME}\007"')

#SETUP CHATGPT SETTINGS
CHATGPT_API_KEY_LENGTH = os.environ.get("CHATGPT_API_KEY_LENGTH") or settings['chatgpt']['api_key_length']
CHATGPT_API_BASE_URL = os.environ.get("CHATGPT_API_BASEURL") or settings['chatgpt']['api_base_url']
CHATGPT_ENDPOINTS_CHAT = os.environ.get("CHATGPT_ENDPOINTS_CHAT") or settings['chatgpt']['endpoints']['chat']
CHATGPT_ENDPOINTS_RECALL = os.environ.get("CHATGPT_ENDPOINTS_RECALL") or settings['chatgpt']['endpoints']['recall']
CHATGPT_ENDPOINTS_ADD_USER = os.environ.get("CHATGPT_ENDPOINTS_ADD_USER") or settings['chatgpt']['endpoints']['add_user']

#SETUP GENERAL SETTINGS
HTTP_STATUS_CHECK_TIMEOUT = os.environ.get("HTTP_CHECK_TIMEOUT") or settings['general']['http_status_check_timeout']