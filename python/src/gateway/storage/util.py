import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    
    except Exception as err:
        print(err)
        return f"Internal Server Error: {err.__str__()}", 500
    
    message = {
            "video_fid": str(fid),
            "mp3_fid": None,
            "username": access["username"]
    }
    try:
        channel.basic_publish(
                exchange="",
                routing_key="video",
                body=json.dumps(message),
                properties=pika.BasicProperties(
                        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                    )
                )
    except Exception as err:
        print(err)
        fs.delete(fid)
        return f"Internal Server error:{err.__str__()}", 500
