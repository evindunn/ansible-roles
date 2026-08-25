# crowdsec

Installs CrowdSec with the iptables firewall bouncer and optional parsers.

## How It Works

The role downloads the CrowdSec installer on the controller, copies it to the target, runs it, then installs `crowdsec` and `crowdsec-firewall-bouncer-iptables` with apt.

It starts and enables both CrowdSec services. Any parser names in `crowdsec_parsers` are installed with `cscli parsers install`.

## Defaults

`crowdsec_parsers` defaults to an empty list.
