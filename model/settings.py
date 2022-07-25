import os

# We will store images uploaded by the user on this folder
UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# REDIS
# Queue name
REDIS_QUEUE = "app_queue"
REDIS_VIDEO_QUEUE = "video_queue"
# Port
REDIS_PORT = 6379
# DB Id
REDIS_DB_ID = 0
# Host IP
REDIS_IP = "redis"
# Sleep parameters which manages the
# interval between requests to our redis queue
SERVER_SLEEP = 0.05

SHAPE = (224,224)
MODEL_CLASSES_MOVEMENT = ['Motion', 'Pull', 'Push', 'Static']
MODEL_CLASSES_SCALE = ['CS', 'ECS', 'FS', 'LS', 'MS']
PATH_MODEL_MOVEMENT = './weight/model.05-0.9174.h5'
PATH_MODEL_SCALE = './weight/model.04-0.5498.h5'
PATH_MODEL = './weight/model.06-1.5956.h5'
FRAMES = 8