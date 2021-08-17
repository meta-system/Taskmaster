# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def migrate(series):
    with open("excel-to-json-(dev-bay.com).json") as file:
        input = json.load(file)

    newEntry = {}

    curEpisode = 0
    curTaskNumb = 0
    #f input[1]
    #dirt, cleanString = soup.find(class_="cc-tagline").text.split(": ", 1)
    #print(input[0]["Task "])
    inputTask = input[0]
    taskLine = inputTask["Task"]
    prevTitle = ""
    prevEpisode = 0
    if len(taskLine) > 3 :
        episodeStr, title = taskLine.split(": ")
        prevTitle = title
        dirt, episodeStr = episodeStr.split(" ")
        episode = int(episodeStr)
        prevEpisode = episode
    else:
        title = prevTitle
        episode = prevEpisode

    #curEpisode, title = input[1]["Task "][:-1].split(": ")
    print(episode)
    print(title)
    newEntry.update()
    print(inputTask)
    inputTask.pop("Task")
    inputTask.pop("Description")
    newEntry = {
        "Series" : series,
        "Episode" : episode,
        "Episode Title" : title,
        "Number": 1,
        "Type": "Prize",
        "Description": "Most unusual item.",
        "Points": inputTask
    }

    taskList = []
    taskList.append(newEntry)
    print(taskList)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    migrate("1")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
