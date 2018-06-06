#!/bin/bash
# Deep-Clean.sh
# set -x

#################################################################################
#
# Usage:
#  deep-clean /vol/win/batch/MedRxProvData
#
# Find log at:
#  /tmp/deep-clean/
#
#################################################################################
## Read Command Arguments
clean_TARGET="$1"

#################################################################################
## Switches
  
  ## Delete Switch [true|false]
  delete_ALL="true"
  
  ## Logging Switch [true|false]
  log_DBG="true"
  ## Logging Save Switch [true|false]
  log_SAVE="true"

  ## Logging Variables
  log_DATE=$(date +%Y/%m/%d:%H:%M:%S)
  log_DEST="/tmp/deep-clean/${clean_TARGET}/"
  log_NAME="$log_DEST/run-clean_${log_DATE}.log"

#################################################################################
## 
log_save () {
    echo "$running_FUNC $prnt_MSG" >>${log_NAME}
}

#################################################################################
## Run Logging Func(s)
log_op () {
if [[ $log_DBG = "true"  ]]; then
    case $1 in
        0) prnt_MSG="$2";
            echo "Running $running_FUNC $prnt_MSG";
            [[ $log_SAVE = "false" ]] || log_save
            ;;
        *) echo "Unhandled Error"
           echo "Failed during $running_FUNC"
           exit 1
           ;;
    esac
fi
}

#################################################################################
## Remove Item
## Will only log item if 'delete_ALL' set to 'false'
rm_item () {
    log_op 0 "Removing $old"
    [[ ! $delete_ALL = "true" ]] || rm $old
}

#################################################################################
## Filter by pattern(s)
## TODO: convert patterns into array for matching from command line argument
rm_filter () {    
for old in $(find $1 \( -name "*2009*" -o -name "*2010*" -o -name "*2011*" -o -name "*2012*" -o -name "*2013*" -o -name "*2014*" -o -name "*2015*" \) -type d); do
    rm_match $old
done
}

#################################################################################
## Find Directories by depth
rm_find () {
for item in $(find ${clean_TARGET} -maxdepth 2 -mindepth 2 -type d); do
    rm_DIR=${item}
    rm_filter $rm_DIR
done
}

#################################################################################
## Main Function
main () {
running_FUNC="main"

    rm_find

}

main
