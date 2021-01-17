#!/bin/bash

echo "Starting replica set initialize"
echo "$MONGODB2"
echo "$MONGODB1"
until mongo --host mongodb1 --eval "print(\"waited for connection\")" && mongo --host mongodb2  --eval "print(\"waited for connection 2\")"
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
EOF
echo "replicas created"
sleep 10
echo "setting mongodb2 as primary ..."
mongo --host mongodb1 <<EOF
rs.stepDown()
EOF

echo "set mongodb2 as primary"


sleep 10 

mongo --host mongodb2 <<EOF
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[1].priority = 1
rs.reconfig(cfg)
EOF

echo "changed voting rights to favour mongodb2"