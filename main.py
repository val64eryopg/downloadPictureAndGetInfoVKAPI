import requests
import json

TOKEN = ""
ID = ""
PATH = ""


def get_pictures_from_api_request(path, token, id):
    req = requests.get(
        "https://api.vk.com/method/photos.getAll?owner_id={1}&photo_sizes=0&access_token={0}&v=V".format(token, id))
    jn = json.loads(req.text)
    for files in jn["response"]["items"]:
        url_photo = files["photo_1280"]
        api = requests.get(url_photo)
        file_name = url_photo.split("/")[-1].split("?")[-2]
        print(file_name)
        with open("{0}\{1}".format(path, file_name), "wb") as f:
            f.write(api.content)


def get_info(id, token):
    req = requests.get(
        "https://api.vk.com/method/users.get?user_ids={1}&photo_sizes=0&fields=sex,status,is_friend,city&access_token={0}&v=V".format(
            token, id))
    jn = json.loads(req.text)
    print("id: ", jn["response"][-1]["id"])
    print("first name: ", jn["response"][-1]["first_name"])
    print("last name: ", jn["response"][-1]["last_name"])
    print("city: ", jn["response"][-1]["city"]["title"])

    if jn["response"][-1]["sex"] == 1:
        print("sex: female")
    else:
        if jn["response"][-1]["sex"] == 2:
            print("sex: male")


if __name__ == '__main__':
    get_pictures_from_api_request(PATH, TOKEN, ID)
    get_info(ID, TOKEN)
