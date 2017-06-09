import os
import urllib.request

import vk

ID_MEMES_GROUP = '-92879038'
IMG_NAME = 'img.jpg'
DATA_NAME = 'info'
DEFAULT_SAVE_PATH = 'MemesAggregator/data/'


def get_group_posts(vk_api, id):
    posts = vk_api.wall.get(owner_id=id, count=2)
    for i in range(1, 3):
        save_post_to_db(posts[i], id)


def save_post_to_db(post, group_id):
    post_id = str(post['id'])
    save_path = DEFAULT_SAVE_PATH + group_id
    photo_save_path = save_path + '/' + post_id + '/'

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    if not os.path.exists(photo_save_path):
        os.makedirs(photo_save_path)

    photo_url = post['attachments'][0]['photo']['src']
    urllib.request.urlretrieve(photo_url, photo_save_path + IMG_NAME)


if __name__ == '__main__':
    id = ID_MEMES_GROUP
    session = vk.Session()
    vk_api = vk.API(session)
    get_group_posts(vk_api, id)
