import uvicorn, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--env', required=True)

args = parser.parse_args()

os.environ['ENV'] = args.env

ssl_keyfile = None
ssl_certfile = None

if args.env == 'production':
    ssl_keyfile = ''
    ssl_certfile = ''

if __name__ == "__main__":
    uvicorn.run(
        app='app:asgi',
        host='0.0.0.0',
        workers=4 if args.env == 'production' else 1,
        port=6400,
        reload=args.env == 'development',
        ssl_certfile=ssl_certfile,
        ssl_keyfile=ssl_keyfile
    )