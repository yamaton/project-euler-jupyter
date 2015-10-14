"""
Quick and dirty script to get project euler problem descriptions

Required libraries
==================
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)

Usage:
======
```
$ python scrape-project-euler.py <problem-id>
```

<problem-id> should be a number, like 42.
The script produces Markdown/HTML styled text as standard output.

@author yamaton
@date 2015-10-14
"""

import sys
import urllib.request
import bs4

BASE = 'https://projecteuler.net/problem={}'


def get_raw_content(problem_id):
    url = BASE.format(problem_id)
    with urllib.request.urlopen(url) as f:
        rawhtml = f.read()
    return rawhtml


def scrape(raw):
    """
    Scrape html and return dictionary with keys
        'id'      (int)
        'title'   (str)
        'url'     (str)
        'content' (soup)
    """
    soup = bs4.BeautifulSoup(raw, 'html.parser')

    tmp = soup.find('h3').get_text()
    prob_id = int(tmp.replace('Problem ', ''))
    url = BASE.format(prob_id)
    title = soup.find('h2').get_text()
    content = soup.find('div', 'problem_content')

    return {'id': prob_id, 'url': url,
            'title': title, 'content': content}


def quick_print(data):
    print('## Problem {}'.format(data['id']))
    print()
    print('[{}]({})'.format(data['title'], data['url']))
    print()
    print('> ', end='')
    print(data['content'])


def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: python {} <problem-number>'.format(sys.argv[0]))

    problem = int(sys.argv[1])
    raw = get_raw_content(problem)
    data = scrape(raw)
    quick_print(data)


if __name__ == '__main__':
        main()
