# Minitrue
Manufacturing Truth since 1984

## What It Is
**Minitrue** is a malicious document generator that can run on Linux without having the need to install MS Office products

## Disclaimer
This tool is designed to help make the maldoc generation easier for you. However, I highly recommend **NOT** skipping the manual method taught in the PEN-200 course materials

## Target Audience
PEN-200 Students

## Features
- VBA Macro
- OLE (Embedded icon)
- Mouse selection
- TAB completion
- Embedded simple HTTP server to host generated documents
- Clipboard-friendly payload URLs

## Project Dependencies
Aspose.Words relies on a specific version of ICU (libicu63) for unicode/ico support\
However, this package is no longer in the Kali repos, so we have to install it manually from the Debian buster repo

- Navigate to https://packages.debian.org/buster/amd64/libicu63/download
- Download the libicu63 package using any of the listed mirrors
- Verify the package SHA256 checksum
- Install the package
- Install libssl dependencies

```sh
# Download libicu63
kali@kali:~$ wget http://ftp.us.debian.org/debian/pool/main/i/icu/libicu63_63.1-6+deb10u3_amd64.deb

# Verify SHA256 checksum one-liner
# Provided SHA256 hash is 38f65aaec4ee088f65330cf636c1cd6edef38109c80559836ecf38e2390a5761 at the time of writing this guide
kali@kali:~$ [ "$(sha256sum libicu63_63.1-6+deb10u3_amd64.deb | cut -d ' ' -f1)" == "38f65aaec4ee088f65330cf636c1cd6edef38109c80559836ecf38e2390a5761" ] && echo '[+] SHA256 checksum OK' || echo "[-] SHA256 checksum mismatch"

kali@kali:~$ sudo apt install ./libicu63_63.1-6+deb10u3_amd64.deb
kali@kali:~$ sudo apt update && sudo apt install libssl-dev libssl1.1
```
#### *Note for future readers*
I have archived the download page and package in case the link goes dead at any point
- [Debian package download page](https://web.archive.org/web/20221102093638/https%3A%2F%2Fpackages.debian.org%2Fbuster%2Famd64%2Flibicu63%2Fdownload)
- [libicu63_63.1-6+deb10u3_amd64.deb - [North America Mirror]](https://web.archive.org/web/20221102103704/http%3A%2F%2Fftp.ca.debian.org%2Fdebian%2Fpool%2Fmain%2Fi%2Ficu%2Flibicu63_63.1-6%252Bdeb10u3_amd64.deb)

Credit to [@securingdev](https://github.com/securingdev) for bringing [this issue](https://github.com/X0RW3LL/Minitrue/issues/1)  to my attention

## Environment Setup
```sh
# NOTE: consider installing libgdiplus via apt to avoid seeing irrelevant ImportErrors
#       related to the aspose library
kali@kali:~$ sudo apt install libgdiplus

# clone the repo into a directory of your choice
kali@kali:~$ git clone https://github.com/X0RW3LL/Minitrue.git

# cd into the repo after it's been cloned locally
kali@kali:~$ cd Minitrue

# install package requirements inside the packages directory
kali@kali:~/Minitrue$ pip3 install -t packages/ -r requirements.txt

# grant execute permissions to the script
kali@kali:~/Minitrue$ chmod +x minitrue
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
