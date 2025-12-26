from typing import Dict
from app.domain.models import Conversation

_conversations: Dict[str, Conversation] = {}


def get_conversation(conversation_id: str) -> Conversation | None:
    return _conversations.get(conversation_id)

def save_conversation(conversation: Conversation) -> None:
    _conversations[conversation.id] = conversation

