import requests
import pyttsx3


# Get Bitcoin live price from Coingecko exchange
def get_bitcoin_price():
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        )
        response.raise_for_status()
        price = response.json()["bitcoin"]["usd"]
        return price
    except Exception as e:
        return None


# Text-To-Speech (TTS) Function powered by pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    price = get_bitcoin_price()
    if price:
        speak(f"Live Bitcoin Price: {price} US dollars.")
    else:
        speak("Sorry, I couldn't fetch the Bitcoin price.")


if __name__ == "__main__":
    main()
