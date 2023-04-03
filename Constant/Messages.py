from Constant.Values import POST_LIMIT

HELP_MESSAGE = """```Post limit: """ + str(POST_LIMIT) + """
help
wiki [search query]
man [page]
google [search query]
show [count] [file name] meme(s)
show [count] [tag multi_word_tag] porn(s),
show [search query]```"""
HELLO_MESSAGE = "Shut the fuck lil dick and go suck on your mummy's titties and stop wasting my time"
NEGATIVE_MESSAGES = ["SQUID GAMES!!", "IDK", "No", "Nope", "I don't want to", "Kill yourself", "Make Sarah do it", "I'm busy playing Minecraft"]
MAGIC_EIGHT_BALL_MESSAGES = ["Yes", "No", "Maybe", "Probably", "Probably Not", "For sure", "No chance", "Uncertain", "How should I know", "You may rely on it.", "As I see it, yes", "I don't care", "Signs point to yes", "Better not tell you now", "You better believe it", "Concentrate and ask again", "Don't count on it", "My sources say no", "Very doubtful"]
DATE_TIME_MESSAGE_FORMAT = "{0} {1}, {2}:{3}{4}"
ERROR_OVER_LIMIT_MESSAGE = "Sorry, my current post limit is {0}".format(str(POST_LIMIT))
ERROR_EXCEPTION_MESSAGE = "Something went wrong (Likely Google Rate Limited)"
ERROR_INVALID_USE_MESSAGE = "I do not understand"