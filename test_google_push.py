# test_google_push.py

from utils.google_sheets import push_to_google_sheets

dummy_data = [
    {"title": "Test 1", "source": "Local", "link": "https://test1.com"},
    {"title": "Test 2", "source": "Local", "link": "https://test2.com"},
]

push_to_google_sheets(dummy_data)
