# VK Admier: documentation
**VK Admier** is simple [VK API](https://vk.com/dev/first_guide) wrapper for community bot development.

## Authorization
You should create **bot object** from ```Client``` class for access to Admier's methods:
```
bot = admier.Client(<group_id: int>, <access_token: str>, <api_version: str>)
```

### ```<group_id: int>```
This is your **community ID**. You can get it [there](https://vk.com/faq18062).

Remember, module works on behalf of **your community**.

### ```<access_token: str>```
This is your **community token**. The easiest way to get it is to create token in **community settings**. 
Find it [there](https://vk.com/dev/access_token?f=2.%20%D0%9A%D0%BB%D1%8E%D1%87%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0%20%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0).

Application has to get this token. It gives access to **VK API** methods.

### ```<api_version: str>```
This is version of **VK API** service. It is not binding argument.

You can find **relevant** API version [there](https://vk.com/dev/versions).

## Long Polling

VK Admier uses **Long Poll Server** to get events. So you should connect to it with ```Client.connect()``` function:
```python
bot.connect(<handler: func>)
```
### ```<handler: func>```
**Handle function** which will process every event. It requires **event argument**.

If you need to filter some events, you can do it in [community settings](https://vk.com/dev/bots_longpoll), otherwise you can check events **programmatically**:
```python
def handle(event):
    # Is there a new message?
    if not(event["updates"]) or not(event["updates"][0]["type"] == "message_new"): return

    params = {
        "peer_id": event["updates"][0]["object"]["message"]["peer_id"],
        "random_id": 0,
        "message": "Hello World!"
    }
    bot.request("messages.send", params)

bot.connect(handle)
```
## Ussage
Use ```Client.request()``` function to make **VK API request**:
```python
bot.request(<method: str>, <parameters: dict>)
```
### ```<method: str>```
String value for method name. Find it, using official [VK API documentation](https://vk.com/dev/methods).

Remember, you can use methods **with community token authorization only**!
```python
bot.request("messages.send", params)
```
### ```<parameters: dict>```
Dictionary with required parameters. **Don't define default parameters** like ```access_token```, ```group_id```, ```v```.
```python
params = {
    "peer_id": 2000000000,
    "random_id": 0,
    "message": "Hello World!"
}
bot.request("messages.send", params)
```
## Example
You can use this template to create your bot:
```python
import admier

# Your access_token is here
access_token = ""

# Your group_id is here
group_id = "" 

def handle(event): 
    # event handler, write your code here
    print(event)

bot = admier.Client(group_id, access_token)
bot.connect(handle)
```
You can check working example in the root of repository, but you have to edit ```group_id``` and ```access_token``` variables.
