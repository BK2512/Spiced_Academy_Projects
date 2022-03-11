from turtle import width
import streamlit as st 
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

option = st.sidebar.selectbox('Chose your page',('Introduction','Results Guardian','Spiegel comparison'))

st.title("Analyse of the Guardien Newspaper during November'21 till February'22")
st.image(image="Guardien200.webp")

if option=='Introduction':
    
    st.write('The Guardian is a British daily newspaper which was founded 1821. It has a circulation of about 105k.')
    
    st.write('We are using **Topic Modelling (LDA=Latent Dirichlet allocation)** to analyze the data of the newspaper.')
    
    st.write('LDA is the process of identifying topics in a set of ducuments. \nIt\'s an unsupervised machine-learning model that takes **documents as input and finds topics as output**.')

    st.write('Following steps were made to get the results:')
    
    st.image(image="Roadmap.png")
    
    st.write('1. Getting the data via wep API from the guardien -> registration necessary')
    st.write('2. Output are Json-files')
    st.write('3. In here, it is kind of a dictionary, filter to just get the <bodytext>(using for-loops)')
    st.write('4. Saving these as Text files on our local computer, that we don\'t need any web scraping anymore')
    st.write('5. Loading the text files again and prepare them for the LDA-Model:')
    st.write(' 5.1 Setting up stopwords from nltk + extend the list by further words')
    st.write('5.2 Using punctuation to get rid of all marks or symbols')
    st.write('5.3 Using WordNetLemmatizer to converting a word to its base form ')
    st.write('6. Further preprocessing with the cleaned data')
    st.write('7. Train an LDA-modell from gensim, chosing to extract the data in 4 Topics')
    st.write('8. Implement the Model for each month and the weeks from november till now')
    st.write('9. Visualize the data with pyLDAvis')



if option=='Results Guardian':
    #Full November
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.write("""### Main Topics of the Gurardien Newsletters in whole November
            \n- Omicron -> found in europe the first time
            \n- Vaccine/variant
            \n- Case""")
    
    htmlfile=open('./HTML_Files/November_full.html').read()
    components.html(htmlfile,width=1300,height=900,scrolling=True)

    #2 Week of November
    st.write("""### Cloud Map second November week(08-14.11)
            \n- Time,Lap,hamilton,verstappen -> Australien GB was cancelled
            \n- Clima is mentioned 
            \n- Nothing with covid""")
    
    st.image(image="secondnov.png")

    #3 week of november
    st.write("""### Third week of November(15-21.11)
            \n- Nearly nothing with covid
            \n- Mainly about politic
            \n- As always some sport like F1""")

    htmlfilenov1=open('./HTML_Files/Nov_week_three.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #4 week of november
    st.write("""### Fourth week of November(22-28.11)
            \n- Almost everything is about covid and the omicron variant
            \n- Still a bit politics
            \n- As always some sport
            \n- Climate is again out of the focus""")

    htmlfilenov1=open('./HTML_Files/Nov_week_four.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #full Dezember
    st.title('December')

    st.write("""### Full December
            \n- Almost everything is about covid and the omicron variant
            \n- Still a bit politics
            \n- No sport anymore
            """)

    htmlfilenov1=open('./HTML_Files/December_full.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #1 week of december
    st.write("""### First week of December(06.12-12.12)
            \n- Highest ranked topic is about F1 -> as there was the F1 Final
            \n- Still a bit politics
            \n- Covid in the first week is just a 'smaller'topic
            """)

    htmlfilenov1=open('./HTML_Files/Dec_week_one.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #3 week of december
    st.write("""### Cloud map third December week(20-26.12)
            \n- Most topic this week is about football
            \n- Words like: league/chelsea/city/west/team/game/goal/premiere etc. 
            \n- Covid is here just mentioned very less
            \n- Archbishop Desmond Tutu died -> Topic2
            """)
    
    st.image(image="thirddec.png")

    #full January
    st.title('January')
    st.write("""### Full January
            \n- Most relevant topics are about russia now
            \n- Keywords: russian/ukraine/sanction
            \n- Also other topics are found like: party/Johnsen,australia
            \n- Covid is still high ranked, but less important then month's before
            """)

    htmlfilenov1=open('./HTML_Files/January_full.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #2 week of january
    st.write("""### Second week of January(10-16.01)
            \n- Most ranked topic is about australia and djokovic
            \n- Also the party gate is represented(topic3)
            \n- Still, covid is not the biggest topic anymore
            """)

    htmlfilenov1=open('./HTML_Files/Jan_week_two.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #4 week of january
    st.write("""### Fourth week of January(24-30.01)
            \n- Highest ranked topic in this week is american football(end of playoffs)
            \n- The whole week is most about sports, also Soccer and Tennis
            \n- Covid is not anymore present 
            \n- Also the russia/ukraine conflict is not anymore in the focus
            """)

    htmlfilenov1=open('./HTML_Files/Jan_week_four.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #full february
    st.title('February')
    st.write("""### Full February
            \n- Everything is just about russia and ukraine
            \n- Words like war/putin etc are now listed
            \n- Most topics we see during the first weeks are not relavant anymore
            \n- Means in week 4 are so much news about these topics, that they're already overwriting the whole month 
            """)

    htmlfilenov1=open('./HTML_Files/February_full.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #1 week of february
    st.write("""### Cloud map first February week(01-06.02)
            \n- Nothing about russia
            \n- Covid is represented just very low 
            \n- In topic 2 we see a bit of sports (one week later is the super bowl)
            \n- Seems overall more politically
            """)
    
    st.image(image="firstfeb.png")

    #2 week of february
    st.write("""### Second week of February(07-13.02)
            \n- Highest ranked topics are now the russia/ukraine crises
            \n- See words like invasion/ukraine/russia/military/diplomatic
            \n- See still a bit of sports
            """)

    htmlfilenov1=open('./HTML_Files/Feb_week_two.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)

    #3 week of february
    st.write("""### Third week of February(14-20.02)
            \n- Covid still not a high ranked topic
            \n- Russia/ukraine conflict is also not at the top
            \n- England and suisse are highly ranked -> announcement of a alzheimer society firendship game
            \n- Topic 4 is mainly about football again
            """)

    htmlfilenov1=open('./HTML_Files/Feb_week_three.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)
    
    #4 week of february
    st.write("""### Fourth week of February(21-25.02)
            \n- Every topic is just about the ukraine/russian conflict and the war
            """)

    htmlfilenov1=open('./HTML_Files/Feb_week_four.html').read()
    components.html(htmlfilenov1,width=1300,height=900,scrolling=True)
    
    
    
if option=='Spiegel comparison':
        st.title('Let\'s see a comparison to a german newspaper')
        st.image(image="Spiegel_logo.png")
        st.write('## Here are the results of the LDA-model of \'Der Spiegel\' on a monthly basis')
        st.write('For the german newspaper Spiegel we could just extract the headliners of each articel. Therfore, the LDA model could not work as accurate as for the Guardian')
        
        #Spiegel November
        st.write("""### LDA of November
            \n- It is mainly about covid and the \'Impfpflicht\'
            \n- Also about the omicron variant
            \n- We see here comparable topics like in the Guardian
            \n- Both have the main topic of Covid/Omicron
            """)
        
        htmlfilenov1=open('./HTML_Files/Spiegel_nov.html').read()
        components.html(htmlfilenov1,width=1300,height=900,scrolling=True)
        
        #Spiegel December
        st.write("""### LDA of December
            \n- Topics are silvester and new year in terms of how corona will expand and how it goes so far
            \n- It is also about sports and the upcoming Olympics
            \n- Olaf Scholz as the new Chancellor
            \n- It is different than in the Guardien
            \n- Spiegel is talking more about 'Boulevard'topics like silvester ->Topic4 -> 'scheiße'?
            \n- In the Guardian the topics are more about corona->probable because of the 'Freedom Day'
            """)
        
        htmlfilenov1=open('./HTML_Files/Spiegel_Dez.html').read()
        components.html(htmlfilenov1,width=1300,height=900,scrolling=True)
        
        #Spiegel Januar
        st.write("""### LDA of January
            \n- Allready a lot about the russian/ukraine crises
            \n- But also in the focus is the party gate of Boris Johnsen
            \n- We see comparable topics like in the Guardian
            \n- Same high ranked topics like russie/ukraine and the party gate
            \n- Corona is in both newspaper not the most important topic anymore
            """)
        
        htmlfilenov1=open('./HTML_Files/Spiegel_jan.html').read()
        components.html(htmlfilenov1,width=1300,height=900,scrolling=True)
        
        #Spiegel February
        st.write("""### LDA of February
            \n- The same like in the Guardian
            \n- The highest ranked topics are about russia and the war
            \n- Some other topics also, but this occurs due to too little data
            """)
        
        htmlfilenov1=open('./HTML_Files/Spiegel_feb.html').read()
        components.html(htmlfilenov1,width=1300,height=900,scrolling=True)