# Team Bit Brigade - Sudhee Hackathon 2024

## Problem Statement

### AI, ML and Data Science - Problem Statement 3

Over the past few years technology has advanced by leaps and bounds but to report an emergency
(fire accidents, road accidents etc.) we still have to wait on a phone call for an operator to pick up.
There is also no way for the victim to show any evidence of an emergency or an accident. Create a
chatbot that can collect preliminary information about the emergency just like an operator would
over a phone call. The question asked by the chatbot should be based on the type of incident. It
should also be able to accept images and other files when relevant.

## Our thoughts

In an era marked by rapid technological advancement, emergency reporting systems remain largely reliant on traditional phone calls to connect victims with operators. This method often results in delays and lacks the capability for victims to provide tangible evidence of the emergency or accident. To address this issue, we propose the development of an innovative chatbot system designed to streamline the emergency reporting process. The chatbot will emulate the role of a human operator, gathering preliminary information from victims based on the type of incident reported. Additionally, the chatbot will integrate image and file uploading functionalities to allow users to submit relevant evidence alongside their reports. By leveraging artificial intelligence and multimedia capabilities, our solution aims to enhance the efficiency and effectiveness of emergency reporting systems, ultimately facilitating quicker response times and improved emergency management outcomes.

## Solution Description

The proposed technical solution involves the development of a sophisticated chatbot system leveraging natural language processing (NLP) techniques and multimedia processing capabilities.

1. **Natural Language Understanding (NLU)**: The chatbot will utilize advanced NLP algorithms to comprehend and interpret user inputs effectively. This includes understanding the nature of the emergency or accident reported and extracting relevant information such as location, type of incident, and severity.

2. **Contextual Questioning**: Based on the type of incident reported, the chatbot will dynamically generate contextually relevant questions to gather comprehensive information from the user. For example, in the case of a fire emergency, the chatbot may ask about the size of the fire, presence of smoke, and potential hazards.

3. **Multimedia Integration**: To address the limitation of traditional phone-based reporting systems, the chatbot will support multimedia file uploads, allowing users to submit images, videos, or other relevant files as evidence. Advanced image and file processing techniques will be employed to analyze and extract relevant information from uploaded files.

4. **Real-Time Communication**: The chatbot will facilitate real-time communication between users and emergency response teams, transmitting the collected information to the appropriate authorities promptly. Integration with existing emergency response systems and protocols will ensure seamless coordination and efficient dispatch of resources.

5. **Scalability and Accessibility**: The chatbot will be designed to scale according to demand and accessible across multiple platforms including web, mobile devices, and messaging applications. This ensures widespread accessibility and ease of use for individuals in need of emergency assistance.

6. **Security and Privacy**: Robust security measures will be implemented to safeguard user data and ensure compliance with privacy regulations. Encryption techniques will be employed to protect sensitive information transmitted through the chatbot.

By combining advanced NLP capabilities with multimedia integration and real-time communication features, the proposed chatbot system offers a comprehensive technical solution to streamline the emergency reporting process and improve overall emergency management outcomes.

### Technical Details (subject to change as we experiment with different approaches)

1. **Programming Language** - Python
2. **Encoder** - all-MiniLM-L6-v2 sentence transformer
3. **Image classifier** - a resnet50 based classifier trained on 5 labels(infra damage, human damage, urban fires, wild fires, land slides), which takes in 300x300 image and classifies it
4. **Chat bot** - a basic chatbot which chooses the reply appropriate response based on the cosine similarity between the response n replies

## Usecases

1. **Emergency Reporting**: Allow users to report various emergencies such as fire accidents, medical emergencies, road accidents, natural disasters, etc., through the chatbot. Users can provide details such as location, type of emergency, and any additional information required for effective response.

2. **Evidence Submission**: Enable users to upload images, videos, or documents as evidence accompanying their emergency reports. This can include photos of the accident scene, medical records, or any other relevant documentation to assist emergency responders in understanding the situation better.

3. **Real-Time Updates**: Provide real-time updates to users regarding the status of their emergency report, such as confirmation of receipt, estimated response time, and any follow-up actions taken by emergency services.

4. **Emergency Preparedness Information**: Offer users information and resources on emergency preparedness, including safety tips, evacuation procedures, and contact details for relevant emergency services.

5. **Language Translation**: Support multilingual capabilities to cater to diverse user populations, ensuring that individuals who speak different languages can effectively communicate their emergencies and receive assistance.

6. **Anonymous Reporting**: Allow users to report emergencies anonymously if they prefer not to disclose their identity, ensuring that individuals feel comfortable seeking help without fear of repercussions.

7. **Integration with Emergency Services**: Integrate the chatbot with existing emergency response systems to automatically dispatch appropriate services based on the reported emergency type and location, improving response times and coordination.

8. **Community Engagement**: Foster community engagement by enabling users to share emergency preparedness tips, safety advice, and personal experiences with others through the chatbot platform, creating a supportive and informed community.

These use cases demonstrate the versatility and potential impact of the chatbot solution in enhancing emergency reporting and response processes, improving user experience, and ultimately contributing to safer and more resilient communities.

## Useful Links

GitHub Repository - [https://github.com/gjaynir0508/sudhee-hackathon-2024](https://github.com/gjaynir0508/sudhee-hackathon-2024)

Kaggle Link - [https://www.kaggle.com/code/gjaynir0508/notebook5b172bee27](https://www.kaggle.com/code/gjaynir0508/notebook5b172bee27)
