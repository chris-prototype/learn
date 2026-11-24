def get_greeting():
  return "Hello"


# temporarily replace get_greeting with a lambda function
# pytest looks for test_
# monkeypatch requires no import
def test_greeting(monkeypatch):
  monkeypatch.setattr(__name__, "get_greeting", lambda: "Hi")
  assert get_greeting() == "Hi"