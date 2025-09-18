#!/usr/bin/env bash
set -euo pipefail
: "${AZURE_MAPS_KEY:?Set AZURE_MAPS_KEY env var}"

src="sdrc_navigation/config/gps_wpf_demo.mvc.template"
dst="sdrc_navigation/config/gps_wpf_demo.mvc"

# shellcheck disable=SC1090
source "$src"
printf 'URL=%s&subscription-key=%s\n' "$URL_BASE" "$AZURE_MAPS_KEY" > "$dst"
echo "Rendered $dst"
