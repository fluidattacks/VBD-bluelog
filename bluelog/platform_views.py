from flask import current_app
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MemberView(ModelView):
    can_delete = False

    def is_accessible(self):
        if not current_app.config.get("BACKOFFICE_LOGIN", True):
            return True
        return current_user.is_authenticated
