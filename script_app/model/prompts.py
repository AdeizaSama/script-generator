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
    - The messaging should be focused primarily on the problems we solve and the key USPs mentioned above. If they are N/A, then use your discretion.
    {f"- The additional context should be treated as an addition to the task. Make sure the script is relevant to the style, theme or information provided in the additional context." if additional_context else ""}
    
    Now please produce your 10 best messages.
    """
