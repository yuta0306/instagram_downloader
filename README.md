# Instagrm_downloader

You can download images on instagram.

# Set up

INSTAGRAM_USER: Username or Phone number
INSTAGRAM_PASS: Password


```bash
pip install -r requirements.txt
```

# Usage

```python
python instagram.py 'hashtag name'
```

# Warning

When the version of chrome-driver-binary, Python library, is **not same** as your Google Chrome version,  
This could not be run.

In that case, you should check your chrome version and then run the pip command below.

```bash
pip install chrome-driver-binary=='Your version'
```