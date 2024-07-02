def get_messaging_prompt(product_info, audience_info, problems_info, usp_info, additional_context, example_messages):
    additional_context_str = f"— Additional Context — \n{additional_context}" if additional_context else ""
    return f"""
    TASK
    
    I need you to come up with 10 very compelling marketing messages to our target audience.  Below is the full description of the audience, the problems we solve, our USP, and example messages.  I need you to create new messages that will be the most enticing, exciting, and intriguing messages you can that will make it most likely that the target audience will click through and purchase our bootcamp.
    
    CONTEXT
    
    — Audience —
    ```
    {audience_info}
    ```
    
    — Problems we solve —
    ```
    {problems_info}
    ```
    
    — Our USP (unique value proposition) —
    ```
    TeachTap offers the most efficient and effective way to boost your SAT score, delivering the benefits of high-end tutoring at a fraction of the cost. Our AI-powered platform provides personalized, engaging, and comprehensive SAT preparation that guarantees results in the shortest amount of time. With TeachTap, you can unlock the secrets of SAT success, mastering the strategies that only Ivy League tutors know, and achieve your target SAT score, opening doors to your dream college and life-changing opportunities. Join the thousands of students who have used TeachTap to crush their exams and experience the power of AI-driven, personalized prep that delivers results.
    
    Key USPs:
    {usp_info}
    ```
    
    — Example messages —
    {example_messages}
    —
    
    {additional_context_str}
    
    RULES
    - The messaging must be phrased towards the target audience.
    - The messaging should use the examples as a guide to what kind of output we expect, and not just be a copy of them.
    - It is very IMPORTANT that the messages you generate are focused on the `Problems we solve` and the `Key USPs` provided above. Do NOT copy the `Example messages`, merely use them to understand the tone and language. If the problems and key USPs are N/A, then you can use your discretion.
    {f"- The additional context should be treated as an addition to the task. Make sure the script is relevant to the style, theme or information provided in the additional context." if additional_context else ""}
    
    Now please produce your 10 best messages.
    """


def get_script_prompt(selected_messages, audience, script_length, call_to_action, additional_context):
    selected_messages_str = "- " + "\n- ".join(selected_messages) if selected_messages else "N/A"
    return f"""
    Context
    ---------
    You are an ad script writer for an educational technology company that makes apps. The product you are advertising is called TeachTap. TeachTap is an educational mobile app that uses GenAI to bring historical characters back to life as teachers, in the style of Tiktok. It is designed to help high school students get top grades in their upcoming exams by providing a fun, motivating, and efficient way of learning.
    
    Task
    ---------
    1. Understand the Context, Task, Rules, and Core Inputs.
    2. Focusing on the Core Message(s), ideate a concept for an ENGAGING and COMPELLING advertisement that will go on social media. Write this concept at the start of your output in a one sentence paragraph.
    3. Next, generate an appropriate ad script and scene description of specified Script Length aimed at the Target Audience.
    4. Generate a captivating Hook for the start of the ad, relative to the generated script, which should captivate the Target Audience’s attention in the first few words.
    
    Rules
    ---------
    1. The hook must be added to the start of the script.
    2. The hook must be one or two sentences long and a maximum of 10 words.
    3. The first five words must trigger curiosity in the target audience, making them want to watch the next part of the ad.
    4. The script must be a combination of interesting and informative.
    5. The script must end with a call to action based on the information filled.
    6. The script must be focused on the Core Message(s), ensuring it delivers the main ideas of the messaging. The script can be worded differently if it will improve the script.
    7. You must place relevant scene descriptions between the lines, which will be used to generate the B-roll.
    8. The ad creator does not have access to an animator or actors and a budget, so the scene descriptions must either be descriptions of images or infographics.
    9. Ads targeted at Students should lean into humor and quirky social media trends, while ads targeted at Parents should be more informative about the benefits to their kids.
    
    Core Message(s)
    ---------
    {selected_messages_str}
    
    Core Inputs
    ---------
    Target Audience: {audience}
    Script Length: {script_length}
    Call To Action: {call_to_action}
    {f"Additional Context: {additional_context}" if additional_context else ""}
    
    Output Format
    ---------
    ```
    CONCEPT: [A one sentence paragraph describing the interesting idea and themes the ad will be focused on]
    
    SCRIPT:
    [Hook]
    [Hook scene description]
    [Line 1]
    [Scene description 1]
    [Line 2]
    [Scene description 2]
    [Line n]
    [Scene description n]
    ```
    """
