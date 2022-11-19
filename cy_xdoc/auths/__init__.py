import cy_web
from fastapi.security import OAuth2PasswordBearer
from fastapi import Request
from cy_xdoc import libs
import cy_kit
__is_the_first_time__ = None
import cy_xdoc.services.apps
@cy_web.auth_type(OAuth2PasswordBearer)
class Authenticate:
    def validate(self,
                 request: Request,
                 username: str,
                 application: str,apps=cy_kit.inject(cy_xdoc.services.apps.AppServices)) -> bool:
        if __is_the_first_time__ is None:
            apps.create_default_app(
                login_url=cy_web.get_host_url()+"/login",
                domain=cy_web.get_host_url(),
                return_url_after_sign_in=cy_web.get_host_url()
            )

        return True
    def validate_account(self,request: Request, username: str, password: str)->bool:


        app_name=username.split('/')[0]
        username=username.split('/')[1]
        if libs.Services.account.validate(app_name,username,password):
            return dict(
                application=app_name,
                username = username,
                is_ok=True
            )
        else:
            return dict(
                application=app_name,
                username=username,
                is_ok=False
            )
