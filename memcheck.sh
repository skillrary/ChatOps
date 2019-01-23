used=$(top -l 1 -s 0 | awk ' /PhysMem/ {print}'| awk '{print $2}' | sed 's/[^0-9]*//g') 

text=currentmemory
check=$used$text
myst=$text$used
echo $myst
if [[ "$used" -ge 7000  ]]; then
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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
fi

exit 0
