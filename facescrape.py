from facebook_scraper import get_posts

def main():
    title = input("Enter the page name: ")
    pages = int(input("Enter the number of pages: "))
    for post in get_posts(title, pages=pages, extra_info = True):
        print(post['text'])

if __name__ == '__main__':
    main()
