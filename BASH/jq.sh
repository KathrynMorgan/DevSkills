#!/bin/bash
# filter for packages in the class "monitoring"

list_SOURCE=$2
show_CLASS=$1

jq -r --arg search $show_CLASS '.[$search][] | "\(.name)"' "$list_SOURCE"


