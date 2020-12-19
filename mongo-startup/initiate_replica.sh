#!/bin/bash

echo "Starting replica set initialize"
until mongo --host mongodb1 --eval "print(\"waited for connection\")" && mongo --host mongodb2 --eval "print(\"waited for connection 2\")"
do
    sleep 2
done
echo "Connection finished"
echo "Creating replica set"
mongo --host mongodb1 <<EOF
rs.initiate(
  {
    _id : 'rs0',
    members: [
      { _id : 0, host : "mongodb1:27017"},
      { _id : 1, host : "mongodb2:27017"},
      
    ]
  }
)

rs.stepDown()
EOF
echo "replicas created & replica2 set to primary"

