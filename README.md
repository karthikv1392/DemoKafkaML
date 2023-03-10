# DemoKafkaML
Demo of how Kafka can be used for streaming data and making predictions using a simple ML model

## Commands to Get Started with Kafka
  1. Download Apache Kafka - https://kafka.apache.org
  2. Go inside the kafka root directory (using cd command)
  3. Run bin/zookeeper-server-start.sh config/zookeeper.properties
  4. Start the Kafka broker bin/kafka-server-start.sh config/server.properties
  5. Create topic bin/kafka-topics.sh --create --topic sample1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  6. Write to topics: bin/kafka-console-producer.sh --topic sample1 --broker-list localhost:9092
  7. Consume from topics bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092


## Disclaimer
The above commands are written for Kafka 2.11. If you are using the latest version of Kafka, please refer to the following page: https://kafka.apache.org/quickstart
