# Static Methods

class ChaiUtils:

    @staticmethod
    def clean_ingrediants(text):
        return [item.strip() for item in text.split(",")]

raw = " water , milk , ginger , honey "

# normal stuff
# obj = ChaiUtils()
# obj.clean_ingrediants(raw)

# decorator usage

cleaned = ChaiUtils.clean_ingrediants(raw) # no need to create objects
print(cleaned)