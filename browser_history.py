class WebPage:
    def __init__(self, url, title):
        self.url = url
        self.title = title

class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit(self, url, title):
        new_page = WebPage(url, title)
        self.history.append(new_page)
        print(f"Visited: {new_page.title} ({new_page.url})")

    def back(self):
        if len(self.history) <= 1:
            print("No previous page in history.")
            return None
        self.history.pop()
        current_page = self.history[-1]
        print(f"Back to: {current_page.title} ({current_page.url})")
        return current_page

    def current_page(self):
        if not self.history:
            print("No pages in history.")
            return None
        current_page = self.history[-1]
        print(f"Current page: {current_page.title} ({current_page.url})")
        return current_page

# Example Usage
if __name__ == "__main__":
    browser = BrowserHistory()

    # Visiting pages
    browser.visit("http://example.com", "Example Domain")
    browser.visit("http://google.com", "Google")
    browser.visit("http://youtube.com", "YouTube")

    # Current page
    browser.current_page()

    # Going back in history
    browser.back()
    browser.back()

    # Try to go back when no previous pages are available
    browser.back()
