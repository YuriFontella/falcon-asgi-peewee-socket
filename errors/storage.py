import falcon

class StorageError:
    @staticmethod
    async def handle(e, req, resp, params):
        raise falcon.HTTPInternalServerError(description=str(e))