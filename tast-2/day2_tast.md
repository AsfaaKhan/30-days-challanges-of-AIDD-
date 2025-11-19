# **📁Part A — Theory (Short Questions)**

## 1. Nine Pillars Understanding

**Qno: 1 Why is using AI Development Agents (like Gemini CLI) for repetitive setup tasks better for your growth as a system architect?**
*Ans :  By using AI development agents for repetitive tasks helps you grow as a system architect on what truely matters in architecture and design.*
*Following are the important benfits for using AI development agents:*
**1. You stop wasting time on setups and practicing architecure**
**2. You learn to communicate with AI by clear specifications like an architect.**
**3. Instead of focusing on typing code , we learn how to  structred** 
**4. By using your guide correct and specific requirments to AI agents we trains the AI.**

**Qno:2 Explain how the Nine Pillars of AIDD help a developer grow into an M-Shaped Developer?**
*Ans : The Nine Pillars  consist of the characteristics of AI Driven Development. These pillars  help a developer to become strong in multiple areas at the same time.*

These are the Nine Pillars of AIDD:
**1. Pillar 1: AI CLI & Coding Agents**
    *These agents runs in the terminal and act like a your coding teammate.*

**2. Pillar 2: Markdown as Programming Language**
    *You just need to write code in markdown with clear instructions and specifictions because AI read this and convert hem into code.*

**3. Pillar 3: MCP Standard (Model Context Protocol)**
    *AI can access database , run commands, use tools, read files or update code safely.*

**4. Pillar 4: AI-First IDEs**
    *Instead of writing eveyting manually , AI can genrate files , write code, fix bugs , run tests, understand your entire project.*

**5. Pillar 5: Linux Universal Dev Environment**
    *Biggest heachache in the world of software developmet is AI Agents only works on their machine  but does not work on another machine or computer. By Linux universal Dev Environment that ensure thats human and AI agents work consistently across machines.*
    [Linus Universal Dev Environment](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/tast-2/screenshots/linux_universal_dev_environment.png)

**6. Pillar 6: Test-Driven Development (TDD)**
    *We first need to write tests then AI generates code that passess the tests. These tests makes development safer, cleaner, predictable.*

**7. Pillar 7: Specification-Driven Development with SpecKit Plus**
    *We need to write clear specifications by using SpecKit plus. By reading this specs AI build code, generates test, creates docs.*

**8. Pillar 8: Composable Vertical Skills**
    *Developers build skills with multiple areas like :Frontend,Backend,Database,AI Agents,DevOps,Cloud*

**9. Pillar 9: Universal Cloud Deployment**     
    *AI automates full deplyments. AI handles the heavy DevOps work.*



# 2. Vibe Coding vs Specification-Driven Development

**Qno: 1 Why does Vibe Coding usually create problems after one week?**
*Ans : Vibe Coding create problems because it is based on mood , not on a strcuture. Developers writes code quickly with the help of AI without any planning, without any specifictions, but within a days  the projects looks messy, confusing  and difficult to understand and headache to debug any error or issue.*

**Qno: 2 How would Specification-Driven Development prevent those problems?**
*Ans: Specification-Driven Development fixes those problems  by using clear written specifictions, requirements, features, rules before starting coding. Developers excatly know what to build.* 


# 3. Architecture Thinking

**Qno : 1 How does architecture-first thinking change the role of a developer in AIDD?**
*Ans : Architecture-first thinking shifts the developer’s role from writing raw code to designing the system, creating clear specifications, and overseeing AI-generated implementations. Developers focus on architecture, decision-making, and quality rather than manual coding.*

**Qno: 2 Explain why developers must think in layers and systems instead of raw code.**
*Ans: Thinking in layers and systems lets developers manage complexity, define clear specifications for AI, ensure maintainability, and consider system-level requirements like scalability and security. It enables efficient collaboration with AI and produces modular, reusable, and reliable software.*


#


# 📁 Part B — Practical Task (Screenshot Required)
Task:
Using any AI CLI tool, generate a 1-paragraph specification for an email validation function.
Requirements:
Must contain “@”
Must contain a valid domain (e.g., .com, .org)
Should return clear error messages

#### CLI prompt:
*$Generate a 1-paragraph specifiction for an email validation function. Requirements : Must Contain @ , Must Conatin a valid domain (e.g,.com,.org) , Should return clear error messages$*

#### Output:
*The email validation function validate_email(email_address: str) -> Tuple[bool, Optional[str]] will accept a single string argument representing an email address and return a tuple containing a boolean indicating validity and an optional string for error messages. The function must ensure the email address contains exactly one "@" symbol separating the local part from the domain. Furthermore, it must verify that the domain contains a valid top-level domain (TLD) consisting of at least two alphabetical characters, preceded by a dot (e.g.,".com", ".org"). If the email address fails any validation rule, the function should return False along with a descriptive error message indicating the specific reason for failure (e.g., "Missing '@' symbol", "Invalid domain format", "Missing top-level domain").*

[screenshots](https://github.com/AsfaaKhan/30-days-challanges-of-AIDD-/blob/main/tast-2/screenshots)


#

# 📁Part C — Multiple Choice Questions
1. What is the main purpose of Spec-Driven Development? (Option 🅱️: ✅)
A. Make coding faster
B. Clear requirements before coding begins ✅
C. Remove developers
D. Avoid documentation

2. What is the biggest mindset shift in AI-Driven Development? (Option 🅱️: ✅)
A. Writing more code manually
B. Thinking in systems and clear instructions ✅
C. Memorizing more syntax
D. Working without any tools

3. Biggest failure of Vibe Coding? (Option 🅱️: ✅)
A. AI stops responding
B. Architecture becomes hard to extend ✅
C. Code runs slow
D. Fewer comments written

4. Main advantage of using AI CLI agents (like Gemini CLI)? (Option 🅱️: ✅)
A. They replace the developer completely
B. Handle repetitive tasks so dev focuses on design & problem-solving ✅
C. Make coding faster but less reliable
D. Make coding optional

5. What defines an M-Shaped Developer? (Option © : ✅)
A. Knows little about everything
B. Deep in only one field
C. Deep skills in multiple related domains ✅
D. Works without AI tools
