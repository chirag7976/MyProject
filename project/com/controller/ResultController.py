from project import app
from flask import render_template, request, session, redirect, url_for
from project.com.controller.LoginController import adminLoginSession, studentLoginSession
from project.com.dao.ResultDAO import ResultDAO
from project.com.vo.ResultVO import ResultVO
from project.com.vo.TestVO import TestVO
from project.com.dao.TestDAO import TestDAO
from project.com.vo.QuestionVO import QuestionVO

# from rake_nltk.rake import Rake
# from datetime import datetime
# from nltk import WordNetLemmatizer
# from nltk.corpus import wordnet as wn
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize



@app.route('/faculty/viewResult')
def facultyViewResult():
    try:
        if adminLoginSession() == 'faculty':
            resultDAO = ResultDAO()
            resultList = resultDAO.viewResult()
            return render_template('faculty/viewResult.html', resultList = resultList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)

@app.route('/faculty/loadPendigResult')
def facultyLoadPendingResults():
    try:
        if adminLoginSession() == 'faculty':
            testVO = TestVO()
            testDAO = TestDAO()

            testVO.test_ResultStatus = 'pending'
            testVOList = testDAO.viewPendingResult(testVO)
            print('asddsaddads', testVOList)
            return render_template('faculty/genrateResult.html', testVOList = testVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)

@app.route('/student/viewResult')
def studentViewResult():
    try:
        if studentLoginSession() == 'student':
            pass
            resultVO = ResultVO()
            resultDAO = ResultDAO()
            resultVO.result_studentId = session['session_stduentId']
            resultList = resultDAO.viewStudentResutl(resultVO)
            return render_template('student/viewResult.html', resultList=resultList)
        else:
            return redirect(url_for('studentLoadLogin'))
    except Exception as ex:
        print(ex)


# @app.route('/facutly/generateResult', methods=['get'])
# def facultyGenrateResult():
#     try:
#         if adminLoginSession() == 'faculty':
#             testId = request.args.get('testId')
#
#             lemmatizer = WordNetLemmatizer()
#
#             resultVO = ResultVO()
#             resultDAO = ResultDAO()
#
#             testVO = TestVO()
#             testDAO = TestDAO()
#
#             questionVO = QuestionVO()
#
#             testVO.testId = testId
#             testVOList = testDAO.viewTest(testVO)
#
#
#             # get Question Seven
#             testQuestionsId = testVOList[0][0].test_QuestionsId
#             testQuestionsIdList = testQuestionsId.split(',')
#
#             #rake : Rapid Automatic Keyword Extraction algorithm
#             rake_ans = Rake()
#
#             #question Object list
#             questionList = []
#
#             for questionId in testQuestionsIdList:
#                 questionVO.questionId = questionId
#                 question = testDAO.viewTestQuestion(questionVO)
#                 questionList += question
#
#             print('question List', questionList)
#
#             #question's answer keyword list
#             questionKeyword = []
#
#             for question in questionList:
#                 #this will remove stop words and genrate keyword by word_tokenize
#                 if questionList.index(question)==6:
#                     # genrating keywords.
#                     englishStopWords = stopwords.words('english')
#                     keyword = word_tokenize(question.keyword)
#                     generatedKeywordList = [item for item in keyword if item not in englishStopWords]
#                     print('Descriptive generatedKeywordList :', generatedKeywordList)
#                     questionKeyword.append(generatedKeywordList)
#                 #this will genrate keyword list from questionId List
#                 else:
#                     print('question from questionList : ', question)
#                     print('question answer Keyword:', question.keyword, ' type of keywords: ', type(question.keyword))
#                     print('question.keyword.split(" "): ' , question.keyword.split(" "))
#                     questionKeyword.append(question.keyword.split(" "))
#                     print('question'  + ' : ' + str(question.keyword.split(" ")))
#             print('Question Orignal Keywords List : ', len(questionKeyword), questionKeyword)
#
#             #synonyms keyword list for different question
#             synonyms_keyword_text = []
#
#             for i in questionKeyword:
#                 row_text = []
#                 for m in i:
#                     #genrate synsets
#                     for j in wn.synsets(m):
#                         #select lemmas form synsets
#                         for k in j.lemmas():
#                             row_text.append(k.name())
#                 synonyms_keyword_text.append(list(set(row_text)))
#
#             print('synonyms_keyword_text: ', synonyms_keyword_text)
#
#             #student's test answers
#             studentAnswerOne = testVOList[0][0].test_AnswerOne
#             studentAnswerTwo = testVOList[0][0].test_AnswerTwo
#             studentAnswerThree = testVOList[0][0].test_AnswerThree
#             studentAnswerFour = testVOList[0][0].test_AnswerFour
#             studentAnswerFive = testVOList[0][0].test_AnswerFive
#             studentAnswerSix = testVOList[0][0].test_AnswerSix
#             studentAnswerSeven = testVOList[0][0].test_AnswerSeven
#
#             print('student Answer One', studentAnswerOne)
#             print('student Answer Two', studentAnswerTwo)
#             print('student Answer Three', studentAnswerThree)
#             print('student Answer Four', studentAnswerFour)
#             print('student Answer Five', studentAnswerFive)
#             print('student Answer Six', studentAnswerSix)
#             print('student Answer Seven', studentAnswerSeven)
#
#             totalMarks = 0                     #total score of test
#
#             for i in range(7):
#                 ###############    Processing User's Answer for Short answer and True/False.  ####################
#
#                 # i= 0 to 5  for check Short answer and True/False.
#                 if i==0:
#                     ans = word_tokenize(testVOList[0][0].test_AnswerOne)
#                     print('tokonizing student anser:', ans)
#                     #genrating synset and lemmas of studentAnswer(testAnswer)
#                     row_text = []
#                     for i in ans:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 row_text.append(k.name())
#                     row_text = list(set(row_text))
#                     print('row_text:', row_text )
#                     print('question answer keywords:', synonyms_keyword_text[0] )
#                     #find matched keywords : row_text vs synonyms_keyword_text[0]
#                     matched_keywords = [item for item in row_text if item in synonyms_keyword_text[0]]
#                     print('matched_keyword', matched_keywords)
#                     #result: Answer is right ot wrong.
#                     if len(matched_keywords) >= 1:
#                         totalMarks +=1
#                         print('Answer one is right.')
#                     else:
#                         print('Answer one is wrong.')
#                     print(totalMarks)
#
#                 if i==1:
#                     ans = word_tokenize(testVOList[0][0].test_AnswerTwo)
#                     print('tokonizing student anser:', ans)
#                     # genrating synset and lemmas of studentAnswer(testAnswer)
#                     row_text = []
#                     for i in ans:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 row_text.append(k.name())
#                     row_text = list(set(row_text))
#                     print('row_text:', row_text)
#                     print('question  answer keywords:', synonyms_keyword_text[1] )
#                     #find matched keywords : row_text vs synonyms_keyword_text[1]
#                     matched_keywords = [item for item in row_text if item in synonyms_keyword_text[1]]
#                     print('matched_keyword', matched_keywords)
#                     # result: Answer is right ot wrong.
#                     if len(matched_keywords) >= 1:
#                         totalMarks +=1
#                         print('Answer two is right.')
#                     else:
#                         print('Answer two is wrong.')
#                     print(totalMarks)
#
#                 if i==2:
#                     ans = word_tokenize(testVOList[0][0].test_AnswerThree)
#                     print('tokonizing student anser:', ans)
#                     # genrating synset and lemmas of studentAnswer(testAnswer)
#                     row_text = []
#                     for i in ans:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 row_text.append(k.name())
#                     row_text = list(set(row_text))
#                     print('row_text:', row_text)
#                     print('question answer keywords:', synonyms_keyword_text[2] )
#                     # find matched keywords : row_text vs synonyms_keyword_text[2]
#                     matched_keywords = [item for item in row_text if item in synonyms_keyword_text[2]]
#                     print('matched_keyword', matched_keywords)
#                     # result: Answer is right ot wrong.
#                     if len(matched_keywords) >= 1:
#                         totalMarks +=1
#                         print('Answer three is right.')
#                     else:
#                         print('Answer three is wrong.')
#                     print(totalMarks)
#
#                 if i==3:
#                     ans = word_tokenize(testVOList[0][0].test_AnswerFour)
#                     print('tokonizing student anser:', ans)
#                     # genrating synset and lemmas of studentAnswer(testAnswer)
#                     row_text = []
#                     for i in ans:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 row_text.append(k.name())
#                     row_text = list(set(row_text))
#                     print('row_text:', row_text)
#                     print('question answer keywords:', synonyms_keyword_text[3] )
#                     # find matched keywords : row_text vs synonyms_keyword_text[3]
#                     matched_keywords = [item for item in row_text if item in synonyms_keyword_text[3]]
#                     print('matched_keyword', matched_keywords)
#                     # result: Answer is right ot wrong.
#                     if len(matched_keywords) >= 1:
#                         totalMarks +=1
#                         print('Answer four is right.')
#                     else:
#                         print('Answer four wrong.')
#                     print(totalMarks)
#
#                 if i==4:
#                     ans = word_tokenize(testVOList[0][0].test_AnswerFive)
#                     print('tokonizing student anser:', ans)
#                     # genrating synset and lemmas of studentAnswer(testAnswer)
#                     row_text = []
#                     for i in ans:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 row_text.append(k.name())
#                     row_text = list(set(row_text))
#                     print('row_text:', row_text)
#                     print('question answer keywords:', synonyms_keyword_text[4] )
#                     # find matched keywords : row_text vs synonyms_keyword_text[4]
#                     matched_keywords = [item for item in row_text if item in synonyms_keyword_text[4]]
#                     print('matched_keyword', matched_keywords)
#                     # result: Answer is right ot wrong.
#                     if len(matched_keywords) >= 1:
#                         totalMarks +=1
#                         print('Answer five is right.')
#                     else:
#                         print('Answer five is wrong.')
#                     print(totalMarks)
#
#                 if i==5:
#                     ans = word_tokenize(testVOList[0][0].test_AnswerSix)
#                     print('tokonizing student anser:', ans)
#                     # genrating synset and lemmas of studentAnswer(testAnswer)
#                     row_text = []
#                     for i in ans:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 row_text.append(k.name())
#                     row_text = list(set(row_text))
#                     print('row_text:', row_text)
#                     print('question answer keywords:', synonyms_keyword_text[5] )
#                     # find matched keywords : row_text vs synonyms_keyword_text[5]
#                     matched_keywords = [item for item in row_text if item in synonyms_keyword_text[5]]
#                     print('matched_keyword', matched_keywords)
#                     # result: Answer is right ot wrong.
#                     if len(matched_keywords) >= 1:
#                         totalMarks +=1
#                         print('Answer six is right.')
#                     else:
#                         print('Answer six is wrong.')
#                     print(totalMarks)
#
#                 print("one word marks :", totalMarks)
#
#                 # i= 6 for generating result for Descriptive Question.
#                 if i==6:
#                     ###############    Processing User's Descriptive Answer  ####################
#                             #generating "sentance tokoniz" of student's answers .
#                     ans = studentAnswerSeven
#                     rake_ans.extract_keywords_from_text(ans)
#                     keywords_ans = rake_ans.get_ranked_phrases()
#                     lemmatizedSentance_keyword_ans = [lemmatizer.lemmatize(i) for i in keywords_ans]
#                     print("User (student) Answer Keywords :",
#                           len(lemmatizedSentance_keyword_ans), lemmatizedSentance_keyword_ans)
#                     print('quations answer seven keywors: ',
#                           len(synonyms_keyword_text[6]), synonyms_keyword_text[6] )
#
#                             #genrating "word tokens" of student's answers.
#                     englishStopWords = stopwords.words('english')
#                     keyword = word_tokenize(ans)
#                     generatedKeywordList = [item for item in keyword if item not in englishStopWords]
#                     print('generatedKeywordList', generatedKeywordList, 'lenth:', len(generatedKeywordList))
#
#                     synonymsWord_keyword_ans = []
#
#                     for i in generatedKeywordList:
#                         for j in wn.synsets(i):
#                             for k in j.lemmas():
#                                 synonymsWord_keyword_ans.append(k.name())
#                     print('synonymsWord_keyword_ans:', synonymsWord_keyword_ans,
#                           'lenth:', len(synonymsWord_keyword_ans))
#
#                     ###############    Processing Questions Descriptive Answer  ####################
#                             # generating "sentance tokonizats" of Question's answers .
#                     rake_ans.extract_keywords_from_text(questionList[6].keyword)
#                     keywords_ans = rake_ans.get_ranked_phrases()
#                     lemmatizedSentance_keyword = [lemmatizer.lemmatize(i) for i in keywords_ans]
#                     print("User Answer Keywords :", len(lemmatizedSentance_keyword), lemmatizedSentance_keyword)
#
#                             # genrating "word tokens" of student's answers.
#                     print('quations answer seven keywors: ', len(synonyms_keyword_text[6]), synonyms_keyword_text[6])
#
#
#
#                     #Sentance Token Count between "Questions Sentance" vs "Test Answer"
#                     sentanceTokenCount = len([item for item in lemmatizedSentance_keyword if item in lemmatizedSentance_keyword_ans])
#                     print('count sentance matched:', sentanceTokenCount )
#
#                     #Sentance Word Token Count between "Question Sentance" vs "Test Answer"
#                     synonymsWordTokenCount = len([item for item in synonyms_keyword_text[6] if item in  synonymsWord_keyword_ans])
#                     print('count of synonyms word tokens matched:', synonymsWordTokenCount)
#
#                     print("SentanceToken count :", sentanceTokenCount,
#                           "matched out of ", len(lemmatizedSentance_keyword))
#                     print('WordTOken count', synonymsWordTokenCount,
#                           'mathced out of ', len(synonyms_keyword_text[6]))
#
#                     #accuracy of Sentance in Answer Seven
#                     accuracyOfSentance = round((sentanceTokenCount * 100) / len(lemmatizedSentance_keyword))
#                     #accuracy of Keyword and Tokens in Answer Seven
#                     accuracyOfTokenWords = round((synonymsWordTokenCount * 100)/ len(synonyms_keyword_text[6]))
#
#                     print("Accuracy of sentance : ", accuracyOfSentance)
#                     print("Accurecy of token word :", accuracyOfTokenWords)
#
#                     #result score of Descriptive Answer
#                     accuracy = (accuracyOfTokenWords * 0.7) + (accuracyOfSentance * 0.3)
#
#                     print('final accuracy of Descriptive answer : ', accuracy)
#
#                     #Descriptive Question has 4 points.
#                     totalMarks += 4*(accuracy/100)
#
#             print('total marks : ', totalMarks)
#
#             # insert into resultmaster
#             resultVO.result_loginId = session['session_loginId']
#             resultVO.result_studentId = testVOList[0][0].test_LoginId
#             resultVO.result_testId = testId
#             resultVO.resultDate = datetime.now().strftime('%d/%m/%Y')
#             resultVO.resultTime = datetime.now().strftime('%H:%M')
#             resultVO.resultScore = totalMarks
#             resultDAO.insertResult(resultVO)
#
#             #update test_ResultStatus in resultmaster
#             testVO.testId = testId
#             testVO.test_ResultStatus = 'generated'
#             testDAO.insertTestData(testVO)
#             return redirect(url_for('facultyViewResult'))
#         else:
#             return redirect('/')
#     except Exception as ex:
#         print(ex)