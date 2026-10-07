#!/bin/bash

# Scan OS packages and email critical findings to configured recipients.
set -euo pipefail
umask 077

source '/etc/trivy-scan.conf'
HOST_NAME="$(hostname)"
REPORT_DIRECTORY="$(mktemp -d '/tmp/trivy-critical-reports.XXXXXXXX')"
trap 'rm -rf -- "$REPORT_DIRECTORY"' EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

RUN_STATUS=0

# Scan OS packages and report critical findings.
run_scan() {
    local scan_name="$1"
    local report_file="$REPORT_DIRECTORY/report.txt"
    local scan_status=0
    shift

    # Reserve exit code 10 for findings so scan errors cannot trigger an alert.
    trivy "$@" --scanners 'vuln' --severity 'CRITICAL' --exit-code 10 \
        --format 'table' --output "$report_file" || scan_status=$?

    case "$scan_status" in
        0)
            ;;
        10)
            if ! mail -s "ALERT: Critical CVEs Detected on $HOST_NAME [$scan_name]" \
                "${EMAILS[@]}" < "$report_file"; then
                printf 'Mail delivery failed for %s\n' "$scan_name" >&2
                RUN_STATUS=1
            fi
            ;;
        *)
            printf 'Trivy scan failed for %s with exit code %s\n' "$scan_name" "$scan_status" >&2
            RUN_STATUS=1
            ;;
    esac
    rm -f -- "$report_file"
}

run_scan 'OS' rootfs --pkg-types 'os' '/'

exit "$RUN_STATUS"
