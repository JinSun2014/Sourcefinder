#! /usr/bin/env python2.7.3

import wikipedia

def wiki(subject):
    result = []
    search_result = wikipedia.search(subject)
    if search_result == []:
        search_result = wikipedia.suggest(subject)[0]
    else:
        search_result = search_result[0]
    try:
        response = wikipedia.page(search_result)
    except wikipedia.exceptions.DisambiguationError as e:
        print e.options
        return []
    original_source='wikipedia'
    result.append({'title': response.title, 'url': response.url, 'original_source':original_source})
    return result

if __name__ == "__main__":
    print wiki('comcast')
    print wiki('kongfu panda')
    print wiki('Murcercy')

