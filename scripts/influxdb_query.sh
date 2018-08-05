HOST=localhost

# Query last 60 min
curl -G "http://$HOST:8086/query?pretty=true" \
  --data-urlencode "db=test" \
  --data-urlencode "q=SELECT \"soil_temperature_c\", \"VWC\" FROM \"test\" WHERE \"id\"='4DAD64' AND time > now() - 60m"

# Query last 20 row
curl -G "http://$HOST:8086/query?pretty=true" \
  --data-urlencode "db=test" \
  --data-urlencode "q=SELECT \"soil_temperature_c\", \"VWC\" FROM \"test\" WHERE \"id\"='4DAD64' ORDER BY time DESC LIMIT 20"

