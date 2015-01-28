from hikes.models import Hike
import webbrowser


def mq_upload_all():
    key = 'Fmjtd%7Cluu82968l1%2Cag%3Do5-9w1x96'
    client_id = '149310'
    pswd = 'yW4dW7cX'
    table_name = 'mqap.149310_pdxhikes'
    field1 = 'Hike'
    field2 = 'Lat'
    field3 = 'Lon'
    url = 'http://www.mapquestapi.com/datamanager/v2/upload-data?key={}&inFormat=json&json={}'
    col_list = []
    col1 = {}
    col2 = {}
    col3 = []
    hikes = Hike.objects.all().order_by('name')
    for hike in hikes:
        location = hike.trailhead
        col1['name'] = field1
        col1['value'] = hike.name
        col2['name'] = field2
        col2['value'] = location.latitude
        col3['name'] = field3
        col3['value'] = location.longitude
        hike.url = encode_url(hike.name)
        col_list.append([col1, col2, col3])
    json = {"clientId": client_id, "password": pswd, "tableName": table_name, "append": 'true', "rows": col_list}

    full_url = url.format(key, json)
    webbrowser.open(full_url)


mq_upload_all()