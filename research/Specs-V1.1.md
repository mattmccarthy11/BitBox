​						Specs V1.1

GateWay Layer: Connects to the exchanges via their respective API's 

Supervising the gateway we will have am Apache Kafka *distributed streaming platform* to !kafka-apis](/Users/mattmccarthy/Desktop/kafka-apis.png)

1. Building real-time streaming data pipelines that reliably get data between systems or applications
2. Building real-time streaming applications that transform or react to the streams of data

![kafka-apis](/Users/mattmccarthy/Desktop/kafka-apis.png)

First a few concepts:

- Kafka is run as a cluster on one or more servers.
- The Kafka cluster stores streams of *records* in categories called *topics*.
- Each record consists of a key, a value, and a timestamp.

Kafka has four core APIs:

- The [Producer API](https://kafka.apache.org/documentation.html#producerapi) allows an application to publish a stream of records to one or more Kafka topics.
- The [Consumer API](https://kafka.apache.org/documentation.html#consumerapi) allows an application to subscribe to one or more topics and process the stream of records produced to them.
- The [Streams API](https://kafka.apache.org/documentation/streams) allows an application to act as a *stream processor*, consuming an input stream from one or more topics and producing an output stream to one or more output topics, effectively transforming the input streams to output streams.
- The [Connector API](https://kafka.apache.org/documentation.html#connect) allows building and running reusable producers or consumers that connect Kafka topics to existing applications or data systems. For example, a connector to a relational database might capture every change to a table.





For begining of this app we will be using the Connector API:

​	Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. It makes it simple to quickly define *connectors* that move large collections of data into and out of Kafka. Kafka Connect can ingest entire databases or collect metrics from all your application servers into Kafka topics, making the data available for stream processing with low latency. An export job can deliver data from Kafka topics into secondary storage and query systems or into batch systems for offline analysis.

- **Distributed and standalone modes** - scale up to a large, centrally managed service supporting an entire organization or scale down to development, testing, and small production deployments
- **REST interface** - submit and manage connectors to your Kafka Connect cluster via an easy to use REST API
- **Streaming/batch integration** - leveraging Kafka's existing capabilities, Kafka Connect is an ideal solution for bridging streaming and batch data systems

# Kafka Streams

Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in a Kafka cluster. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka’s server-side cluster technology.

https://docs.confluent.io/current/streams/index.html#kafka-streams



We're trying to avoid this: 

![platform_chart_updated](/Users/mattmccarthy/Desktop/platform_chart_updated.png)





Kafka acts as a buffer:

![streaming_platform_rev](/Users/mattmccarthy/Desktop/streaming_platform_rev.png)

I found this video series on how Confluent's high level wrapper works: https://www.youtube.com/watch?time_continue=71&v=Z3JKCLG3VP4



So Kafka is going to direct data to our Postgres Time scale db: http://www.timescale.com/

“TimescaleDB is uniquely positioned in the time-series database market as the only serious player that scales up AND down, and natively supports a robust, proven SQL engine. There's a lot of value in being able to deploy the same tech on your IoT edge/gateway as you do in the cloud, and you can still leverage the full complement of SQL tools for reporting, administration, etc.”

Time scale is a time series optimised flavor of postgres that has in the box functionality for horizontal and vertical scaling of database clusters



This code is just a java depandancy that we process that is decalred in Maven or cradle build...

All the work is done within the application 



Apache Avro:



We're using a KTABLE vs KSTEAM 

