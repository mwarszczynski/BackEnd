import pytest

from social_media import Facebook


@pytest.fixture()
def facebook():
    facebook = Facebook()
    yield facebook
    # facebook.remove()


def test_facebook_initialization(facebook):
    assert facebook


def test_facebook_upload_post(facebook):
    facebook.send_message('Hello World')
    assert facebook.post_content == ['Hello World']


def test_facebook_upload_post_length(facebook):
    with pytest.raises(Exception):
        facebook.send_message('Hello'*42)
    assert facebook.post_content == []


# Next
