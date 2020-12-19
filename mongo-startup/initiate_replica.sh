#!/bin/bash

echo "Starting replica set initialize"
until mongo --host mongodb1 --eval "print(\"waited for connection\")"
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
sleep 7
#  setting mongodb2 as PRIMARY
mongo --host mongodb1 <<EOF
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[1].priority = 1
rs.reconfig(cfg)
EOF
echo "replica set created & first attempt to set primary"

echo "start sleep"
sleep 10
echo "end sleep"

#  setting mongodb2 as PRIMARY
mongo --host mongodb2 <<EOF
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[1].priority = 1
rs.reconfig(cfg)
EOF

echo "second attempt to set primary"
