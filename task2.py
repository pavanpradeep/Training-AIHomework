
from flask import Flask
from flask_restplus import Resource, Api, reqparse, fields
import requests

app = Flask(__name__)
api = Api(app)

model = api.model('Url Model', {'url': fields.String(description="Url of the Website")})

@api.route('/api/v1/ping')
class API1(Resource):

    @api.expect(model)
    def post(request):
        try:
            url = api.payload["url"]
            resp = requests.get(url)
            # import pdb;pdb.set_trace();
            return {'resp': resp.status_code}
        except Exception as e:
            return {"Error": str(e)}



@api.route('/health')
class API2(Resource):

    def get(request):
        return{"health": "Healthly"}


@api.route('/api/v1/info')
class API3(Resource):

    def get(request):
        return{"Receiver": "Cisco is the best!"}



if __name__ == '__main__':
    app.run(debug=True, port=8080)


