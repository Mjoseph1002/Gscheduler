from app import create_app
import logging

app=create_app()

# logging.basicConfig(level=logging.INFO)
# logging.info("Starting the Flask application...")
# def list_all_routes(app):
#     for rule in app.url_map.iter_rules():
#         methods = ', '.join(rule.methods)
#         print(f"Endpoint: {rule.endpoint}, URL: {rule.rule}, Methods: {methods}")

if __name__ == "__main__":
    # list_all_routes(app)
    app.run(host='127.0.0.1', port=5000,debug = app.config['DEBUG'])
