def get_messaging_prompt(audience_info, problems_info, usp_info, example_messages):
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


def get_hooks_prompt(product_name, target_audience, narrator, core_message, additional_context):
    product_details = "TeachTap is an educational mobile app that uses GenAI to bring historical characters back to " \
                      "life as the teachers, in the style of Tiktok. It is designed to help high school students get " \
                      "top grades in their upcoming exams by providing a fun, motivating and efficient way of learning."
    example_core_message = "High SAT scores open doors to elite universities: Without them, gaining admission to your " \
                           "dream school may be out of reach. A high SAT score gives you the competitive edge needed " \
                           "to succeed in today's highly selective admissions process."
    example_hook = "Top universities care about SAT scores. But is your child ready?"

    return f"""
    Context
    ---------
    You are an ad script writer for an educational technology company that makes apps. The product you are advertising is called {product_name}. Description of the app: {product_details}

    Task
    ---------
    1. Understand the Context, Task, Rules, Examples, and Core Inputs.
    2. Generate five captivating Hooks for the start of the ad, relative to the Core Inputs, which should captivate the Target Audience’s attention in the first few words.

    Rules
    ---------
    1. The hook must be one or two sentences long and a maximum of 10 words
    2. The first five words must trigger curiosity in the target audience, making them want to watch the next part of the ad.
    3. The hook must be funny, interesting, or hyperbolic.
    4. The hook must be relevant to the core message.

    Core Inputs
    ---------
    Target Audience: {target_audience}
    AI Figure/Narrator: {narrator}
    Core Message: {core_message}
    Additional Context from Creator: {additional_context}

    Example(s)
    ---------
    ```
    Core Message: {example_core_message}
    Hook: {example_hook}
    ```
    """
