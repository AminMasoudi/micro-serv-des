import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor

def start(message, fs_video, fs_mp3, channel):
    message = json.loads(message)
    
    tf = tempfile.NamedTemporaryFile()
    out = fs_video.get(ObjectId(message["video_fid"]))
    tf.write(out.read())
    #convert
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()
    
    #write
    tf_path = tempfile.gettempdir() + f"/{message['video_fid']}.mp3"
    audio.write_audiofile(tf_path)

    f = open(tf_path, "rb")
    data = f.read()
    f_id = fs_mp3.put(data)
    f.close()
    os.remove(tf_path)

    message["mp3_fid"] = str(f_id)

    try:
        channel.basic_publish(
                exchange="",
                routing_key=os.environ.get("MP3_QUEUE"),
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ),
        )
    except :
        fs_mp3.delete(fid)
        return "failed to publish message"



