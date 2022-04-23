cat ${1} | python3 "src/mapper.py" | sort | python3 "src/reducer.py" > ${2}
