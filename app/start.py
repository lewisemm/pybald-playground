import pybald
from pybald import context
from pybald.core.controllers import Controller, action
from pybald.core.router import Router

pybald.configure(debug=True)


def map(urls):
    urls.connect(
        "user", r"/user/new/", controller="user", action="registration")
    urls.connect(
        "login", r"/auth/login/", controller="user", action="login")
    urls.connect(
        "logout", r"/auth/logout/", controller="user", action="logout")

    urls.connect(
        "bucketlist-list",
        r"/bucketlists/",
        controller="bucketlist",
        action="list",
        conditions={"method": ["GET"]}
    )
    urls.connect(
        "bucketlist-create",
        r"/bucketlists/",
        controller="bucketlist",
        action="create",
        conditions={"method": ["POST"]}
    )
    urls.connect(
        "bucketlist-detail",
        r"/bucketlists/{id}/",
        controller="bucketlist",
        action="detail",
        conditions={"method": ["GET"]}
    )
    urls.connect(
        "bucketlist-update",
        r"/bucketlists/{id}/",
        controller="bucketlist",
        action="update",
        conditions={"method": ["PUT"]}
    )
    urls.connect(
        "bucketlist-delete",
        r"/bucketlists/{id}/",
        controller="bucketlist",
        action="destroy",
        conditions={"method": ["DELETE"]}
    )


class UserController(Controller):
    @action
    def registration(self, req):
        return "Registration logic here!"

    @action
    def login(self, req):
        return "Login logic here!"

    @action
    def logout(self, req):
        return "Logout logic here!"


class BucketlistController(Controller):
    @action
    def list(self, req):
        return "Bucketlist:list logic here!"

    @action
    def create(self, req):
        return "Bucketlist:create logic here!"

    @action
    def detail(self, req):
        return "Bucketlist:detail for bucketlist ID {} here!".format(
            "req.id")

    @action
    def update(self, req):
        return "Bucketlist:update for bucketlist ID {} here!".format(
            "req.id")

    @action
    def destroy(self, req):
        return "Bucketlist:destroy for bucketlist ID {} here!".format(
            "req.id")


app = Router(routes=map, controllers=[UserController, BucketlistController])

if __name__ == "__main__":
    context.start(app)