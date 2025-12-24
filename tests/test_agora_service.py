import pytest
from services.agora_service import AgoraService

@pytest.fixture
def agora_service():
    return AgoraService()

def test_generate_rtc_token_returns_string(agora_service):
    channel = "test_channel"
    uid = "user_123"
    role = "host"

    token = agora_service.generate_rtc_token(channel_name=channel, uid=uid, role=role)
    assert isinstance(token, str)
    assert len(token) > 0

def test_generate_rtc_token_invalid_role(agora_service):
    with pytest.raises(ValueError):
        agora_service.generate_rtc_token(channel_name="ch", uid="uid", role="invalid_role")

def test_generate_rtm_token_returns_string(agora_service):
    uid = "user_456"
    token = agora_service.generate_rtm_token(uid=uid)
    assert isinstance(token, str)
    assert len(token) > 0