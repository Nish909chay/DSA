"""
📌 TASK FOR GITHUB COPILOT:

You are a subject matter expert in Operating Systems and a professional question paper setter.

You are given a large, cleaned transcript of OS lectures in the file `os_trans_cleaned.txt`.

Your task is to:
1. Read and analyze the full transcript.
2. Identify major OS concepts mentioned, such as:
   - Process Scheduling
   - Threads and Processes
   - Deadlock
   - Memory Management
   - Paging and Segmentation
   - File Systems
   - Synchronization and Semaphores
   - CPU Scheduling Algorithms (FCFS, SJF, RR, Priority)
   - Disk Scheduling
3. For each concept found, generate 3–5 **aptitude-style MCQs**.
   - Each question must have 4 options: (a), (b), (c), (d)
   - Provide the **correct answer**
   - Give a **brief one-line explanation**

4. Save all the questions in a text file called `os_mcq_output.txt`, grouped by topic like:

---------------------
Topic: Deadlock

Q1. Which of the following is NOT a necessary condition for a deadlock?
a) Mutual exclusion
b) Hold and wait
c) Preemption
d) Circular wait  
Answer: c) Preemption  
Explanation: Preemption prevents deadlocks by forcibly removing resources.
---------------------

🧠 Note:
- If no direct questions exist in transcript, infer and create new ones based on concepts.
- Make questions suitable for campus placement, GATE, or tech interview MCQs.
"""

# === START CODE ===

def generate_os_mcqs():
    with open("os_trans_cleaned.txt", "r", encoding="utf-8") as f:
        transcript = f.read()

    # Step 1: Analyze transcript to extract concepts (let Copilot infer)
    # Step 2: Generate MCQs per concept
    # Step 3: Save all to output file
    with open("os_mcq_output.txt", "w", encoding="utf-8") as out:
        # Example of how Copilot should write
        out.write("Topic: Process Scheduling\n\n")
        out.write("Q1. In Round Robin scheduling, each process gets:\n")
        out.write("a) An unlimited time slice\nb) A random priority\nc) A fixed time quantum\nd) Executed last\n")
        out.write("Answer: c) A fixed time quantum\n")
        out.write("Explanation: Round Robin assigns equal fixed time slices for fairness.\n\n")

        # Copilot should continue writing similar blocks for all other topics

generate_os_mcqs()
