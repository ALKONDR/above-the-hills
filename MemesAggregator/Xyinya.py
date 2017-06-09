import os

import vk

ID_SPORTS_RU_GROUP = '-755816'
IMG_NAME = 'img'
DATA_NAME = 'info'
DEFAULT_SAVE_PATH = 'data/'


def get_group_posts(vk_api, id):
    posts = vk_api.wall.get(owner_id=id, count=10)
    for i in range(1, 10):
        print(posts[i]['text'])
        save_post_to_db(posts[i], id)


def save_post_to_db(post, post_id):
    save_path = DEFAULT_SAVE_PATH + post_id
    if not os.path.exists(save_path):
        os.makedirs(save_path)


if __name__ == '__main__':
    id = ID_SPORTS_RU_GROUP
    session = vk.Session()
    vk_api = vk.API(session)
    get_group_posts(vk_api, id)
