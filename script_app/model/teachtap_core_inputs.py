AUDIENCE_INFO = {
    'Students': """Students in US high schools taking the SAT exam in the next 2-3 months, who need a high score to get into their preferred college and potentially get a scholarship

a. Demographics:
i. Age: 16-18 years old
ii. Education: Currently enrolled in high school, typically grades 11-12
iii. Location: United States

b. Psychographics:
i. Ambitious and driven to succeed academically
ii. Focused on gaining admission to top colleges and universities
iii. Seeking scholarship opportunities to reduce financial burden
iv. Balancing schoolwork, extracurricular activities, and test preparation

c. Pain Points:
i. Limited time to study for the SAT while managing other responsibilities
ii. Pressure to achieve high scores to stand out in the competitive admissions process
iii. Difficulty understanding and applying complex concepts tested on the SAT
iv. Stress and anxiety related to test performance and college admissions

d. Goals:
i. Achieve a high SAT score (e.g., 1400+ out of 1600) to increase chances of admission to top colleges
ii. Secure scholarships to reduce the cost of higher education
iii. Build confidence in their test-taking abilities and academic skills
iv. Develop effective test-taking strategies and time-management techniques

e. Sub-cohorts to target with different messaging:
i. The High Achievers
- Consistently earn top grades, are involved in extracurricular activities, and aim for admission to elite colleges.
- Seek advanced study materials, time management techniques, and strategies to maintain their academic edge.
ii. The Scholarship Seekers
- Come from low to middle-income households and are highly motivated to secure scholarships.  May be first-generation college students.
- Need affordable SAT prep resources, guidance on finding scholarships, and strategies to improve their scores.
iii. The Confidence Builders
- Struggle with test anxiety and self-doubt, and seek to improve their SAT scores and build confidence.
- Need a supportive study environment, strategies to manage test anxiety, and personalized feedback.
iv. The Last-Minute Preppers
- Procrastinated on starting their SAT prep, feel overwhelmed by the amount of study material to cover in a short time, and need a focused and efficient study plan.
- Require condensed study materials, time management techniques, and intensive practice sessions.
v. The Pressured Immigrants
- First or second-generation immigrants facing intense pressure from parents to excel academically.
- Need resources to manage stress, culturally sensitive guidance on navigating the US college admissions process, and support in balancing family obligations with personal goals and well-being.
vi. The Underrepresented Minorities
- Come from underrepresented racial or ethnic groups and face additional barriers to college access, such as discrimination or lack of access
- Seek culturally relevant SAT prep materials, guidance on navigating systemic barriers, and mentorship to visualize their success.
vii. The Learning Challenged
- Have diagnosed or undiagnosed learning disabilities (e.g. ADHD, dyslexia) and struggle with traditional teaching methods and standardized testing.
- Need accommodations, adaptive learning tools, and strategies to capitalize on their strengths and build confidence in their abilities.
""",
    'Parents': """Parents of these same high school students taking SAT exams in the next 2-3 months, who want their child to get a high score on the SAT so they can get into the best college they can and potentially get a scholarship

a. Demographics:
i. Age: 45-60 years old
ii. Income: Middle to high-income households
iii. Location: United States

b. Psychographics:
i. Highly involved in their child's academic success and college admissions process
ii. Willing to invest time and money in resources that can help their child succeed
iii. Value education as a means to future success and financial stability

c. Pain Points:
i. Concern about the rising cost of college education and the need for scholarships
ii. Worry about their child's stress levels and mental well-being during the test preparation process
iii. Uncertainty about the best ways to support their child's SAT preparation
iv. Balancing the desire for their child's success with other family responsibilities and financial constraints

d. Goals:
i. Help their child achieve a high SAT score to increase chances of admission to top colleges
ii. Secure scholarships to reduce the financial burden of higher education
iii. Provide their child with the best resources and support for SAT success
iv. Foster a positive and supportive environment for their child during the test preparation process

e. Sub-cohorts to target with different messaging:
i. The Helicopter Parents
- Highly involved in their child's academic life and college admissions process, often to the point of micromanagement.
- Seek resources to help their child succeed while maintaining control and oversight.
ii. The Supportive Sidelines
- Encourage and support their child's academic pursuits but try to maintain a healthy balance of involvement.
- Look for ways to empower their child to take ownership of their SAT prep and college admissions process.
iii. The Financial Planners
- Focused on the financial aspects of college admissions and are actively seeking ways to reduce costs.
- Prioritize SAT prep resources that offer the best value for money and can help their child secure scholarships.
iv. The First-Generation Guides
- Parents who did not attend college themselves and may feel less equipped to navigate the admissions process.
- Seek clear, accessible guidance and resources to help them support their child's college aspirations.
v. The Time-Crunched Professionals
- Balancing demanding careers with supporting their child's academic success.
- Need efficient, flexible SAT prep solutions that fit into their busy schedules and require minimal hands-on involvement.
vi. The Unconventional Paths
- Open to exploring alternative college options, such as community colleges or trade schools.
- Seek resources to help their child find the best-fit educational path based on their unique interests and goals.
vii. The Special Needs Advocates
- Parents of children with learning disabilities, physical disabilities, or other special needs.
- Look for SAT prep resources that offer accommodations, assistive technology, and strategies tailored to their child's specific needs.
"""
}

# script_app/models/data.py

PROBLEMS_INFO = {
    '1': {
        'title': 'SAT Score Importance',
        'description': '''
        The SAT score is a critical factor in college admissions and scholarships.
        a. A high SAT score can significantly increase a student's chances of getting into their desired college and securing merit-based scholarships.
        b. Even small improvements in SAT scores can make a difference in admissions decisions and scholarship awards, especially for competitive colleges.
        '''
    },
    '2': {
        'title': 'Underestimation of SAT Prep',
        'description': '''
        Many students underestimate the importance of SAT prep and fail to invest enough time and resources.
        a. Students often prioritize other activities, such as schoolwork and extracurriculars, over SAT prep, not realizing the long-term impact of their scores.
        b. Lack of awareness about the importance of the SAT can lead to missed opportunities and regrets later in the college admissions process.
        '''
    },
    '3': {
        'title': 'Inadequate SAT Prep Consequences',
        'description': '''
        Inadequate SAT preparation can limit a student's college options and financial aid prospects.
        a. Students who don't invest in SAT prep may not reach their full potential and may have to settle for less competitive colleges or fewer scholarship options.
        b. The long-term consequences of limited college choices can impact a student's career prospects, earning potential, and overall life trajectory.
        '''
    },
    '4': {
        'title': 'SAT Scores Improvement Misconception',
        'description': '''
        Many students and parents believe that SAT scores are fixed and cannot be significantly improved.
        a. This misconception can lead to a lack of motivation and effort in SAT prep, creating a self-fulfilling prophecy of mediocre scores.
        b. In reality, research shows that consistent, high-quality SAT preparation can lead to significant score improvements for students at all levels.
        '''
    },
    '5': {
        'title': 'Achieving High SAT Scores',
        'description': '''
        Achieving a high SAT score (1400+, 1500+, or even 1600) is possible for any student who puts in the time and effort.
        a. Success on the SAT is not just about innate intelligence or test-taking ability; it's about dedication, strategic preparation, and consistent practice.
        b. With the right resources and support, any student can master the content and strategies needed to excel on the SAT and maximize their college admissions chances.
        '''
    },
    '6': {
        'title': 'Investing in SAT Prep',
        'description': '''
        Investing in effective SAT prep is a smart decision with long-term benefits.
        a. Higher SAT scores can open doors to more selective colleges, generous scholarships, and life-changing opportunities.
        b. The time and resources invested in SAT prep can pay off many times over in terms of college affordability, career success, and personal growth.
        '''
    }
}

# script_app/models/data.py
USP_MAIN_DESCRIPTION = """TeachTap offers the most efficient and effective way to boost your SAT score, delivering the benefits of high-end tutoring at a fraction of the cost. Our AI-powered platform provides personalized, engaging, and comprehensive SAT preparation that guarantees results in the shortest amount of time. With TeachTap, you can unlock the secrets of SAT success, mastering the strategies that only Ivy League tutors know, and achieve your target SAT score, opening doors to your dream college and life-changing opportunities. Join the thousands of students who have used TeachTap to crush their exams and experience the power of AI-driven, personalized prep that delivers results."""

USP_INFO = {
    '1': {
        'title': 'High-end tutoring strategies made accessible and affordable',
        'description': """TeachTap has distilled the expertise of top SAT tutors into an AI-powered platform, making their proven strategies and insights accessible to everyone.
* For a fraction of the cost of traditional high-end tutoring, you can access the same level of personalized guidance, comprehensive resources, and performance-boosting techniques."""
    },
    '2': {
        'title': 'Maximum score improvement in minimum time',
        'description': """TeachTap's AI-driven approach ensures you get the most out of every minute you invest in SAT prep. Our platform identifies your strengths and weaknesses, providing targeted practice and instruction that accelerates your progress.
* We're so confident in our ability to help you achieve your target score that we offer a money-back guarantee if you don't reach your goal after putting in the recommended time and effort."""
    },
    '3': {
        'title': 'Engaging and effective learning experience powered by AI',
        'description': """TeachTap brings SAT prep to life through AI-powered video explanations from virtual tutors, including historical figures who make learning fun and memorable.
* Our AI tutors are available 24/7 to answer your questions, provide instant feedback on practice tests, and guide you through challenging concepts and strategies.
* With unlimited practice tests, comprehensive progress tracking, and adaptive learning technology, TeachTap ensures you stay motivated, engaged, and on track to crush the SAT."""
    }
}

EXAMPLE_MESSAGES = [
    {
        'type': 'USP',
        'target_audience': 'Student',
        'description': "You deserve access to the same SAT strategies that give wealthy students an unfair advantage. TeachTap levels the playing field, delivering the secrets of Ivy League tutoring to your fingertips at a price that won't break the bank."
    },
    {
        'type': 'USP',
        'target_audience': 'Student',
        'description': "Tired of wasting precious time on ineffective SAT prep? TeachTap's AI-powered platform identifies your weak spots and delivers targeted practice that accelerates your progress, ensuring you achieve your goal score in record time."
    },
    {
        'type': 'USP',
        'target_audience': 'Student',
        'description': "Studying for the SAT doesn't have to be a soul-crushing chore. With TeachTap's AI tutors bringing the exam to life through engaging video explanations and 24/7 support, you'll actually enjoy the journey to your dream score."
    },
    {
        'type': 'PAIN',
        'target_audience': 'Student',
        'description': "Balancing SAT prep with schoolwork and extracurriculars can feel impossible, but neglecting your score can crush your college dreams. TeachTap fits seamlessly into your busy schedule, delivering maximum results with minimum time investment."
    },
    {
        'type': 'PAIN',
        'target_audience': 'Student',
        'description': "The pressure to stand out in college admissions can be suffocating. TeachTap helps you rise above the competition with the personalized strategies and support you need to achieve an SAT score that opens doors to your future."
    },
    {
        'type': 'PAIN',
        'target_audience': 'Student',
        'description': "Confusion and self-doubt can be your worst enemies on test day. TeachTap's comprehensive approach builds your skills and confidence, so you can conquer even the toughest SAT questions with poise and precision."
    },
    {
        'type': 'USP+PAIN',
        'target_audience': 'Student',
        'description': "You're capable of so much more than you realize - all you need are the same tools and techniques that elite students use to dominate the SAT. TeachTap unlocks your full potential at a price that makes success possible for everyone."
    },
    {
        'type': 'USP+PAIN',
        'target_audience': 'Student',
        'description': "Every minute you spend on lackluster SAT prep is a minute stolen from the activities you love. TeachTap maximizes the impact of your study time, so you can achieve your goal score and get back to what matters most."
    },
    {
        'type': 'USP+PAIN',
        'target_audience': 'Student',
        'description': "Conquering the SAT takes more than just practice - it takes self-assurance and strategic know-how. TeachTap's AI-powered platform and virtual tutors give you the unwavering support and insider knowledge you need to succeed."
    },
    {
        'type': 'USP',
        'target_audience': 'Student',
        'description': "The SAT is not an IQ test - it's a game that can be mastered with the right strategies and support. TeachTap gives you the cheat codes to beat the system and secure your dream score and future, without sacrificing your time, money, or sanity."
    },
    {
        'type': 'ROI',
        'target_audience': 'Student',
        'description': "Investing just 20 hours in SAT prep is the smartest move you can make for your college application. TeachTap's AI-powered platform delivers the most significant score improvements in the least amount of time, making it the most valuable investment in your future."
    },
    {
        'type': 'SCORE INCREASE',
        'target_audience': 'Student',
        'description': "Imagine adding 100 points to your SAT score in just 10 hours. With TeachTap's targeted AI-based prep, you can achieve the score you need to unlock doors to your dream college and scholarships."
    },
    {
        'type': 'ACCESSIBILITY',
        'target_audience': 'Student',
        'description': "High-end SAT tutoring used to be a luxury reserved for the elite. Now, TeachTap's AI technology brings those same proven strategies to you for just $200, democratizing access to top-tier prep and leveling the playing field."
    },
    {
        'type': 'CALCULATOR SKILLS',
        'target_audience': 'Student',
        'description': "Mastering just 10 critical calculator skills can boost your SAT score by 120 points. TeachTap's AI tutors guide you through these game-changing techniques, so you can conquer the Math section with confidence."
    },
    {
        'type': 'SUMMER PREP',
        'target_audience': 'Student',
        'description': "You know you need to prep for the SAT, and summer is the perfect time to knock it out. TeachTap's flexible, AI-driven platform fits seamlessly into your schedule, so you can make the most of your break and start senior year ahead of the game."
    },
    {
        'type': 'ROI+ACCESSIBILITY',
        'target_audience': 'Student',
        'description': "In a world where college admissions grow more competitive by the year, investing in SAT prep is non-negotiable. TeachTap delivers the most effective, efficient, and affordable prep available, making elite strategies accessible to all students who dare to dream big."
    },
    {
        'type': 'STRESS-FREE PREP',
        'target_audience': 'Student',
        'description': "SAT stress can be overwhelming, but it doesn't have to be. TeachTap's engaging platform and 24/7 support create a low-pressure environment that keeps you motivated and confident, so you can conquer the exam without losing your cool."
    },
    {
        'type': 'SCHOLARSHIP SHORTCUT',
        'target_audience': 'Student',
        'description': "A high SAT score is your ticket to life-changing scholarships, but you don't have to spend countless hours studying to get there. TeachTap's personalized approach and proven strategies help you secure the financial aid you need in record time."
    },
    {
        'type': 'DREAM SCHOOL DESTINY',
        'target_audience': 'Student',
        'description': "Your dream school is within reach, but you need an SAT score that reflects your true potential. TeachTap's adaptive learning platform and targeted practice help you showcase your strengths and conquer your weaknesses, so you can achieve the score that opens doors to your dream future."
    },
    {
        'type': 'FAMILY HERO',
        'target_audience': 'Student',
        'description': "You know your SAT success means the world to your family, but the pressure to perform can be intense. TeachTap's supportive platform and AI tutors empower you to become the hero of your own story, achieving the score you need to make your family proud and transform your collective future."
    },
    {
        'type': 'USP',
        'target_audience': 'Parent',
        'description': "You want your child to have every advantage in the college admissions race, but high-end tutoring can break the bank. TeachTap delivers the same proven strategies used by Ivy League tutors at a price that fits your family budget."
    },
    {
        'type': 'USP',
        'target_audience': 'Parent',
        'description': "Between school, activities, and family obligations, your child's time is stretched thin. TeachTap's AI-powered platform maximizes the impact of every study session, ensuring they achieve their goal score efficiently, without sacrificing other priorities."
    },
    {
        'type': 'USP',
        'target_audience': 'Parent',
        'description': "Watching your child struggle with SAT stress can be heartbreaking. TeachTap's engaging AI tutors and 24/7 support create a positive, interactive learning experience that keeps your student motivated and confident."
    },
    {
        'type': 'PAIN',
        'target_audience': 'Parent',
        'description': "As a parent, you're all too familiar with the challenge of fitting SAT prep into an already packed schedule. TeachTap's flexible, personalized approach seamlessly integrates with your child's unique needs and timeline, delivering results without added stress."
    },
    {
        'type': 'PAIN',
        'target_audience': 'Parent',
        'description': "The pressure to secure scholarships and stand out in college admissions can weigh heavily on your family. TeachTap equips your child with the tools and strategies they need to achieve an SAT score that opens doors to financial aid and their dream school."
    },
    {
        'type': 'PAIN',
        'target_audience': 'Parent',
        'description': "Watching your child doubt their abilities can be painful. TeachTap's comprehensive skill-building and adaptive learning technology boost your student's confidence, empowering them to conquer the SAT with self-assurance."
    },
    {
        'type': 'USP+PAIN',
        'target_audience': 'Parent',
        'description': "You'd do anything to give your child a bright future, but the cost of elite test prep can be prohibitive. TeachTap levels the playing field, providing access to top-tier tutoring strategies that can secure valuable scholarships, without the exorbitant price tag."
    },
    {
        'type': 'USP+PAIN',
        'target_audience': 'Parent',
        'description': "You want your child to succeed on the SAT, but not at the expense of their well-being. TeachTap's efficient, AI-driven approach maximizes every minute of prep time, ensuring your student achieves their goals while still having time for friends, family, and personal growth."
    },
    {
        'type': 'USP+PAIN',
        'target_audience': 'Parent',
        'description': "As a parent, you know that true success comes from within. TeachTap's engaging platform and motivating AI tutors build your child's confidence and love of learning, fostering a positive mindset that extends far beyond test day."
    },
    {
        'type': 'USP',
        'target_audience': 'Parent',
        'description': "You want to set your child up for long-term success, but navigating the SAT and college admissions process can feel overwhelming. TeachTap is your partner, providing affordable access to elite strategies, time-saving AI technology, and unwavering support that empowers your student to reach their full potential."
    },
    {
        'type': 'EFFICIENCY',
        'target_audience': 'Parent',
        'description': "Between schoolwork, extracurriculars, and college applications, your child's time is precious. TeachTap's AI technology maximizes the impact of every study session, delivering targeted practice and personalized guidance that helps them achieve their goal score in record time."
    },
    {
        'type': 'CONFIDENCE',
        'target_audience': 'Parent',
        'description': "The SAT can be a major source of stress and self-doubt for students. TeachTap's comprehensive approach builds your child's skills and confidence, empowering them to conquer the exam with poise and self-assurance."
    },
    {
        'type': 'SCHOLARSHIP SUCCESS',
        'target_audience': 'Parent',
        'description': "A high SAT score can be the key to unlocking life-changing scholarships. TeachTap's proven strategies and personalized approach have helped thousands of students secure generous financial aid packages, making their college dreams a reality."
    },
    {
        'type': 'PARENT EMPOWERMENT',
        'target_audience': 'Parent',
        'description': "Navigating the SAT and college admissions process can leave even the most involved parents feeling helpless. TeachTap's comprehensive resources and progress tracking features give you the tools and insights you need to support your child every step of the way."
    },
    {
        'type': 'SCORE-BOOSTING',
        'target_audience': 'Parent',
        'description': "You know your child is capable of SAT greatness, but unlocking their full potential takes more than just hard work. TeachTap's AI technology identifies your student's unique strengths and weaknesses, delivering targeted practice and Ivy League strategies that guarantee score improvements."
    },
    {
        'type': 'DREAM-ACHIEVING',
        'target_audience': 'Parent',
        'description': "Your child's college dreams are your dreams too. TeachTap's personalized, adaptive learning platform and proven results give your student the tools and confidence they need to aim high and achieve the SAT score that will open doors to their dream school."
    },
    {
        'type': 'FAMILY TRANSFORMED',
        'target_audience': 'Parent',
        'description': "You've seen firsthand how the stress and pressure of the SAT can take a toll on your whole family. TeachTap's engaging platform, 24/7 support, and proven results not only help your child succeed but also bring newfound confidence and harmony to your entire household."
    },
    {
        'type': 'SUMMER ADVANTAGE',
        'target_audience': 'Parent',
        'description': "Summer is the ideal time for your child to get ahead on SAT prep, but finding a flexible program that fits your family's schedule can be a challenge. TeachTap's AI-powered platform adapts to your student's unique needs and timeline, ensuring they make the most of their break and start senior year with a competitive edge."
    },
    {
        'type': 'ACCESSIBLE EXCELLENCE',
        'target_audience': 'Parent',
        'description': "You want your child to have access to the same top-tier SAT strategies as their peers from wealthy families, but the cost of high-end tutoring can be prohibitive. TeachTap's AI technology brings the proven methods of elite tutors to your child's fingertips at a fraction of the cost, ensuring they have every opportunity to succeed, regardless of your family's financial situation."
    },
    {
        'type': 'SMART INVESTMENT',
        'target_audience': 'Parent',
        'description': "As a parent, you understand that investing in your child's education is one of the most important decisions you'll make. TeachTap's AI-powered SAT prep delivers the highest return on your investment, providing the most efficient and effective path to score improvements that can open doors to prestigious colleges and life-changing scholarships."
    }
]
