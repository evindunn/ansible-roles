# trivy

Installs Trivy from the official Aqua Security apt repository and a mailx provider on Debian and Ubuntu.

## Example

```yml
- hosts: servers
  become: true
  roles:
    - role: trivy
      trivy_emails:
        - alerts@example.com
        - admin@example.com
```

## Defaults

`trivy_mail_package` defaults to `bsd-mailx`, which provides the `mailx` command.

`trivy_emails` is a required nonempty list of recipients and replaces the previous `trivy_email` variable. A root cron job scans `/` with `trivy rootfs` for CRITICAL OS-package vulnerabilities each day at 03:00 in the host's local time. Set `trivy_cron_hour` and `trivy_cron_minute` to change the schedule.

The job emails an OS table report with critical findings to every recipient. Scan failures do not send vulnerability alerts. Scan or mail delivery failures return a failure status. Temporary reports use unique private files and are removed when the script exits. Repeated findings send an alert each day.

Configure the host's mail transport to deliver outbound email. The role installs the mail client but does not configure SMTP delivery.

The role stores the ASCII-armored repository signing key at `/usr/share/keyrings/trivy.asc` and writes `/etc/apt/sources.list.d/trivy.list` with the upstream `generic` suite. It uses Ansible modules without shell pipelines or GPG conversion.

See the [official installation instructions](https://github.com/aquasecurity/trivy/blob/main/docs/getting-started/installation.md).
