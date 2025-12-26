# Traductor entre HTTP y el dominio
# Estará recibiendo requests, llamando servicios del dominio y devolviendo respuestas HTTP.

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.domain.models import Conversation
from app.services.conversation import receive_message
from app.storage.memory import get_conversation, save_conversation

router = APIRouter()

class MessageRequest(BaseModel):
    conversation_id: str
    sender: str
    content: str
    timestamp: str
    
@router.post("/messages")
def post_message(payload: MessageRequest):
    conversation = get_conversation(payload.conversation_id)
    
    if not conversation:
        conversation = Conversation(id=payload.conversation_id)
        
    try:
        conversation = receive_message(
            conversation,
            sender=payload.sender,
            content=payload.content
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    save_conversation(conversation)

    return {
        "conversation_id": conversation.id,
        "messages": len(conversation.messages),
        "state": conversation.state
    }