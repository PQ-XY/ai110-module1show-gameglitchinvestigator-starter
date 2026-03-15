# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. When I change the difficulty setting on the sidebar, it updates the main page difficulty level, but it didn't change the range on the main page.
  2. Shoule the hard level be range 1 - 100 and normal level be 1 - 50? Currently, the hard is from 1 - 50 and normal being 1 - 100.
  3. I run the game twice and it just keeps telling me to go lower even I put 0, which is not even in the range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  I ask AI that "Ok, you are a software engineer teamed with me to debug the code. Now I noticed that there is a logic bug that level hard should be range 1- 100 and level normal should be range 1 -50." AI was able to find the bug and correct it easily.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  I asked AI to update the "new game" button to refresh the page everytime I click it. AI updated my code and then the program has runtime error. So I have to revert back. 
  

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I re-run the program and check if it is working now.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  After the updates, I run the pytest and it passed all the cases.
- Did AI help you design or understand any tests? How?
  Yes, I asked AI to add some edge cases for the tests. It did add some cases like string. But I have to let it know what specific edge cases I want, like negative numbers.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit apps don’t “step through” code like a traditional script; instead, the whole script runs top‑to‑bottom every time something changes (e.g., you click a button, move a slider, or call st.rerun()). Each interaction triggers a fresh run, which is how the UI updates.
  Because the script keeps rerunning, you need a place to remember values between runs (like the secret number, score, or how many guesses you’ve made). st.session_state is basically a dictionary that lives across reruns for each user, so you can store and update things there and they’ll still be available the next time the script reruns for that same browser session.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I would use Git more. Previously, I only use Git add and commint when I had a page down or one feather fully implemented. I think now I should break it into parts and it should be easier to track back.
- What is one thing you would do differently next time you work with AI on a coding task?
  I will try to be specific and provide more detail as I can to help AI get to the point I need. And I should give AI more restriction on what file I want to update.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I think AI can be useful and make our work more efficent. But it also requires that the software engineer knows what he is doing so he can guide AI more efficently.
