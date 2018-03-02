#!/bin/bash
# filter for packages in the class "monitoring"

list_SOURCE=$1
show_CLASS=$2

jq -r '.monitoring[] | "\(.name)"' "$list_SOURCE"


