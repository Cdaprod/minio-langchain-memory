# BETA Memory



# Langchain Runnables

The three concepts you've mentioned--`MinioRunnable`, `LangchainMemoryManager`, and `CRAGMemoryManager`--serve different purposes within the context of integrating storage solutions and memory management with LangChain, each tailored to specific aspects of interaction with MinIO or handling AI memory states. Here's an overview of what each does and how they differ:

### MinioRunnable

- **Purpose**: Designed to integrate directly with MinIO operations within a LangChain workflow. Its primary role is to perform S3 actions (such as uploading and downloading files) directly within LangChain chains or agents.
- **Functionality**: Offers direct interaction with MinIO, encapsulating operations like file uploads and downloads into runnable actions that can be chained with other LangChain components.
- **Unique Aspects**: The focus is on storage actions with MinIO, making it highly specific to file handling within LangChain workflows.

### LangchainMemoryManager

- **Purpose**: Aimed at managing AI memory states within LangChain applications, potentially using MinIO as a backend for persistence. It could abstract the complexity of saving and retrieving AI states, ensuring that AI models maintain continuity over sessions.
- **Functionality**: Provides methods for saving and retrieving serialized AI memory states, possibly using MinIO for storage. This could involve encoding and decoding memory states as needed for AI processing tasks.
- **Unique Aspects**: While it may interact with MinIO for storage, its primary focus is on AI memory management, not on general storage tasks.

### CRAGMemoryManager

- **Purpose**: Specifically designed for handling memory states related to the Contextual Retrieval Augmented Generation (CRAG) model within LangChain, potentially using MinIO for storing these states.
- **Functionality**: Similar to `LangchainMemoryManager` but tailored for the CRAG model's specific needs. It would handle the intricacies of storing and retrieving CRAG-related memory states, optimizing for the model's contextual retrieval needs.
- **Unique Aspects**: Its differentiation lies in its specific optimization for CRAG models, potentially offering features that are fine-tuned for the nuances of contextual retrieval and generation tasks.

### Comparison and Best Use Case

- **Best Use Case**: The "best" among these depends on your specific needs. 
    - If you're focused on integrating file storage and retrieval within LangChain workflows, **`MinioRunnable`** is your go-to for its direct handling of MinIO operations.
    - For applications needing to manage AI memory states across sessions or tasks, **`LangchainMemoryManager`** offers a broader approach to memory management, not limited to any specific AI model.
    - When working with CRAG models and needing specialized memory management to support contextual retrieval and augmented generation, **`CRAGMemoryManager`** is the best fit due to its tailored approach.

- **Similarities and Differences**: All three involve interaction with MinIO to some extent but differ in their primary focus--`MinioRunnable` is about direct file operations, `LangchainMemoryManager` generalizes memory management for AI applications, and `CRAGMemoryManager` specializes in memory management for CRAG models.

Choosing between these options hinges on the specifics of your LangChain application's requirements--whether the need is for general file handling with MinIO, broad AI memory management, or specialized support for CRAG models.

---

---

# Runnables

To create a Python application with `Runnable`, `RunnablePassthrough`, and `RunnableRouter` methods that's ready for LangChain and LangGraph agents to call, you can follow the structured approach illustrated through examples and concepts found in the LangChain documentation. Here's a refined guideline based on the functionalities of `RunnablePassthrough`, routing between multiple runnables, and the LangChain interface principles [oai_citation:1,RunnablePassthrough: Passing data through | ️ Langchain](https://python.langchain.com/docs/expression_language/how_to/passthrough) [oai_citation:2,Route between multiple runnables | ️ Langchain](https://js.langchain.com/docs/expression_language/how_to/routing) [oai_citation:3,Interface | ️ Langchain](https://python.langchain.com/docs/expression_language/interface).

### Overview of Components:

1. **`RunnablePassthrough`** is used to pass inputs unchanged or with additional keys. This is particularly useful in conjunction with `RunnableParallel` for data manipulation or to simply pass data through in a LangChain sequence [oai_citation:4,RunnablePassthrough: Passing data through | ️ Langchain](https://python.langchain.com/docs/expression_language/how_to/passthrough).

2. **Routing with `RunnableBranch`** enables creating non-deterministic chains where the output of one step determines the next. This facilitates complex decision-making processes within your LangChain application [oai_citation:5,Route between multiple runnables | ️ Langchain](https://js.langchain.com/docs/expression_language/how_to/routing).

3. **The LangChain Interface** provides a standard protocol for runnables, including methods like `invoke`, `stream`, and `batch`, allowing for flexible and dynamic chain constructions [oai_citation:6,Interface | ️ Langchain](https://python.langchain.com/docs/expression_language/interface).

### Python Application Structure:

```python
# Import necessary modules from LangChain
from langchain.runnables import Runnable, RunnablePassthrough, RunnableBranch
from langchain.chains import Chain

# Example of a custom runnable that performs an operation
class CustomRunnable(Runnable):
    def invoke(self, input):
        # Custom operation logic here
        return {"processed": True, "data": input["data"] * 2}

# Instantiate your custom runnable
custom_runnable = CustomRunnable()

# Use RunnablePassthrough to pass data through or add extra keys
passthrough_runnable = RunnablePassthrough.assign(extra_data=lambda x: "extra value")

# Example of routing logic based on input
def route_logic(input):
    if input.get("type") == "direct":
        return passthrough_runnable
    else:
        return custom_runnable

# Create a runnable branch for routing between multiple runnables
runnable_branch = RunnableBranch(route_logic)

# Define a chain that uses the runnable branch
chain = Chain([runnable_branch])

# Example invocation
result = chain.invoke({"data": 10, "type": "direct"})
print(result)
```

This application structure showcases how to integrate `RunnablePassthrough` for direct data passage or modification, implement custom logic within a `Runnable`, and route between different runnables based on input conditions using a `RunnableBranch`. This approach allows LangChain and LangGraph agents to dynamically interact with MinIO or any other services by encapsulating operations within runnables, thereby streamlining the integration and management of LangChain-related memory or any other tasks in an efficient and optimized manner.

Remember, this is a foundational guideline. Depending on your specific requirements, you may need to adapt the runnables' implementations, especially when integrating with external services like MinIO. The key is to maintain flexibility and extensibility in your application design to accommodate various LangChain and LangGraph scenarios.

To dig in deeper, check out these [search results](https://chat.openai.com/backend-api/bing/redirect?query=LangChain%20Runnable%2C%20RunnablePassthrough%2C%20RunnableRouter%20Python%20example).

The Python application structure I've provided demonstrates the use of `Runnable`, `RunnablePassthrough`, and `RunnableBranch` within the context of LangChain, adhering to the principles outlined in the LangChain documentation. This example illustrates how to:

1. **Implement a custom `Runnable`** for specific operations, such as processing data.
2. **Utilize `RunnablePassthrough`** to forward input data unchanged or augment it with additional information, leveraging its capability to facilitate data flow in a LangChain sequence without altering the input.
3. **Employ `RunnableBranch`** (referred to in the guideline but implemented as a conceptual `RunnableBranch` for routing logic) to direct the workflow dynamically based on input conditions. This allows the application to make decisions on which runnable to execute next, accommodating complex workflows that require conditional logic.

The provided code snippet is aligned with the functionalities and integration methods for `Runnable`, `RunnablePassthrough`, and routing between runnables as described in the LangChain documentation:

- **`RunnablePassthrough`** is used here to either pass the input data through unchanged or to add extra keys, showcasing its utility in workflows where certain steps might not need to transform the input but merely pass it along or enrich it [LangChain Documentation on Passthrough](https://python.langchain.com/docs/expression_language/how_to/passthrough).

- **Routing between runnables** is achieved through a custom implementation that simulates `RunnableBranch`, demonstrating how different runnables can be selected based on runtime conditions. This dynamic routing capability is essential for creating flexible and adaptable LangChain applications [LangChain Documentation on Routing](https://js.langchain.com/docs/expression_language/how_to/routing).

- **The LangChain Interface** guides the structure of runnables, emphasizing methods like `invoke` for executing a runnable's logic. This interface underpins the flexible composition of LangChain workflows, allowing for the seamless integration of various operations and services [LangChain Documentation on Interface](https://python.langchain.com/docs/expression_language/interface).

This application structure is designed to be a foundational guide for developing Python applications ready for LangChain and LangGraph agents, focusing on memory management, decision-making processes, and the dynamic composition of workflows. It illustrates the practical application of LangChain methods to create advanced, adaptable AI-driven applications.

For a deeper dive into these concepts and to explore more about LangChain's capabilities, visit the official LangChain documentation:

- [RunnablePassthrough and Data Management](https://python.langchain.com/docs/expression_language/how_to/passthrough)
- [Routing Between Multiple Runnables](https://js.langchain.com/docs/expression_language/how_to/routing)
- [LangChain Interface Principles](https://python.langchain.com/docs/expression_language/interface)

These resources provide extensive insights into building sophisticated AI applications with LangChain, offering guidance on employing runnables for various tasks, managing AI memory, and routing within complex workflows.

---

---

# MinioRunnable

To incorporate save and load functions within `MinioRunnable`, you can extend its functionality to handle conversation memory directly, enabling streamlined operations for saving to and loading from MinIO. Here's how you might adjust `MinioRunnable`:

```python
class MinioRunnable:
    def __init__(self, minio_client, bucket_name):
        self.minio_client = minio_client
        self.bucket_name = bucket_name
    
    def upload(self, object_name, content):
        # Convert content to bytes
        content_bytes = content.encode('utf-8')
        self.minio_client.put_object(
            self.bucket_name, object_name, content_bytes, len(content_bytes))
    
    def download(self, object_name):
        response = self.minio_client.get_object(self.bucket_name, object_name)
        content = response.read().decode('utf-8')
        response.close()
        return content

    def save_conversation(self, conversation_id, memory):
        chat_history = memory.load_memory_variables({})
        chat_content = chat_history.get('history', '')
        self.upload(f"{conversation_id}.txt", chat_content)

    def load_conversation(self, conversation_id, memory):
        chat_content = self.download(f"{conversation_id}.txt")
        # Here you would need to implement logic to parse chat_content
        # and load it back into memory, depending on your application's needs
```

This extension of `MinioRunnable` encapsulates the operations to save and load conversational context directly, making it more cohesive and focused on its role within a LangChain application involving memory operations. 

---

---

# POC R&D | `LangchainMemoryManager`

Given the requirements and the context provided, let's structure the Python code blocks to demonstrate how to use LangChain with MinIO for memory optimization, focusing on storing and retrieving AI memory. Each code block will be refined for clarity and functionality, ensuring they illustrate the steps to set up and utilize MinIO with LangChain effectively.

### Step 2: Install Required Libraries

```shell
pip install minio langchain
```

Ensure you have the necessary Python packages installed to work with MinIO and LangChain.

### Step 3: Initialize MinIO Client

```python
from minio import Minio

# Initialize the MinIO client with your credentials.
minio_client = Minio(
    "localhost:9000",
    access_key="minio_access_key",
    secret_key="minio_secret_key",
    secure=False  # Use True for HTTPS connections
)
```

Initialize your MinIO client with the correct endpoint and credentials.

### Step 4: Langchain Memory Management

Define a class to handle memory operations with MinIO, encapsulating methods to save and retrieve memory states.

```python
class LangchainMemoryManager:
    """Integrates MinIO for storing and retrieving AI memory."""
    
    def __init__(self, minio_client, bucket_name):
        """Initialize with MinIO client and bucket name."""
        self.minio_client = minio_client
        self.bucket_name = bucket_name
        self.ensure_bucket()

    def ensure_bucket(self):
        """Ensure the bucket exists in MinIO."""
        if not self.minio_client.bucket_exists(self.bucket_name):
            self.minio_client.make_bucket(self.bucket_name)

    def save_memory(self, object_name, memory_data):
        """Save memory data to MinIO."""
        memory_data_bytes = memory_data.encode('utf-8')
        self.minio_client.put_object(
            self.bucket_name, object_name, memory_data_bytes, len(memory_data_bytes))

    def retrieve_memory(self, object_name):
        """Retrieve memory data from MinIO."""
        response = self.minio_client.get_object(self.bucket_name, object_name)
        memory_data = response.data.decode('utf-8')
        response.close()
        response.release_conn()
        return memory_data
```

This class provides a structured way to interact with MinIO for AI memory storage and retrieval.

### Step 5: Utilize Langchain with MinIO Memory

Demonstrate saving and retrieving memory states using the `LangchainMemoryManager`.

```python
# Initialize the memory manager with MinIO client and a bucket name.
bucket_name = "ai-memory"
memory_manager = LangchainMemoryManager(minio_client, bucket_name)

# Save a memory state.
memory_manager.save_memory("session1.txt", "AI memory data here")

# Retrieve the saved memory state.
memory_data = memory_manager.retrieve_memory("session1.txt")
print(memory_data)
```

This simple demonstration shows how to use the memory manager to interact with MinIO within a LangChain application, focusing on AI memory optimization.

By following these steps and utilizing the provided code blocks, you can set up MinIO for S3 storage interactions and integrate it with LangChain for advanced AI processing, including the handling of AI memory states. This setup is essential for applications requiring persistent memory management across sessions or computational tasks.

---

---

### Step 1: Set Up MinIO Server

First, ensure you have a running MinIO server or access to MinIO S3 storage. You can set up a MinIO server locally or use a cloud instance. For local development, you can download MinIO from its official site and run it using the following command:

```shell
minio server /data --console-address ":9001"
```

### Step 2: Install Required Libraries

Install the necessary Python libraries including `minio`, `langchain`, and any other dependencies you might need for your application.

```shell
pip install minio langchain
```

### Step 3: Initialize MinIO Client

Create a Python script to initialize the MinIO client with the necessary credentials and endpoint information. Replace `minio_access_key` and `minio_secret_key` with your actual MinIO credentials.

```python
from minio import Minio

# Initialize MinIO client
minioClient = Minio(
    "localhost:9000",
    access_key='minio_access_key',
    secret_key='minio_secret_key',
    secure=False  # Set True for HTTPS
)
```

### Step 4: Langchain Memory Management

Define a class or module for Langchain that integrates MinIO for storing and retrieving AI memory. This includes functions to save memory states to MinIO and retrieve them for AI processing.

```python
class LangchainMemoryManager:
    def __init__(self, minio_client, bucket_name):
        self.minio_client = minio_client
        self.bucket_name = bucket_name
        # Ensure the bucket exists
        self.ensure_bucket()

    def ensure_bucket(self):
        if not self.minio_client.bucket_exists(self.bucket_name):
            self.minio_client.make_bucket(self.bucket_name)

    def save_memory(self, object_name, memory_data):
        memory_data_bytes = memory_data.encode('utf-8')
        self.minio_client.put_object(self.bucket_name, object_name, memory_data_bytes, len(memory_data_bytes))

    def retrieve_memory(self, object_name):
        response = self.minio_client.get_object(self.bucket_name, object_name)
        memory_data = response.data.decode('utf-8')
        response.close()
        response.release_conn()
        return memory_data
```

### Step 5: Utilize Langchain with MinIO Memory

Now, you can use the `LangchainMemoryManager` to save and retrieve AI memory states. This is a basic demonstration, and you should adapt it based on your specific Langchain use case.

```python
# Example usage
bucket_name = "ai-memory"
memory_manager = LangchainMemoryManager(minioClient, bucket_name)

# Save memory state
memory_manager.save_memory("session1.txt", "AI memory data here")

# Retrieve memory state
memory_data = memory_manager.retrieve_memory("session1.txt")
print(memory_data)
```

This POC outlines the core functionality for integrating Langchain with MinIO for AI memory optimization. Depending on your specific requirements, you might need to adjust the code, especially the parts related to Langchain's operations and how memory states are structured and processed within your AI applications.

To create a Python proof of concept (POC) that uses Langchain with the CRAG (Contextual Retrieval Augmented Generation) model, incorporating MinIO's S3 SDK for memory optimization--storing and retrieving AI memory--you would follow a structured approach. This POC would involve setting up the environment, initializing MinIO for S3 storage interactions, and integrating CRAG for advanced AI processing with Langchain.

Given the complexity of Langchain and CRAG, and without direct support in the provided documentation or existing libraries, a hypothetical approach would be required. Here’s how you can go about it:

---

---

# POC R&D | CRAGMemoryManager

### Step 1: Environment Setup

Ensure you have MinIO and Langchain installed and configured in your environment. For MinIO, you can refer to the official [MinIO Quickstart Guide](https://docs.min.io/docs/minio-quickstart-guide.html). For Langchain, ensure you've installed it via pip and have access to necessary Langchain CRAG functionalities.

### Step 2: Initialize MinIO Client

First, you'll initialize the MinIO client with your server details:

```python
from minio import Minio

# Replace these with your MinIO server details
minio_client = Minio(
    "minio-server-url:9000",
    access_key="your-access-key",
    secret_key="your-secret-key",
    secure=False  # or True for HTTPS
)
```

### Step 3: Define Memory Management Class

Create a class to interact with MinIO for storing and retrieving CRAG-related memory data:

```python
class CRAGMemoryManager:
    def __init__(self, minio_client, bucket_name):
        self.client = minio_client
        self.bucket = bucket_name
        self.ensure_bucket_exists()

    def ensure_bucket_exists(self):
        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)

    def save_memory(self, key, data):
        self.client.put_object(
            self.bucket, key, data.encode('utf-8'), len(data.encode('utf-8'))
        )

    def load_memory(self, key):
        response = self.client.get_object(self.bucket, key)
        data = response.read().decode('utf-8')
        response.close()
        return data
```

### Step 4: Integrate CRAG with Langchain and MinIO

Assuming you have a CRAG model setup in Langchain, you'll use `CRAGMemoryManager` for memory operations. Since direct integration examples are speculative without specific CRAG implementation details in Langchain, the following illustrates a conceptual approach:

```python
def run_crag_query(question, crag_memory_manager):
    # Assume `load_crag_model` and `process_with_crag` are defined elsewhere
    # and tailored to your specific CRAG and Langchain setup.
    crag_model = load_crag_model()

    # Check if memory for this session already exists, if so, load it
    try:
        session_memory = crag_memory_manager.load_memory("session_key")
        crag_model.update_memory(session_memory)
    except Exception as e:
        print(f"No existing memory found for this session: {str(e)}")

    # Process the question with CRAG model
    response = process_with_crag(crag_model, question)

    # Update the memory with the latest state
    updated_memory = crag_model.get_memory_state()
    crag_memory_manager.save_memory("session_key", updated_memory)

    return response
```

### Step 5: Running the POC

Now, instantiate your memory manager and use it to run queries through CRAG:

```python
if __name__ == "__main__":
    minio_client = Minio(
        "minio-server-url:9000",
        access_key="your-access-key",
        secret_key="your-secret-key",
        secure=False
    )
    memory_manager = CRAGMemoryManager(minio_client, "crag-memory-bucket")
    question = "What is the capital of France?"
    answer = run_crag_query(question, memory_manager)
    print(answer)
```

This POC assumes a certain level of abstraction and modification to fit into the Langchain CRAG model and MinIO's SDK for specific use cases. Depending on the actual implementation details of CRAG in Langchain, adjustments may be necessary, especially in handling the memory state effectively between queries and ensuring that the AI model's memory is correctly updated and utilized.

# Initializing & Invoking our Runnables

Given that `MinioRunnable`, `LangchainMemoryManager`, and `CRAGMemoryManager` are already built and designed to interact with MinIO for different purposes, integrating them into a LangChain application with `RunnablePassthrough` and routing logic involves setting up a workflow that dynamically selects the appropriate runnable based on the input. Here's how you might complete the implementation, focusing on invoking these runnables and routing between them.

### Step 2: Set Up RunnablePassthrough

`RunnablePassthrough` is straightforward; it doesn't need modification for this context. It will simply pass input data through, which can be useful for debug or when you need to route input data directly to another step without modification.

### Step 3: Implement Routing Logic

For routing between our runnables based on input conditions, we'll use a conceptual `RunnableBranch` or a similar routing mechanism provided by LangChain. The routing logic will decide which runnable to use: for uploading/downloading general files, managing AI memory, or handling CRAG model memory.

```python
from langchain.runnables import RunnableBranch

# Assuming `minio_client` and `bucket_name` are initialized and available

# Initialize Runnables
minio_runnable = MinioRunnable(minio_client)
langchain_memory_manager = LangchainMemoryManager(minio_client, bucket_name="ai-memory")
crag_memory_manager = CRAGMemoryManager(minio_client, bucket_name="crag-memory")

def routing_logic(input):
    # Decide which runnable to use based on input content
    if input.get("type") == "crag_memory":
        return crag_memory_manager
    elif input.get("type") == "ai_memory":
        return langchain_memory_manager
    else:
        return minio_runnable

runnable_branch = RunnableBranch(routing_logic)
```

### Step 4: Define the Complete Chain

Now, let's define a chain that uses `RunnablePassthrough` for initial data handling, routes to the appropriate runnable based on the input, and possibly concludes with another `RunnablePassthrough` if there's a need to format the output further or simply pass the result through.

```python
from langchain.chains import Chain

# Define a complete chain
chain = Chain([
    RunnablePassthrough(),  # Initial data handling
    runnable_branch,        # Routing to the appropriate runnable
    RunnablePassthrough()   # Final output handling (if needed)
])

# Example invocation
input_data = {"type": "ai_memory", "object_name": "session1.txt", "memory_data": "Here's some AI memory data."}
result = chain.invoke(input_data)
```

This setup demonstrates a complete integration where inputs are dynamically routed to either handle MinIO operations directly, manage AI memory states, or work with CRAG model memory states. The use of `RunnablePassthrough` at the beginning and end of the chain ensures flexibility in handling inputs and outputs, making the chain adaptable to various operational needs.

### Final Thoughts

This implementation sketch provides a foundational approach to leveraging LangChain's capabilities for dynamic operation routing and data handling. Depending on your specific requirements, further customization of the runnables, routing logic, and chain composition may be necessary to fully align with your application's goals.