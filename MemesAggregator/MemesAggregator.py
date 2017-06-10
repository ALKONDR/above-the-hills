import json
import os
import urllib.request

import time
import vk

ID_MEMES_GROUP = '-92879038'
IMG_NAME = 'img.jpg'
INFO_NAME = 'info.json'
DEFAULT_SAVE_PATH = 'MemesAggregator/data/'


def get_group_posts(vk_api, id, count):
    posts = vk_api.wall.get(owner_id=id, count=count)
    for i in range(1, count + 1):
        save_post_to_db(posts[i], id)


def save_post_to_db(post, group_id):
    # Create dir for group posts if not exist
    group_path = DEFAULT_SAVE_PATH + group_id
    if not os.path.exists(group_path):
        os.makedirs(group_path)

    # Create dir for post if not exist
    post_path = group_path + '/' + str(post['id']) + '/'
    if not os.path.exists(post_path):
        os.makedirs(post_path)

    save_img(post, post_path)
    save_info(post, post_path)


def save_img(post, path):
    # Save img only if no image was saved previously
    if not os.path.exists(path + IMG_NAME):
        photo_url = post['attachments'][0]['photo']['src']
        urllib.request.urlretrieve(photo_url, path + IMG_NAME)


def save_info(post, path):
    if not os.path.exists(path + INFO_NAME):
        data = {}
        likes_history = []

        data['id'] = post['id']
        data['likes_history'] = likes_history
        add_like_info(data, post)

        with open(path + INFO_NAME, 'w') as fp:
            json.dump(data, fp)
    else:
        with open(path + INFO_NAME) as data_file:
            data = json.load(data_file)
            add_like_info(data, post)
            save_json(path + INFO_NAME, data)
        pass


def add_like_info(data, post):
    current_time = int(time.time())
    like_info = {str(current_time): post['likes']['count']}
    data['likes_history'].append(like_info)


def save_json(file, data):
    with open(file, 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    id = ID_MEMES_GROUP
    session = vk.Session()
    vk_api = vk.API(session)
    get_group_posts(vk_api, id, 10)
