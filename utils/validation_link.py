def validate_url(url):
    if (("https://" in url) or ("http://" in url)):
        valid_url = url[8:]
        count = 0
        if ("/" in valid_url):
            for symbol in valid_url:
                count += 1
                if symbol == "/":
                    new_url = valid_url[:count-1]
                    return new_url
        return valid_url
    return url
