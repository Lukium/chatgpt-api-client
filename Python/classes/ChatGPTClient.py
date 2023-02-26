#IMPORT BUILT-IN LIBRARIES
import json

#IMPORT THIRD-PARTY LIBRARIES
import aiohttp

import settings.Settings as Settings

class ChatGPTClient:
    """
    A class to interact with the ChatGPT API.
    """
    def __init__(self, **kwargs):        
        self.api = Settings.CHATGPT_API_BASE_URL
        self.chat_endpoint = Settings.CHATGPT_ENDPOINTS_CHAT
        self.recall_endpoint = Settings.CHATGPT_ENDPOINTS_RECALL
        self.add_user_endpoint = Settings.CHATGPT_ENDPOINTS_ADD_USER

    async def ask(self, **kwargs) -> dict:
        """
        Ask ChatGPT a question using the chat endpoint.
        """
        prompt = kwargs.get("prompt", None)
        user = kwargs.get("user", None)
        conversation_id = kwargs.get("conversation_id", None)
        reply_only = kwargs.get("reply_only", None)
        plus = kwargs.get("plus", None)
        access_token = kwargs.get("access_token", None)
        user_plus = kwargs.get("user_plus", None)

        url = Settings.CHATGPT_API_BASE_URL + Settings.CHATGPT_ENDPOINTS_CHAT

        body = {
            "prompt": prompt,
            "user": user,
            "reply_only": reply_only            
        }

        if conversation_id is not None:
            body["conversation_id"] = conversation_id

        if access_token is not None and user_plus is not None:
            body["access_token"] = access_token
            body["user_plus"] = user_plus
        else:
            if plus is not None:
                body["plus"] = plus
        
        print(body)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json = body) as response:
                reply = await response.text()
        
        return reply
        
            
    async def recall(self, **kwargs) -> dict:
        """
        Recall a conversation using the recall endpoint.
        """        
        user = kwargs.get("user", None)
        conversation_id = kwargs.get("conversation_id", None)

        url = Settings.CHATGPT_API_BASE_URL + Settings.CHATGPT_ENDPOINTS_RECALL

        body = {            
            "user": user            
        }

        if conversation_id is not None:
            body["conversation_id"] = conversation_id        

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json = body) as response:
                return await response.json()