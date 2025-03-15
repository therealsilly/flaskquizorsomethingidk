def getAllQuizzesQuery():
    return "SELECT * FROM quiz"

def getQuestsByQuizIdQuery(quiz_id):
    return f'''
            SELECT q.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3
            FROM quiz_content qc
            INNER JOIN question q on q.id = qc.question_id
            WHERE qc.quiz_id = {quiz_id}
            '''
