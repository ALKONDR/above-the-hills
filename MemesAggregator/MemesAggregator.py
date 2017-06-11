import json
import os
import shutil
import urllib.request
import time
import vk
from scipy.spatial import distance as dist
from skimage.measure import compare_ssim as ssim
import cv2

IMG_NAME = 'img.jpg'
INFO_NAME = 'info.json'
POST_TEMP_SAVE_PATH = 'MemesAggregator/temp_data/'
POST_TEMPLATE_SAVE_PATH = 'MemesAggregator/data_template/'
TEMPLATE_PATH = 'MemesAggregator/templates/'
TEMPLATES_DICT = [TEMPLATE_PATH + "Agutin.jpg", TEMPLATE_PATH + "Finger.jpg",
                  TEMPLATE_PATH + "Leo.jpg", TEMPLATE_PATH + "Robert.jpg",
                  TEMPLATE_PATH + "SadMan.jpg", TEMPLATE_PATH + "Lyagootka.jpg", TEMPLATE_PATH + "Wowdoge.jpg"]
GROUPS = {'-148089915'}
SCAN_TIME = int(time.time())


# **************MAIN METHODS******************

def get_group_posts(vk_api, id, count):
    posts = vk_api.wall.get(owner_id=id, count=count)
    for i in range(1, count + 1):
        if 'attachments' in posts[i]:
            if 'photo' in posts[i]['attachments'][0]:
                if 'src' in posts[i]['attachments'][0]['photo']:
                    clusterizate(posts[i], id, POST_TEMPLATE_SAVE_PATH)
                    # delete_meta_info()


# Db path - save to temp folder or to template
def clusterizate(post, group_id, db_path):
    # Create dir for group posts if not exist
    group_path = db_path + group_id
    if not os.path.exists(group_path):
        os.makedirs(group_path)

    # Create dir for post if not exist
    post_path = group_path + '/' + str(post['id']) + '/'
    if not os.path.exists(post_path):
        os.makedirs(post_path)

    save_img(post, post_path)
    template = get_best_template(post_path + IMG_NAME)
    # If file is suitable for the one of the templates
    if len(template) != 0:
        save_info_to_template(post, template)


def delete_meta_info():
    for id in GROUPS:
        shutil.rmtree(POST_TEMPLATE_SAVE_PATH + id + '/')


def save_info_to_template(post, template):
    template_name = template[template.rfind('/') + 1:template.rfind('.')]
    data = get_json(template_name)
    add_like_info(data, template_name, post)
    pass


# **************HELP METHODS******************

def get_best_template(url):
    best_template = ""
    best_colleration = -1
    for i in range(len(TEMPLATES_DICT)):
        mem_value = compare(url, TEMPLATES_DICT[i])
        if best_colleration < mem_value:
            best_colleration = mem_value
            best_template = TEMPLATES_DICT[i]
    if best_colleration <= 0.6:
        return ""
    else:
        return best_template


def compare(imagePathA, imagePathB):
    imageA = cv2.imread(imagePathA)
    imageB = cv2.imread(imagePathB)

    histA = cv2.calcHist([imageA], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    histA = cv2.normalize(histA, histA).flatten()

    histB = cv2.calcHist([imageB], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    histB = cv2.normalize(histB, histB).flatten()

    d = cv2.compareHist(histA, histB, cv2.HISTCMP_CORREL)
    d2 = dist.chebyshev(histA, histB)

    imageA_ssim = cv2.medianBlur(cv2.resize(cv2.imread(imagePathA, 0), (500, 500), interpolation=cv2.INTER_AREA), 7)
    imageB_ssim = cv2.medianBlur(cv2.resize(cv2.imread(imagePathB, 0), (500, 500), interpolation=cv2.INTER_AREA), 7)
    d3 = ssim(imageA_ssim, imageB_ssim)
    return min(abs(d), ((abs(d) ** 0.5) + abs(d3 - d2) ** 0.6) * 0.5);


def save_img(post, path):
    # Save img only if no image was saved previously
    photo_url = post['attachments'][0]['photo']['src']
    urllib.request.urlretrieve(photo_url, path + IMG_NAME)


def add_like_info(data, template_name, post):
    like_info = {str(SCAN_TIME): post['likes']['count']}
    data['likes_history'].append(like_info)
    save_json(POST_TEMPLATE_SAVE_PATH + template_name + '.json', data)


def save_json(path, data):
    with open(path, 'w') as fp:
        json.dump(data, fp)


def get_json(name):
    path = POST_TEMPLATE_SAVE_PATH + name + '.json'
    # Create if not exist
    if not os.path.exists(path):
        data = {}
        likes_history = []
        data['likes_history'] = likes_history
        save_json(path, data)
        with open(path) as json_data:
            return json.load(json_data)
    else:
        with open(path) as json_data:
            return json.load(json_data)


if __name__ == '__main__':
    session = vk.Session()
    vk_api = vk.API(session)
    for id in GROUPS:
        get_group_posts(vk_api, id, 6)
