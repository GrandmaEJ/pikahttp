# 🚀 pikahttp

[![CI](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml/badge.svg)](https://github.com/GrandmaEJ/pikahttp/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/pikahttp.svg)](https://pypi.org/project/pikahttp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/pikahttp.svg)](https://pypi.org/project/pikahttp/)

> Python এর জন্য একটি অসাধারণ দ্রুত HTTP ক্লায়েন্ট, Rust এবং Hyper দ্বারা চালিত।

`pikahttp` Python এর ব্যবহারের সহজতা এবং Rust এর কর্মক্ষমতা একত্রিত করে, একটি সহজ কিন্তু শক্তিশালী HTTP ক্লায়েন্ট প্রদান করে যা ঐতিহ্যগত Python HTTP লাইব্রেরির তুলনায় ১৮% পর্যন্ত দ্রুত।

---

## ✨ বৈশিষ্ট্য

* ⚡ **অতি-দ্রুত**: সর্বোচ্চ কর্মক্ষমতার জন্য Rust এবং Hyper দিয়ে নির্মিত
* 🔄 **সহজ**: পরিষ্কার, স্বজ্ঞাত Python API যা পরিচিত প্যাটার্ন ব্যবহার করে
* 🛡️ **নির্ভরযোগ্য**: হুডের নিচে যুদ্ধ-পরীক্ষিত Rust লাইব্রেরি
* 💾 **দক্ষ**: ন্যূনতম মেমরি বরাদ্দ এবং শূন্য-কপি অপারেশন
* 🔒 **নিরাপদ**: ডিজাইন অনুযায়ী থ্রেড-নিরাপদ এবং মেমরি-নিরাপদ
* 🚀 **Async-First**: সম্পূর্ণ অ্যাসিঙ্ক্রোনাস HTTP অনুরোধ সহ sync সুবিধা
* 🌐 **HTTP/2 প্রস্তুত**: স্থানীয় HTTP/2 সাপোর্ট
* 📦 **সেশন ম্যানেজমেন্ট**: সংযোগ повтор ব্যবহারের জন্য বিল্ট-ইন সেশন সাপোর্ট
* 🔧 **কাস্টমাইজযোগ্য**: ব্যাপক হেডার, প্যারামিটার এবং বডি সাপোর্ট

---

## 🔧 ইনস্টলেশন

### PyPI থেকে (প্রস্তাবিত)
```bash
pip install pikahttp
```

### সোর্স থেকে
```bash
git clone https://github.com/GrandmaEJ/pikahttp.git
cd pikahttp
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pip install maturin
maturin develop
```

### ডেভেলপমেন্ট ইনস্টলেশন
```bash
# ডেভেলপমেন্ট মোডে লাইভ রিলোডিং সহ ইনস্টল করুন
maturin develop --features="pyo3/extension-module"
```

---

## 🚀 দ্রুত শুরু

### সেশন দিয়ে বেসিক ব্যবহার

```python
from pikahttp import Session
import json

# একটি সেশন তৈরি করুন
session = Session()

# GET অনুরোধ
response = session.request(
    "GET",
    "https://httpbin.org/get",
    headers={"User-Agent": "pikahttp/0.1.0"}
)
print(f"Status code: {response['status_code']}")
print(f"Content: {response['content']}")
```

### সুবিধার পদ্ধতি ব্যবহার করে

```python
from pikahttp import Session

# একটি সেশন তৈরি করুন
session = Session()

# GET অনুরোধ
response = session.get("https://api.github.com/zen")
print(f"Status: {response['status_code']}")
print(f"Headers: {response['headers']}")

# JSON সহ POST অনুরোধ
data = {"hello": "world", "test": True}
response = session.post(
    "https://httpbin.org/post",
    headers={"Content-Type": "application/json"},
    body=json.dumps(data)
)
print(f"Response: {response['content']}")
```

### উন্নত ব্যবহার

```python
from pikahttp import Session
import json

session = Session()

# কাস্টম হেডার
headers = {
    "User-Agent": "pikahttp/0.1.0",
    "Accept": "application/json",
    "X-Custom-Header": "custom-value"
}

# কাস্টম হেডার দিয়ে GET
response = session.request(
    "GET",
    "https://api.github.com/users/octocat",
    headers=headers
)

# JSON ডেটা দিয়ে POST
post_data = {
    "title": "Test Post",
    "body": "This is a test post using pikahttp"
}
response = session.post(
    "https://jsonplaceholder.typicode.com/posts",
    headers={
        "Content-Type": "application/json",
        "User-Agent": "pikahttp/0.1.0"
    },
    body=json.dumps(post_data)
)

print(f"Created post with status: {response['status_code']}")
```

---

## 📊 পারফরম্যান্স বেঞ্চমার্ক

প্রতিটি ১০০টি অনুরোধ সহ বেঞ্চমার্কের উপর ভিত্তি করে:

| লাইব্রেরি  | গড় (s) | মধ্যমা (s) | ন্যূনতম (s) | সর্বোচ্চ (s) | স্ট্যান্ডার্ড বিচ্যুতি (s) |
| -------- | -------- | ---------- | ------- | ------- | ---------- |
| urllib   | 0.2389   | 0.2351     | 0.2291  | 0.6488  | 0.0415     |
| requests | 0.2590   | 0.2575     | 0.2524  | 0.3014  | 0.0071     |
| pikahttp | 0.2193   | 0.2202     | 0.2162  | 0.2252  | 0.0021     |

### পারফরম্যান্স হাইলাইট

* 🚀 `requests` এর চেয়ে **১৮.১% দ্রুত**
* 🎯 `urllib` এর চেয়ে **৮.৯% দ্রুত**
* 📊 আরো সামঞ্জস্যপূর্ণ পারফরম্যান্স (৬০% কম স্ট্যান্ডার্ড বিচ্যুতি)
* ⚡ সংকলিত Rust কোডের কারণে দ্রুত স্টার্টআপ সময়
* 💾 কম মেমরি পদচিহ্ন

---

## 🏗️ আর্কিটেকচার

### প্রযুক্তির স্ট্যাক

- **কোর**: Hyper HTTP লাইব্রেরি সহ Rust
- **বাইন্ডিং**: Python ইন্টিগ্রেশনের জন্য PyO3
- **রানটাইম**: Async এক্সিকিউশনের জন্য Tokio
- **প্রোটোকল**: HTTP/1.1 এবং HTTP/2 সাপোর্ট
- **নিরাপত্তা**: স্থানীয় সার্টিফিকেট সহ TLS/HTTPS

### ডিজাইন নীতি

1. **পারফরম্যান্স প্রথম**: প্রতিটি অপারেশন গতির জন্য অপ্টিমাইজড
2. **মেমরি নিরাপত্তা**: Rust এর মালিকানা ব্যবস্থা সাধারণ বাগ প্রতিরোধ করে
3. **শূন্য-কপি**: Rust এবং Python এর মধ্যে ডেটা কপিং ন্যূনতম রাখুন
4. **ডিফল্ট Async**: সর্বোচ্চ থ্রোপুটের জন্য অ-ব্লকিং I/O
5. **সহজ API**: সহজে শেখার জন্য Pythonic ইন্টারফেস

### মডিউল স্ট্রাকচার

```
pikahttp/
├── src/
│   ├── lib.rs              # Python মডিউল ডেফিনিশন
│   ├── runtime.rs          # গ্লোবাল async রানটাইম এবং HTTP ক্লায়েন্ট
│   ├── types.rs            # ত্রুটির ধরন এবং ফলাফলের ধরন
│   └── client/
│       ├── mod.rs          # ক্লায়েন্ট মডিউল এক্সপোর্ট
│       └── session.rs      # কোর সেশন বাস্তবায়ন
├── python/pikahttp/
│   └── __init__.py         # উচ্চ-স্তর Python API
├── examples/               # ব্যবহারের উদাহরণ
├── tests/                  # টেস্ট সুইট
└── benchmark.py           # পারফরম্যান্স বেঞ্চমার্ক
```

---

## 🔧 API রেফারেন্স

### সেশন ক্লাস

#### `Session()`

একটি নতুন HTTP সেশন তৈরি করে।

```python
session = Session()
```

#### `request(method, url, headers=None, body=None)`

একটি সাধারণ HTTP অনুরোধ তৈরি করে।

**প্যারামিটার:**
- `method` (str): HTTP পদ্ধতি (GET, POST, PUT, DELETE, ইত্যাদি)
- `url` (str): টার্গেট URL
- `headers` (dict, ঐচ্ছিক): HTTP হেডার
- `body` (str, ঐচ্ছিক): অনুরোধের বডি

**রিটার্ন:**
- `dict`: `status_code`, `headers` এবং `content` সহ প্রতিক্রিয়া

**উদাহরণ:**
```python
response = session.request("GET", "https://api.example.com/data")
print(response["status_code"])  # 200
print(response["content"])      # বাইট বিষয়বস্তু
```

#### `get(url, headers=None)`

GET অনুরোধের জন্য সুবিধার পদ্ধতি।

```python
response = session.get("https://api.example.com/users")
```

#### `post(url, headers=None, body=None)`

POST অনুরোধের জন্য সুবিধার পদ্ধতি।

```python
response = session.post(
    "https://api.example.com/users",
    headers={"Content-Type": "application/json"},
    body='{"name": "John"}'
)
```

### প্রতিক্রিয়া অবজেক্ট

প্রতিক্রিয়া একটি অভিধান যার নিম্নলিখিত স্ট্রাকচার রয়েছে:

```python
{
    "status_code": 200,           # HTTP স্ট্যাটাস কোড
    "headers": {...},             # প্রতিক্রিয়া হেডার
    "content": b"..."             # কাঁচা বাইট বিষয়বস্তু
}
```

---

## 🧪 টেস্টিং

### টেস্ট চালানো

```bash
# ডেভেলপমেন্ট নির্ভরতা ইনস্টল করুন
pip install -r requirements-dev.txt

# টেস্ট সুইট চালান
pytest tests/

# কভারেজ সহ চালান
pytest tests/ --cov=pikahttp

# নির্দিষ্ট টেস্ট ফাইল চালান
pytest tests/test_requests.py
```

### টেস্ট কভারেজ

টেস্ট সুইটে অন্তর্ভুক্ত:
- ✅ GET এবং POST অনুরোধ হ্যান্ডলিং
- ✅ কাস্টম হেডার সাপোর্ট
- ✅ JSON পেলোড হ্যান্ডলিং
- ✅ ত্রুটি হ্যান্ডলিং এবং এজ কেস
- ✅ সেশন ম্যানেজমেন্ট
- ✅ মক সার্ভার ইন্টিগ্রেশন

### বেঞ্চমার্কিং

```bash
# পারফরম্যান্স বেঞ্চমার্ক চালান
python benchmark.py

# কাস্টম বেঞ্চমার্ক সেটিংস
python benchmark.py --requests 1000 --concurrent 10
```

---

## 🔒 নিরাপত্তা ও নির্ভরযোগ্যতা

### নিরাপত্তা বৈশিষ্ট্য

* **TLS/HTTPS সাপোর্ট**: সঠিক সার্টিফিকেট ভ্যালিডেশন সহ স্থানীয় TLS বাস্তবায়ন
* **মেমরি নিরাপত্তা**: Rust বাফার ওভারফ্লো এবং মেমরি লিক প্রতিরোধ করে
* **থ্রেড নিরাপত্তা**: শেয়ার্ড রিসোর্সে নিরাপদ কনকারেন্ট অ্যাক্সেস
* **ইনপুট ভ্যালিডেশন**: সকল ইনপুট এবং প্যারামিটারের সঠিক ভ্যালিডেশন

### নির্ভরযোগ্যতা বৈশিষ্ট্য

* **কানেকশন পুলিং**: HTTP সংযোগের দক্ষ повтор ব্যবহার
* **টাইমআউট হ্যান্ডলিং**: অনুরোধের জন্য কনফিগারযোগ্য টাইমআউট
* **ত্রুটি পুনরুদ্ধার**: নেটওয়ার্ক ত্রুটির নম্র হ্যান্ডলিং
* **প্রোটোকল সম্মতি**: সম্পূর্ণ HTTP/1.1 এবং HTTP/2 সম্মতি

### সর্বোত্তম অনুশীলন

1. **সেশন ব্যবহার করুন**: ভাল পারফরম্যান্সের জন্য সেশন повтор ব্যবহার করুন
2. **টাইমআউট সেট করুন**: সর্বদা উপযুক্ত টাইমআউট কনফিগার করুন
3. **ত্রুটি হ্যান্ডল করুন**: স্ট্যাটাস কোড পরীক্ষা করুন এবং ব্যতিক্রম হ্যান্ডল করুন
4. **প্রতিক্রিয়া যাচাই করুন**: প্রক্রিয়াকরণের আগে প্রতিক্রিয়া ডেটা যাচাই করুন

---

## 📋 উদাহরণ

### বেসিক GET অনুরোধ
```python
from pikahttp import Session

session = Session()
response = session.get("https://httpbin.org/get")
print(f"Status: {response['status_code']}")
```

### JSON সহ POST
```python
import json
from pikahttp import Session

session = Session()
data = {"name": "John", "email": "john@example.com"}

response = session.post(
    "https://httpbin.org/post",
    headers={"Content-Type": "application/json"},
    body=json.dumps(data)
)
```

### কাস্টম হেডার
```python
from pikahttp import Session

session = Session()
headers = {
    "User-Agent": "MyApp/1.0",
    "Authorization": "Bearer your-token-here",
    "Accept": "application/json"
}

response = session.get(
    "https://api.example.com/protected",
    headers=headers
)
```

### ত্রুটি হ্যান্ডলিং
```python
from pikahttp import Session

session = Session()

try:
    response = session.get("https://httpbin.org/status/500")
    if response['status_code'] >= 400:
        print(f"Error: {response['status_code']}")
except Exception as e:
    print(f"Request failed: {e}")
```

---

## 🚀 উন্নত ব্যবহার

### কানেকশন পুলিং

pikahttp স্বয়ংক্রিয়ভাবে কানেকশন পুলিং হ্যান্ডল করে:

```python
from pikahttp import Session

# সেশন তৈরি করুন (স্বয়ংক্রিয়ভাবে সংযোগ পুল করে)
session = Session()

# একাধিক অনুরোধ সংযোগ повтор ব্যবহার করে
for i in range(100):
    response = session.get(f"https://api.example.com/item/{i}")
    # সংযোগগুলি স্বয়ংক্রিয়ভাবে повтор ব্যবহার করা হয়
```

### পারফরম্যান্স অপ্টিমাইজেশন টিপস

1. **সেশন повтор ব্যবহার করুন**: একটি সেশন তৈরি করুন এবং এটি повтор ব্যবহার করুন
2. **ব্যাচ অনুরোধ**: সম্পর্কিত অনুরোধ একসাথে গোষ্ঠী করুন
3. **Keep-Alive ব্যবহার করুন**: অনুরোধের মধ্যে সংযোগ সক্রিয় রাখুন
4. **মেমরি মনিটর করুন**: বড় প্রতিক্রিয়া সম্ভব হলে স্ট্রিম করা উচিত

### ত্রুটি হ্যান্ডলিং প্যাটার্ন

```python
from pikahttp import Session

def robust_request(session, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = session.get(url)
            if 200 <= response['status_code'] < 300:
                return response
            else:
                print(f"HTTP {response['status_code']}")
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                raise
    return None
```

---

## 🔧 ডেভেলপমেন্ট

### ডেভেলপমেন্ট পরিবেশ সেটআপ

```bash
git clone https://github.com/GrandmaEJ/pikahttp.git
cd pikahttp

# ভার্চুয়াল পরিবেশ তৈরি করুন
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# ডেভেলপমেন্ট নির্ভরতা ইনস্টল করুন
pip install -r requirements-dev.txt

# ডেভেলপমেন্ট মোডে pikahttp ইনস্টল করুন
pip install maturin
maturin develop
```

### কোড গুণমান

```bash
# Rust কোড ফরম্যাট করুন
cargo fmt

# Rust কোড চেক করুন
cargo clippy

# Python কোড ফরম্যাট করুন
black python/ tests/ examples/

# Python কোড লিন্ট করুন
flake8 python/ tests/ examples/

# Python কোড টাইপ চেক করুন
mypy python/
```

### প্রোডাকশনের জন্য বিল্ড

```bash
# রিলিজ বিল্ড
maturin build --release

# নির্দিষ্ট Python সংস্করণের জন্য বিল্ড
maturin build --release --python=python3.11

# হুইল প্যাকেজ বিল্ড
maturin build --release --out wheels
```

---

## 📦 ডিপ্লয়মেন্ট

### Docker ডিপ্লয়মেন্ট

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["python", "-m", "pikahttp"]
```

### প্রোডাকশন বিবেচনা

1. **নির্ভরতা ব্যবস্থাপনা**: পুনরুৎপাদনযোগ্যতার জন্য সংস্করণ পিন করুন
2. **রিসোর্স সীমা**: মেমরি এবং CPU ব্যবহার মনিটর করুন
3. **কানেকশন সীমা**: উপযুক্ত কানেকশন পুলিং কনফিগার করুন
4. **মনিটরিং**: অনুরোধ/প্রতিক্রিয়া সময় এবং ত্রুটি হার লগ করুন

---

## 🤝 অবদান

### শুরু করা

1. রিপোজিটরি ফোর্ক করুন
2. একটি ফিচার ব্রাঞ্চ তৈরি করুন: `git checkout -b feature/amazing-feature`
3. আপনার পরিবর্তনগুলি করুন
4. টেস্ট চালান: `pytest tests/`
5. আপনার পরিবর্তন কমিট করুন: `git commit -m 'Add amazing feature'`
6. ব্রাঞ্চে পুশ করুন: `git push origin feature/amazing-feature`
7. একটি Pull Request খুলুন

### ডেভেলপমেন্ট নির্দেশিকা

* Rust এবং Python স্টাইল গাইড অনুসরণ করুন
* নতুন ফিচারের জন্য ব্যাপক টেস্ট লিখুন
* API পরিবর্তনের জন্য ডকুমেন্টেশন আপডেট করুন
* PR জমা দেওয়ার আগে সমস্ত টেস্ট পাস হওয়া নিশ্চিত করুন
* পারফরম্যান্স-ক্রিটিক্যাল পরিবর্তনের জন্য বেঞ্চমার্ক যোগ করুন

### বাগ রিপোর্ট

অনুগ্রহ করে ইস্যু ট্র্যাকার ব্যবহার করুন:
- সমস্যার স্পষ্ট বর্ণনা
- পুনরুত্পাদনের ধাপ
- প্রত্যাশিত vs প্রকৃত আচরণ
- পরিবেশের বিবরণ (Python সংস্করণ, OS, ইত্যাদি)

---

## 📄 লাইসেন্স

MIT লাইসেন্স। বিস্তারিত জানার জন্য [LICENSE](LICENSE) দেখুন।

---

## 📞 সাপোর্ট

- **ডকুমেন্টেশন**: [GitHub Wiki](https://github.com/GrandmaEJ/pikahttp/wiki)
- **ইস্যু**: [GitHub Issues](https://github.com/GrandmaEJ/pikahttp/issues)
- **আলোচনা**: [GitHub Discussions](https://github.com/GrandmaEJ/pikahttp/discussions)
- **ইমেইল**: [যোগাযোগের তথ্য](mailto:support@pikahttp.dev)

---

## 🙏 স্বীকৃতি

- **Hyper**: Rust এর জন্য উচ্চ-পারফরম্যান্স HTTP লাইব্রেরি
- **PyO3**: Rust এর জন্য Python বাইন্ডিং
- **Tokio**: Rust এর জন্য async রানটাইম
- **Python কমিউনিটি**: ফিডব্যাক এবং অবদানের জন্য

---

**[English Documentation](README.en.md)** | Bengali Version