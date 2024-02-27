# **Log File Analysis for UMHPC**

### **Overview:**

*In this project, we aim to analyze the log files extracted from the SLURM scheduler of the Data Intensive Computing Centre (DICC) at UM, focusing on the High Performance Computing (HPC) system known as UMHPC. The objective is to extract valuable insights and metrics from these logs to enhance the efficiency, performance, and stability of the UMHPC system.*

### **Background:**

*UMHPC plays a crucial role in supporting modern scientific collaborations by providing HPC services to the campus community. As the complexity of computational experiments increases, it becomes essential to monitor and analyze system logs to ensure optimal performance and reliability.*

*There are different types of nodes for different types of jobs. Our HPC cluster consists of the following:*

- ***VPN Gateway**, where users establish a private connection to interact with Login Node and internal HPC resources*

- ***Login Node**, where users log in via SSH or Open OnDemand portal*

- ***CPU compute nodes** (where majority of computations will be executed)*

- ***GPU compute nodes** (for those jobs that can benefit from the massive parallel execution on Graphical Processing Unit)*

- ***Storage nodes** (where the data is been stored)*





### **Figure 1: Architecture of UMHPC**

![Architecture of UMHPC](./architecture%20of%20UMHPC.png)

### **Project Goals:**

1.  **Log File Analysis:** *We will study the six-month log file extracted from the SLURM controller to understand the patterns, trends, and anomalies in job submissions and executions.*

2.  **Program Development:** *A Python program will be developed to parse and analyze the log files, extracting useful information such as job creation/termination timestamps, job partitions, errors, execution times, and more.*

3. **Visualization:** *The extracted data will be presented in both tabular and graphical formats to provide clear insights into the performance and usage patterns of the UMHPC system.*

4.  **Metrics Extraction:** *Various metrics will be calculated, including:* 

    -  *Number of jobs created/ended within a given time range.*

    -  *Number of jobs by partitions, i.e. EPYC, Opteron and GPU.*

    -  *Number of jobs causing error and the corresponding user. The error is indicated as “\[2022-06-01T15:12:23.290\] error: This association…”*

    -  *Average execution time of the jobs submitted to UMHPC.*

    -  *Other statistical data that you can extract.*

### **Expected Outcome:**

1.  By analyzing the log files and deriving meaningful metrics, we aim to:

    -  *Enhance system monitoring and management capabilities.*
    -  *Identify potential performance bottlenecks and areas for optimization.*
    -  *Improve user experience by addressing common issues and errors promptly.*
    -  *Provide valuable insights for future resource allocation and system upgrades.*


