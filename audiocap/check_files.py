import os

# audio_dir = '/hy-tmp/audiocap/train/train1'
# audio_dir = '/hy-tmp/audiocap/train/train2'
# audio_dir = '/hy-tmp/audiocap/train/train3'
# audio_dir = '/hy-tmp/audiocap/train/train4'
# audio_dir = '/hy-tmp/audiocap/train/train5'
# audio_dir = '/hy-tmp/audiocap/train/train6'
# audio_dir = '/hy-tmp/audiocap/train/train7'
# audio_dir = '/hy-tmp/audiocap/train/train8'
# audio_dir = '/hy-tmp/audiocap/train/train9'
# audio_dir = '/hy-tmp/audiocap/train/train10'
# audio_dir = '/hy-tmp/audiocap/train/train11'
# audio_dir = '/hy-tmp/audiocap/train/train12'

audio_dir = '/hy-tmp/audiocap/audio_all/'

for filename in os.listdir(audio_dir):
    if filename.endswith('.wav'):
        file_path = os.path.join(audio_dir, filename)
        size = os.path.getsize(file_path)
    
        if size < 100*1024:
            print(f'{filename} is broken, deleting...')
            os.remove(file_path)
        else:
            print(f'{filename} is okay')