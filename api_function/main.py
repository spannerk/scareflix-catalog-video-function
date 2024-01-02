import functions_framework
from google.cloud import firestore_v1

def get_video_from_id(id):
    db = firestore_v1.Client(project='scareflix', database='scareflix-db')
    path = "videos/{}".format(id)
    doc = db.document(path).get()
    return {'id':id, 'data': doc.to_dict()}

@functions_framework.http
def get_video(request):
    video_id = request.args.get('id')
    return get_video_from_id(video_id)

if __name__ == 'main':
    print(get_video_from_id(
        'H39i2OmK5B8pm45qnyct'
    ))