from TwitchWebsocket import TwitchWebsocket
import json, requests, random, logging

from Log import Log
Log(__file__)

from Settings import Settings

class TwitchDinner:
    def __init__(self):
        self.host = None
        self.port = None
        self.chan = None
        self.nick = None
        self.auth = None

        self.strings = ["You should eat ", "How about ", "Get some ", "Go eat ", "Consume this "]
        self.recipe = None
        
        # Fill previously initialised variables with data from the settings.txt file
        Settings(self)

        self.ws = TwitchWebsocket(host=self.host, 
                                  port=self.port,
                                  chan=self.chan,
                                  nick=self.nick,
                                  auth=self.auth,
                                  callback=self.message_handler,
                                  capability=["membership", "tags", "commands"],
                                  live=True)
        self.ws.start_bot()
        
    def set_settings(self, host, port, chan, nick, auth):
        self.host = host
        self.port = port
        self.chan = chan
        self.nick = nick
        self.auth = auth

    def message_handler(self, m):
        try:
            if m.type == "366":
                logging.info(f"Successfully joined channel: #{m.channel}")
            
            elif m.type == "PRIVMSG":
                if m.message.startswith(("!food", "!suggest", "!dinner", "!foodmedaddy")):
                    out = self.query_site()
                    self.ws.send_message(out)
                    logging.info(out)

                elif m.message.startswith("!recipe"):
                    if self.recipe == None:
                        out = "I don't know what food to take the recipe from NotLikeThis"
                    else:
                        out = "Recipe of most recent recommendation: " + self.recipe
                    self.ws.send_message(out)
                    logging.info(out)

        except Exception as e:
            logging.exception(e)
    
    def query_site(self):
        # Get raw HTML etc from website
        self.data = requests.get("http://www.whatthefuckshouldimakefordinner.com/").text

        # Start and end of the recipe URL
        string_recipe_start = "<dt><a href=\""
        string_recipe_end = "\" target=\"_blank\">"
        # Start and end of the recipe name
        start_recipe = self.data.find(string_recipe_start) + len(string_recipe_start)
        end_recipe = self.data.find(string_recipe_end)
        # Get the recipe
        recipe = self.data[start_recipe: end_recipe]
        if "www.cookstr.com" in recipe:
            self.recipe = self.data[start_recipe: end_recipe]
        else:
            logging.debug(f"Not a www.cookstr.com URL: {recipe}")
            self.recipe = None

        start_name = end_recipe + len(string_recipe_end)
        # And get the recipe name
        recipe_name = random.choice(self.strings) + self.data[start_name: self.data.find("<", start_name)]

        # Check if the recipe might be a book, if so, get another recipe
        # If recipe is in the name, or if there is a digit in the name, then the recipe is likely a book
        if "recipe" in recipe_name.lower() or any(char.isdigit() for char in recipe_name):
            return self.query_site()

        return recipe_name

if __name__ == "__main__":
    TwitchDinner()