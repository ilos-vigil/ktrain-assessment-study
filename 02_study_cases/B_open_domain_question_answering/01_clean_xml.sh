#!/bin/bash

cd /home/ilos-vigil/Desktop/TUGAS_AKHIR/studi_kasus/02_qa
source /home/ilos-vigil/Desktop/TUGAS_AKHIR/studi_kasus/.venv/bin/activate
# https://pypi.org/project/wikiextractor/

XMLPATH=$1
XMLDICT=$2
if ["$1" == ""] && ["$2" == ""];
then
    XMLPATH='./dataset/idwiki-20210301-pages-articles.xml'
    XMLDICT='./dataset/xml'
    echo "No arguments supplied, use $XMLPATH and $XMLDICT instead"
fi

python -m wikiextractor.WikiExtractor $XMLPATH -b 10000000 -o $XMLDICT --processes 11 > ./dataset/debug_wikiextactor.log 2>&1
