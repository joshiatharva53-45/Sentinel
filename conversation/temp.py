import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from conversation.session import ConversationSession

session = ConversationSession()

print(session.session_id)

print(session.state)

print(session.expired())

session.history.add(
    role="user",
    content="Hello Sentinel"
)

print(session.history.count())