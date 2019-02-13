
import re


#Searchs the message for "negative thoughs" or "goals" ignoring case, and returns the first match it sees
def negativeThoughtsOrGoals(userMessage):
    userMessage = userMessage.lower()
    responceAsRegex = re.match("goals|negative thoughts|end the conversation", userMessage)
    try:
        responce = responceAsRegex.group(0)
        return responce
    except AttributeError:
        return "normal"


print(negativeThoughtsOrGoals("end the conver9sation"))