from main import get_weather

def test_get_weather():
    assert get_weather(21) == "Hot" 
    # As we wrote in get_weather func that if temp>20 it should be hot so we cross checked here whether it is working correctly or not

