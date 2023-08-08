import uvicorn, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--env', required=True)

args = parser.parse_args()

os.environ['ENV'] = args.env

ssl_keyfile = None
ssl_certfile = None

reload = True

if args.env == 'production':
    ssl_keyfile = ''
    ssl_certfile = ''

    reload = False

if __name__ == "__main__":
    uvicorn.run(
        app='src.app:asgi',
        host='0.0.0.0',
        port=8000,
        ssl_certfile=ssl_certfile,
        ssl_keyfile=ssl_keyfile,

        reload=reload
    )
