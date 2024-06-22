def get_messaging_prompt(product_info, audience_info, problems_info, usp_info, example_messages):
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
    
    RULES
    - The messaging must be phrased towards the target audience.
    
    Now please produce your 10 best messages.
    """
