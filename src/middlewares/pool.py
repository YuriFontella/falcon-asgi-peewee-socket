from config.db.pool import db

class Pool:
    async def process_request(self, req, resp):
        db.connect(reuse_if_open=True)

    async def process_response(self, req, resp, resource, params):
        db.close()
