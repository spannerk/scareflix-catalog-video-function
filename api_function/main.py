import functions_framework
from google.cloud import firestore_v1

def get_video_from_id(id):
    db = firestore_v1.Client(project='scareflix', database='scareflix-db')
    path = "videos/{}".format(id)
    doc = db.document(path).get()
    return {'id':id,
            'data': doc.to_dict(),
            'metadata': get_metadata(doc, db.collection("tmdb_metadata")), 
            'trigger_warnings': get_trigger_warnings(doc, db.collection("ddtd_metadata"))}

def get_metadata(doc, collection_ref):
    metadata_id = doc.to_dict().get('tmdb_metadata_id')
    if metadata_id:
        metadata_ref = collection_ref.document(metadata_id)
        metadata = metadata_ref.get()
        if metadata.exists:
            return metadata.to_dict()
    return None

def get_trigger_warnings(doc, collection_ref):
    metadata_id = doc.to_dict().get('ddtd_metadata_id')
    if metadata_id:
        metadata_ref = collection_ref.document(metadata_id)
        metadata = metadata_ref.get()
        if metadata.exists:
            return metadata.to_dict()
    return None


@functions_framework.http
def get_video(request):
    video_id = request.args.get('id')
    return get_video_from_id(video_id)

if __name__ == 'main':
    print(get_video_from_id(
        'H39i2OmK5B8pm45qnyct'
    ))