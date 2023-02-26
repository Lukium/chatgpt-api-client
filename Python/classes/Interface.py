import uuid

from classes.ChatGPTClient import ChatGPTClient
import settings.Settings as Settings

class Interface:
    def __init__(self):
        self.endpoint_chat = Settings.CHATGPT_API_BASE_URL + Settings.CHATGPT_ENDPOINTS_CHAT
        self.endpoint_recall = Settings.CHATGPT_API_BASE_URL + Settings.CHATGPT_ENDPOINTS_RECALL
        self.endpoint_add_user = Settings.CHATGPT_API_BASE_URL + Settings.CHATGPT_ENDPOINTS_ADD_USER
        self.ChatGPTClient = ChatGPTClient()    
  
    async def chat(self):
        """
        Ask ChatGPT a question using the chat endpoint.
        """
        #GET API KEY
        self.user = None
        while self.user is None:
            self.user = input(f'Enter your API KEY:\n(Required) (Length:{Settings.CHATGPT_API_KEY_LENGTH})\n')
            try:
                if len(self.user) < Settings.CHATGPT_API_KEY_LENGTH or len(self.user) > Settings.CHATGPT_API_KEY_LENGTH:
                    raise ValueError
            except ValueError:
                print(f'Invalid API KEY, it must be {Settings.CHATGPT_API_KEY_LENGTH} characters long.')
                self.user = None
        #GET PROMPT
        self.prompt = None
        while self.prompt is None:
            self.prompt = input(f'Enter your prompt (Required):\n')
            try:
                if len(self.prompt) < 1:
                    raise ValueError
            except ValueError:
                print(f'Invalid prompt, it must be at least 1 character long.')
                self.prompt = None

        #GET REPLY TYPE
        self.reply_only = None
        while self.reply_only is None:
            self.reply_only = input(f'What type of reply would you like to receive?\n(Required) [R(Reply Only) | J(Full Json) | Default: (R)]\n')
            try:
                if self.reply_only == '':
                    self.reply_only = 'R'
                if self.reply_only.upper() not in ['R', 'J']:
                    raise ValueError
            except ValueError:
                print(f'Invalid reply type, it must be R or J.')
                self.reply_only = None
        if self.reply_only.upper() == 'J':
            self.reply_only = 'false'
        elif self.reply_only.upper() == 'R':
            self.reply_only = 'true'

        #GET CONVERSATION ID
        self.conversation_id = None
        self.conversation_id = input(f'Enter your exixsting Conversation ID if you would like to followup on a previous conversation:\n')
        while True:            
            if self.conversation_id == '':
                break
            try:
                uuid_obj = uuid.UUID(self.conversation_id, version=4)
                if str(uuid_obj) == self.conversation_id:
                    break
            except ValueError:
                pass
            new_input = input(f'Invalid Conversation ID, it must be a valid UUID or left blank, Please try again')
            if new_input == '':
                break
            self.conversation_id = new_input
        if self.conversation_id == '':
            self.conversation_id = None

        #GET PLUS
        self.plus = None
        while self.plus is None:
            self.plus = input(f'Select whether to use a Plus account:\n[Y(Yes) | N(No) | A(Any) | Default: (N)]\n')
            try:
                if self.plus == '':
                    self.plus = 'N'
                if self.plus.upper() not in ['Y', 'N', 'A']:
                    raise ValueError
            except ValueError:
                print(f'Invalid plus, it must be Y, N or A.')
                self.plus = None
        if self.plus.upper() == 'A':
            self.plus = 'any'
        elif self.plus.upper() == 'Y':
            self.plus = 'true'
        elif self.plus.upper() == 'N':
            self.plus = 'false'

        #GET ACCESS TOKEN
        self.access_token = input(f'Enter your Access Token if you would like to use your own account (can be retrieved from Access Token Option):\n')

        #GET USER PLUS
        if self.access_token != '':
            self.user_plus = None
            while self.user_plus is None:
                self.user_plus = input(f'Is your Access Token linked to a Plus Account?\n(Required when using Access Token) [Y(Yes) | N(No) | Default: (N)]\n')
                try:
                    if self.user_plus == '':
                        self.user_plus = 'N'
                    if self.user_plus.upper() not in ['Y', 'N']:
                        raise ValueError
                except ValueError:
                    print(f'Invalid user plus, it must be Y or N.')
                    self.user_plus = None
        if self.access_token == '':
            self.access_token = None
            self.user_plus = None
        
        print(f'Please wait...')
        response = await self.ChatGPTClient.ask(prompt = self.prompt,
                                                user = self.user,
                                                reply_only = self.reply_only,
                                                conversation_id = self.conversation_id,
                                                plus = self.plus,
                                                access_token = self.access_token,
                                                user_plus = self.user_plus,)
        
        print(f'Response: {response}')



