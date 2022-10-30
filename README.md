# Minitrue
Manufacturing Truth since 1984

## What It Is
**Minitrue** is a malicious document generator that can run on Linux without having the need to install MS Office products.

## Target Audience
PEN-200 Students

## Features
- VBA Macro
- OLE (Embedded icon)
- Mouse selection
- TAB completion
- Embedded simple HTTP server to host generated documents
- Clipboard-friendly payload URLs

## Environment Setup
```sh
# NOTE: consider installing libgdiplus via apt to avoid seeing irrelevant ImportErrors
#       related to the aspose library
$ sudo apt install libgdiplus

# clone the repo into a directory of your choice
$ git clone https://github.com/X0RW3LL/Minitrue.git

# cd into the repo after it's been cloned locally
$ cd Minitrue

# install package requirements inside the packages directory
$ pip3 install -t packages/ -r requirements.txt

# grant execute permissions to the script
$ chmod +x minitrue
```
## Usage
```sh
$ ./minitrue
```

## Screenshots
[![minutrue-overview.png](https://i.postimg.cc/3JdqYJ4Q/minutrue-overview.png)](https://postimg.cc/KRhf5bD0)
[![minitrue-poc.png](https://i.postimg.cc/MZsLCjGY/minitrue-poc.png)](https://postimg.cc/F1LGcz3f)

## FAQs
- **Should I be worried about potential backdoors?**
  - The short answer: no
  - The long answer: your concerns are valid, and I encourage everyone to practice due diligence by going through the code and keeping an eye out for changes. However, I would not 1) do something unethical, and 2) jeopardize my reputation by pulling off such a silly stunt
- **How do I report bugs?**
  - You may create an issue with all the relevant bits of information; full Traceback calls, pasted payload and stack dump, and screenshots
- **What about contribution?**
  - Contribution is highly encouraged. Create a PR and we may discuss it
- **How can I contact you?**
  - You may reach out via [Twitter](https://twitter.com/X0RW3LL) or Discord: `X0RW3LL#6548`

## Credits
Special thanks to the entire Offensive-Security team, as well as the amazing community that's helped me through my journey :heart:

## Links
[Offensive-Security Official Website](https://www.offensive-security.com)\
[Offensive-Security Community Discord](https://offs.ec/discord)\
[Kali Linux & Friends Discord](https://discord.kali.org/)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F3EFYS1)
