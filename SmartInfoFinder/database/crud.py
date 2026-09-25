from sqlalchemy.orm import Session

from database.models import (
    User,
    Conversation,
    Message
)


# ==================================================
# USER FUNCTIONS
# ==================================================

def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(
            User.email == email.strip().lower()
        )
        .first()
    )


def get_user_by_id(
    db: Session,
    user_id: int
):

    return (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )


# ==================================================
# CONVERSATION FUNCTIONS
# ==================================================

def create_conversation(
    db: Session,
    user_id: int,
    title: str = "New Chat"
):

    conversation = Conversation(
        user_id=user_id,
        title=title
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversation(
    db: Session,
    conversation_id: int,
    user_id: int
):

    return (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id
        )
        .first()
    )


def get_conversations(
    db: Session,
    user_id: int
):

    return (
        db.query(Conversation)
        .filter(
            Conversation.user_id == user_id
        )
        .join(Message)
        .distinct()
        .order_by(
            Conversation.updated_at.desc()
        )
        .all()
    )


def update_conversation_title(
    db: Session,
    conversation_id: int,
    user_id: int,
    title: str
):

    conversation = get_conversation(
        db,
        conversation_id,
        user_id
    )

    if not conversation:
        return None

    conversation.title = title.strip()

    db.commit()
    db.refresh(conversation)

    return conversation


def delete_conversation(
    db: Session,
    conversation_id: int,
    user_id: int
):

    conversation = get_conversation(
        db,
        conversation_id,
        user_id
    )

    if not conversation:
        return False

    db.delete(conversation)
    db.commit()

    return True


# ==================================================
# MESSAGE FUNCTIONS
# ==================================================

def get_messages(
    db: Session,
    conversation_id: int,
    user_id: int
):

    conversation = get_conversation(
        db,
        conversation_id,
        user_id
    )

    if not conversation:
        return []

    return (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation_id
        )
        .order_by(
            Message.created_at.asc()
        )
        .all()
    )


def add_message(
    db: Session,
    conversation_id: int,
    user_id: int,
    role: str,
    content: str
):

    conversation = get_conversation(
        db,
        conversation_id,
        user_id
    )

    if not conversation:
        return None

    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content
    )

    db.add(message)

    # Update conversation timestamp
    conversation.updated_at = message.created_at

    db.commit()
    db.refresh(message)

    return message