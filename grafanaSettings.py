import os

grafana_url = os.getenv('GRAFANA_URL', 'http://grafana-kaidu.192.168.162.3.nip.io')
token = os.getenv('GRAFANA_TOKEN', 'eyJrIjoiekw1cktzanZTWDBXclltTjZBOUJ3OEx2Y2lWRDFQT2EiLCJuIjoiZGV2ZWxvcGVyIiwiaWQiOjF9')
http_get_headers = {'Authorization': 'Bearer ' + token}
http_post_headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

