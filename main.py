import os
import pandas as pd

def update_source_link():
    chats = [ f for f in os.listdir('chat-file') if '[LINE]' in f ]
    out_links = []
    for cf in chats:
        links = get_yt_links(os.path.join('chat-file', cf))
        print("\n\n", cf, "\n\n")
        print(links)
        out_links += links
    pd.DataFrame({'link':out_links}).to_csv("links.csv", index=False) 



def get_yt_links(chatfile):
    with open(chatfile, 'r', errors='ignore') as f:
        lines = f.readlines()
    def is_yt_link(x):
        if 'https' in x and 'youtu' in x:
            return True
        return False
    links = list(filter(is_yt_link, lines))
    def process_link_line(x):
        x = x.replace("\n", "")
        x = x[x.find('http'):]
        return x
    return list(map(process_link_line, links))


def download_mp3(folder, link):
    command = '.\\bin\\youtube-dl.exe --extract-audio --audio-format "mp3" -o "mp3\\{}\\%(title)s.%(ext)s" "{}"'
    command = command.format(folder, link)
    print(command)
    os.system(command)

if __name__ == '__main__':
    update_source_link()
    df = pd.read_csv("links.csv")
    for link in df.link.tolist():
        download_mp3('ava8125', link)
    foo = input("\nDone")
