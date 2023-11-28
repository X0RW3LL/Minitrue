# Minitrue
Manufacturing Truth since 1984

## What It Is
**Minitrue** is a malicious document generator that can run on Linux natively without having the need to install MS Office products

## Disclaimer

This tool is designed to help make maldoc generation easier for you. However, I highly recommend **NOT** skipping the manual method taught in the PEN-200 course materials

## Target Audience

PEN-200 learners

## Features

- VBA Macro
- OLE (Embedded icon)
- Mouse selection
- TAB completion
- Embedded simple HTTP server to host generated documents
- Clipboard-friendly payload URLs

## Project Dependencies

- libicu63 (manually downloaded and installed via apt. Credit to [@securingdev](https://github.com/securingdev) for bringing [this issue](https://github.com/X0RW3LL/Minitrue/issues/1)  to my attention)
- libssl1.1 (built from source)
- libgdiplus (apt)
- aspose-words (pypi)
- prompt_toolkit (pypi)

## Setup

```sh
kali@kali:~$ git clone https://github.com/X0RW3LL/Minitrue.git
kali@kali:~$ cd Minitrue
kali@kali:~/Minitrue$ ./setup.sh 
```

## Usage

```sh
kali@kali:~/Minitrue$ ./minitrue
```

## Screenshots
[![minutrue-overview.png](https://i.postimg.cc/3JdqYJ4Q/minutrue-overview.png)](https://postimg.cc/KRhf5bD0)
[![minitrue-poc.png](https://i.postimg.cc/MZsLCjGY/minitrue-poc.png)](https://postimg.cc/F1LGcz3f)

## FAQs
- **Should I be worried about potential backdoors?**
  - The short answer: No
  - The long answer: No. Your concerns are valid, however, and I encourage everyone to practice due diligence by going through the code and keeping an eye out for changes. 
- **How do I report bugs?**
  - You may create an issue with all the relevant details
- **What about contributions?**
  - Contribution is highly encouraged. Create a PR and we may discuss it
- **How can I contact you?**
  - You may reach out via [Twitter](https://twitter.com/X0RW3LL) or Discord: `@x0rw3ll`

## Credits
Special thanks to the entire OffSec team, as well as the amazing community that's helped me through my journey :heart:

## Links
[OffSec Official Website](https://www.offsec.com)\
[OffSec Community Discord](https://offs.ec/discord)\
[Kali Linux & Friends Discord](https://discord.kali.org/)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F3EFYS1)
