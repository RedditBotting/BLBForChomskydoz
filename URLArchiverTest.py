import URLArchiver

urlsForTesting = ["www.google.com", "www.reddit.com", "www.meatspin.com"]

for url in urlsForTesting:
    print url + " with archive URL of " + URLArchiver.archive(url)