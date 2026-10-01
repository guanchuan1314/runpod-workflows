import argparse
import base64
import json
import os
import pathlib
import time
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', required=True)
    args = parser.parse_args()
    key = os.environ['RUNPOD_API_KEY']
    endpoint = os.environ.get('RUNPOD_ENDPOINT_ID', 'ojli7psn8voa05')
    if not endpoint.isalnum():
        raise ValueError('Invalid endpoint ID')
    root = pathlib.Path(__file__).resolve().parent
    workflow = json.loads((root / 'workflow-api.json').read_text(encoding='utf-8-sig'))
    workflow['452']['inputs']['prompt'] = args.prompt
    def call(path, body=None):
        request = urllib.request.Request(
            f'https://api.runpod.ai/v2/{endpoint}/{path}',
            data=json.dumps(body).encode() if body is not None else None,
            headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)
    job = call('run', {'input': {'workflow': workflow}})
    job_id = job['id']
    print('Job:', job_id, flush=True)
    deadline = time.monotonic() + 1800
    while time.monotonic() < deadline:
        result = call(f'status/{job_id}')
        status = result['status']
        if status == 'COMPLETED':
            output = root / 'generated' / job_id
            output.mkdir(parents=True, exist_ok=True)
            (output / 'result.json').write_text(json.dumps(result))
            for index, item in enumerate(result.get('output', {}).get('images', [])):
                if item.get('type') == 'base64':
                    name = pathlib.Path(item.get('filename', f'image-{index}.png')).name
                    if name in ('', '.', '..'):
                        name = f'image-{index}.png'
                    (output / name).write_bytes(base64.b64decode(item['data'], validate=True))
            print('Saved:', output)
            return
        if status in ('FAILED', 'CANCELLED', 'TIMED_OUT'):
            raise RuntimeError(f'Job {job_id}: {status}: {result.get("error", "")}')
        time.sleep(5)
    raise TimeoutError(f'Job {job_id} may still be running. Check or cancel in RunPod console.')

if __name__ == '__main__':
    main()
