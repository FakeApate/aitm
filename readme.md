# Modifier-in-the-Middle

To demonstrate how easily 2FA can be bypassed, I wrote this Addon for [mitmproxy](https://mitmproxy.org/).

## How to Run

- Create a virtual environment (venv).
- Check out the latest release of mitmproxy (it's included as a submodule in this repo).
- Build & install mitmproxy. Double-check to ensure it's really installed in the venv.
- Create a certificate for your domain.
- Replace my domain with yours in `aitm_config.py`.
- Run `python -m aitm` and browse your site.
- Use a cookie editor extension for your browser to insert the captured session

## Disclaimer

Please read the [DISCLAIMER](./DISCLAIMER.md) file before using this software.