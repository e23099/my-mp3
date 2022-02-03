from main import download_mp3


def run_by_maintain_list():
    chill = []
    run = []
    downloaded_link = {}
    download_this_time = []
    with open('mp3/andy/maintain_list.md', 'r', encoding='utf-8-sig') as f:
        line = f.readline()
        while '## Chill' not in line:
            line = f.readline()
        while '## Run' not in line:
            if 'http' in line:
                link = line[line.find('http'):-2]
                chill.append(link)
                downloaded_link[link] = False
            line = f.readline()
        while '## Downloaded' not in line:
            if 'http' in line:
                link = line[line.find('http'):-2]
                run.append(link)
                downloaded_link[link] = False
            line = f.readline()
        for line in f.readlines():
            if 'http' in line:
                link = line[line.find('http'):-1]
                downloaded_link[link] = True
    

    for link in chill:
        if not downloaded_link[link]:
            download_mp3('andy/chill', link)
            download_this_time.append(link)

    for link in run:
        if not download_mp3[link]:
            download_mp3('andy/run', link)
            download_this_time.append(link)

    with open('mp3/andy/maintain_list.md', 'a+', encoding='utf-8-sig') as f:
        f.writelines(list(map(lambda x: x+'\n', download_this_time)))


if __name__ == '__main__':
    run_by_maintain_list()
