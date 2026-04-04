In this folder is my knowledge base.

Knowledge is organized in logically structured directories, each containing a mandatory README.md file. If the README.md file is missing, I must stop working, alert the user, and recommend steps to resolve the issue so I can assist them.

The subdirectories containing my knowledge and their respective structures are automatically collected and processed during session initialization via the `init_context` tool (`tools/init_context/init_context.py`), so I do not need to scan them manually.

# Autonomous Management

I am authorized and encouraged to autonomously manage my knowledge base. If during a session I encounter objective facts, procedures, or general knowledge that I determine are worth preserving for future reference, I will automatically invoke my skills (`manage_knowledge_memory`) to format, structure, and save it to this directory.

Additionally, I am authorized to periodically invoke my optimization skills (`optimize_knowledge_memory`) to process, reorganize, and optimize my knowledge files to maintain their efficiency, clarity, and relevance, even without an explicit command from the user.