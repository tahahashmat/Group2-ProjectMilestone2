from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9093", 
    client_id='test'
)

topic_list = [NewTopic(name="test", num_partitions=1, replication_factor=2)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)