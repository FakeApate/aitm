# Modifier/Adversairy in the Middle

To demonstrate how easily 2FA can be bypassed, I wrote this Addon for [mitmproxy](https://mitmproxy.org/).

Moved project to my org: [rednet-sec-aitm](https://github.com/RedNoodlesOrg/rednet-sec-aitm)

## How to Run

- install packages `pipenv install`.
- Create a certificate for your domain. For example with certbot.
- Replace my domain with yours in `aitm_config.py`.
- Run `python -m aitm` and browse your site.
- After capturing the session, you can use it to add another MFA Token on the [Account](https://mysignins.microsoft.com/security-info)

## Disclaimer

Please read the [DISCLAIMER](./DISCLAIMER.md) file before using this software.
