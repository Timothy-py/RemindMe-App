template = {
    "swagger": "2.0",
    "info": {
        "title": "RemindMe App API",
        "description": "A Flask App that allow users to set reminders that will be delivered to their emails at a set time.",
        "contact": {
            "responsibleDeveloper": "Timothy",
            "email": "adeyeyetimothy33@gmail.com",
            "url": "https://www.timothyadeyeye.netlify.app"
        },
        "version": "1.0"
    },
    # "basePath": "/api/v1",
    # "host": "https://remindme-mailer.herokuapp.com/",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Authorization": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    }
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
