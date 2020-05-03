sudo docker swarm leave --force
sudo docker swarm init
sudo docker service create --replicas 1 --name metrics --mount type=bind,source=/home/student/Downloads/IDP/idp-project/prometheus/prometheus.yml,destination=/etc/prometheus/prometheus.yml --publish 9090:9090/tcp prom/prometheus

sudo docker service rm metrics
sudo docker service ls
