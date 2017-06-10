import json
import os
import urllib.request

import vk

ID_MEMES_GROUP = '-92879038'
IMG_NAME = 'img.jpg'
INFO_NAME = 'info.json'
DEFAULT_SAVE_PATH = 'MemesAggregator/data/'


def get_group_posts(vk_api, id):
    posts = vk_api.wall.get(owner_id=id, count=2)
    for i in range(1, 3):
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
        with open(path + INFO_NAME, 'w') as fp:
            json.dump({}, fp)
    else:
        pass


if __name__ == '__main__':
    id = ID_MEMES_GROUP
    session = vk.Session()
    vk_api = vk.API(session)
    get_group_posts(vk_api, id)
