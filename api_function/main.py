import functions_framework
from google.cloud import firestore_v1

@functions_framework.http
def get_video(request):
    db = firestore_v1.Client(project='scareflix', database='scareflix-db')
    col_ref = db.collection("videos")
    return [{'id':doc.id, 'data': doc.to_dict()} for doc in col_ref.get()]
