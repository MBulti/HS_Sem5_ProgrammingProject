"""
Implementation of Programming Project Flask API
This returns the movie recommendation based on a entered movie
"""
import os
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class Recommendation(Resource):
    """
    Recommendation Endpoint, takes the watched movie as a string
    """

    def get(self):
        args = request.args;
        print(args)

        """
        Retuns the movie input
        """
        data={"data": args['movie']}

        return data

api.add_resource(Recommendation,'/recommendation')


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")


    app.run(host="0.0.0.0", port=cfg_port, debug=True)
#Test