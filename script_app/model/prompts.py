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


def get_script_prompt(selected_messages, audience, script_length, call_to_action, additional_context):
    selected_messages_str = "- " + "\n- ".join(selected_messages) if selected_messages else "N/A"
    return f"""
    Context
    ---------
    You are an ad script writer for an educational technology company that makes apps. The product you are advertising is called TeachTap. TeachTap is an educational mobile app that uses GenAI to bring historical characters back to life as teachers, in the style of Tiktok. It is designed to help high school students get top grades in their upcoming exams by providing a fun, motivating, and efficient way of learning.
    
    Task
    ---------
    1. Understand the Context, Task, Rules, and Core Inputs.
    2. Focusing on the Core Message(s), generate an appropriate ad script of specified Script Length aimed at the Target Audience.
    3. Generate a captivating Hook for the start of the ad, relative to the generated script, which should captivate the Target Audience’s attention in the first few words.
    
    Rules
    ---------
    1. The hook must be added to the start of the script.
    2. The hook must be one or two sentences long and a maximum of 10 words.
    3. The first five words must trigger curiosity in the target audience, making them want to watch the next part of the ad.
    4. The script must be a combination of interesting and informative.
    5. The script must end with a call to action based on the information filled.
    
    Core Message(s)
    ---------
    {selected_messages_str}
    
    Core Inputs
    ---------
    Target Audience: {audience}
    Script Length: {script_length}
    Call To Action: {call_to_action}
    {f"Additional Context: {additional_context}" if additional_context else ""}
    
    Example(s)
    ---------
    ```
    SAT Tutors are EXPENSIVE!
    At least the effective ones are.
    That’s why TeachTap has come up with an affordable solution to get your child into the top universities.
    By hiring elite SAT tutors to train our AI, we’ve combined the best of human expertise and artificial intelligence.
    Our AI tutors are available to your child 24/7. Sign up for the SAT boot camp, today.
    ```
    ```
    Top universities care about SAT scores.
    But is your child ready?
    Only about 5% of students attain high enough SAT scores to get into the top colleges.
    But you can get ahead of the curve with TeachTap, and give your child a significant advantage in college admissions.
    TeachTap revolutionizes SAT prep with engaging and comprehensive practice tests.
    Our AI tutors and personalized score tracking highlight areas requiring improvement ensuring your child is on the path to success.
    Stay ahead of the curve with TeachTap.
    ```
    ```
    [A talk show setting where the host is standing with the audience - "Mastermind Moms: AP Test Edition" is displayed in a game show style font at the top]
    Host: Mastermind Moms: AP Test Edition, where the thankless job of being a parent meets strategy.
    Host: Let's hear 'em!
    Mom 1: I swapped my son's TikTok app with TeachTap, and after swiping for 5 hours their AP score went up by a whole point!
    Audience: *Gasps and cheers*
    Host: (sing-song) Amaaaaziiiing!
    Mom 2: I told my daughter if she was going to be on her phone all day, she had to spend at least 1 hour on TeachTap, and now... she's learning... *zoom in* on purpose!
    Audience: *Laughs and applause*
    CTA: It's the fastest path to an A in their class and a 5 on the AP test! Hook your kid up with TeachTap right now!
    ```
    """
