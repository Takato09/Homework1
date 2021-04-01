from tld import get_tld  # pip install tld

site_list = ["https://www.twitch.tv", "https://www.youtube.com", "https://pasts.aluksne.lv", "https://us02web.zoom.us",
             "https://www.wikimedia.org/", "https://minecraftonly.ru", "https://codeby.net"]


def ste_to_domain(url) -> list:
    return [get_tld(i) for i in url]


print(site_list)
print(ste_to_domain(site_list))
