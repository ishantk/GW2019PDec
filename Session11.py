"""
Strings in Python
String is textual data (aplhanumeric + symbols)
"""

# johnsShopTitle = 'Johns Coffee Shop'
# johnsShopTitle = 'John's Coffee Shop'  # error
# johnsShopTitle = 'John\'s Coffee Shop' # escape sequence
# johnsShopTitle = "John's Coffee Shop"
johnsShopTitle = r'John\'s Coffee Shop' # raw string

print(johnsShopTitle, type(johnsShopTitle))

print()

textMessage = "Hello" \
              "This is John" \
              "When can we meet and discuss Project?"
print(textMessage)

print()

quotes = """Work Hard, Get Luckier
Search the Candle, rather than cursing the darkness
    Be Exceptional
"""

print(quotes)