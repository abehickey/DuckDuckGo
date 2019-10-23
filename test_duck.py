import requests

url_ddg = "https://api.duckduckgo.com"

test_input = ["Washington",
              "Adams",
              "Jefferson",
              "Madison",
              "Monroe",
              "Jackson",
              "Van Buren",
              "Harrison",
              "Tyler",
              "Polk",
              "Taylor",
              "Fillmore",
              "Pierce",
              "Buchanan",
              "Lincoln",
              "Johnson",
              "Grant",
              "Hayes",
              "Garfield",
              "Arthur",
              "Cleveland",
              "McKinley",
              "Roosevelt",
              "Taft",
              "Wilson",
              "Harding",
              "Coolidge",
              "Hoover",
              "Truman",
              "Eisenhower",
              "Kennedy",
              "Nixon",
              "Ford",
              "Carter",
              "Reagan",
              "Bush",
              "Clinton",
              "Obama",
              "Trump"
              ]


def test_presidents():
    # Query DuckDuckGo with "presidents of the united states"
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data['RelatedTopics']

    # Create a list of Text from RelatedTopics
    search_list = []
    for i in range(len(related_topics)):
        search_list.append(related_topics[i]['Text'])

    # Search for President's last name
    str_search_list = str(search_list)
    found = True
    for pres in test_input:
        # If the name is not found then found variable will be changed to False
        if pres not in str_search_list:
            found = False

    assert found == True
