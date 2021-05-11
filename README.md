# TwitchSuggestDinner
Twitch bot that will suggest what you should get for dinner!

---
# Explanation
When the bot has started, it will start listening to chat messages in the channel listed in the settings.txt file. Everyone in chat can now use `!dinner` for the bot to start suggesting food. Because just the name of a food isn't particularly useful, users can also type `!recipe` to see the recipe of the previously suggested meal.<br>
This bot uses the wonderful http://www.whatthefuckshouldimakefordinner.com for it's recommendations.

---

# Example

The chat output when `!dinner`, `!food`, `!foodmedaddy` or `!suggest` was typed by someone:
<pre>
<b>How about Beef Wellington</b>
</pre>
And the console:
<pre>
<b>[2019-04-28 13:01:57] [root        ] [INFO    ] - How about Beef Wellington</b>
</pre>
The chat output when `!recipe` was typed by someone, after a meal was suggested:
<pre>
<b>Recipe of most recent recommendation: https://www.cookstr.com/Beef-Recipes/Beef-Wellington-Recipe</b>
</pre>
And the console:
<pre>
<b>[2019-04-28 13:04:11] [root        ] [INFO    ] - Recipe of most recent recommendation: https://www.cookstr.com/Beef-Recipes/Beef-Wellington-Recipe</b>
</pre>

---

# Settings
This bot is controlled by a settings.txt file, which looks like:
```
{
    "Host": "irc.chat.twitch.tv",
    "Port": 6667,
    "Channel": "#<channel>",
    "Nickname": "<name>",
    "Authentication": "oauth:<auth>"
}
```

| **Parameter**        | **Meaning** | **Example** |
| -------------------- | ----------- | ----------- |
| Host                 | The URL that will be used. Do not change.                         | "irc.chat.twitch.tv" |
| Port                 | The Port that will be used. Do not change.                        | 6667 |
| Channel              | The Channel that will be connected to.                            | "#CubieDev" |
| Nickname             | The Username of the bot account.                                  | "CubieB0T" |
| Authentication       | The OAuth token for the bot account.                              | "oauth:pivogip8ybletucqdz4pkhag6itbax" |

*Note that the example OAuth token is not an actual token, but merely a generated string to give an indication what it might look like.*

I got my real OAuth token from https://twitchapps.com/tmi/.

---

# Requirements
* [Python 3.6+](https://www.python.org/downloads/)
* [Module requirements](requirements.txt)<br>
Install these modules using `pip install -r requirements.txt`

Among these modules is my own [TwitchWebsocket](https://github.com/CubieDev/TwitchWebsocket) wrapper, which makes making a Twitch chat bot a lot easier.
This repository can be seen as an implementation using this wrapper.

---

# Other Twitch Bots

* [TwitchMarkovChain](https://github.com/CubieDev/TwitchMarkovChain)
* [TwitchAIDungeon](https://github.com/CubieDev/TwitchAIDungeon)
* [TwitchGoogleTranslate](https://github.com/CubieDev/TwitchGoogleTranslate)
* [TwitchCubieBotGUI](https://github.com/CubieDev/TwitchCubieBotGUI)
* [TwitchCubieBot](https://github.com/CubieDev/TwitchCubieBot)
* [TwitchRandomRecipe](https://github.com/CubieDev/TwitchRandomRecipe)
* [TwitchUrbanDictionary](https://github.com/CubieDev/TwitchUrbanDictionary)
* [TwitchRhymeBot](https://github.com/CubieDev/TwitchRhymeBot)
* [TwitchWeather](https://github.com/CubieDev/TwitchWeather)
* [TwitchDeathCounter](https://github.com/CubieDev/TwitchDeathCounter)
* [TwitchSuggestDinner](https://github.com/CubieDev/TwitchSuggestDinner)
* [TwitchPickUser](https://github.com/CubieDev/TwitchPickUser)
* [TwitchSaveMessages](https://github.com/CubieDev/TwitchSaveMessages)
* [TwitchMMLevelPickerGUI](https://github.com/CubieDev/TwitchMMLevelPickerGUI) (Mario Maker 2 specific bot)
* [TwitchMMLevelQueueGUI](https://github.com/CubieDev/TwitchMMLevelQueueGUI) (Mario Maker 2 specific bot)
* [TwitchPackCounter](https://github.com/CubieDev/TwitchPackCounter) (Streamer specific bot)
* [TwitchDialCheck](https://github.com/CubieDev/TwitchDialCheck) (Streamer specific bot)
* [TwitchSendMessage](https://github.com/CubieDev/TwitchSendMessage) (Meant for debugging purposes)

