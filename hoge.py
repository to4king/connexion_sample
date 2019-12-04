import connexion

def get_sample(**kwargs):
    return {'status': 'hoge OK!!'}

options = {"swagger_ui": True}
app = connexion.FlaskApp(__name__, specification_dir='openapi/', options=options)
app.add_api('spec.yaml')
app.run(port=8080)