from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct  # answer: 'a', 'b', 'c', 'd'

def testpaper(request):
    questions = [
        Questions('मापन क्यों आवश्यक है?',
                  '(a) केवल विज्ञान में दिखाने के लिए', '(b) भौतिक मात्राओं को समझने और तुलना करने के लिए', '(c) गणित के लिए', '(d) केवल प्रयोगशालाओं में', 'b'),
        Questions('भौतिक विज्ञान में इकाइयों का क्या महत्व है?',
                  '(a) भ्रम पैदा करने के लिए', '(b) माप को मानकीकृत करने के लिए', '(c) केवल प्रयोगों में', '(d) केवल सिद्धांतों के लिए', 'b'),
        Questions('Accuracy और Precision में क्या अंतर है?',
                  '(a) दोनों एक ही हैं', '(b) Accuracy सही परिणाम के निकट होना, Precision परिणामों का आपस में निकट होना', '(c) Precision सही परिणाम के निकट होना, Accuracy परिणामों का आपस में निकट होना', '(d) कोई अंतर नहीं', 'b'),
        Questions('मापन में त्रुटि किसे कहते हैं?',
                  '(a) सही मापन', '(b) मापन और वास्तविक मान के बीच अंतर', '(c) इकाई परिवर्तन', '(d) कोई फर्क नहीं', 'b'),
        Questions('किसी भौतिक मात्रा को मापने के लिए यंत्र का उदाहरण क्या है?',
                  '(a) Thermometer', '(b) Computer', '(c) Calculator', '(d) Notebook', 'a'),
        Questions('सटीकता (Accuracy) बढ़ाने के लिए क्या करना चाहिए?',
                  '(a) बेहतर यंत्र का प्रयोग', '(b) जितनी जल्दी हो सके मापन करना', '(c) मापन को नजरअंदाज करना', '(d) केवल अनुमान लगाना', 'a'),
        Questions('मापन में Fundamental Units क्या हैं?',
                  '(a) आधारभूत भौतिक मात्राएँ जैसे लंबाई, द्रव्यमान, समय', '(b) Derived Units', '(c) किसी भी मात्रा के अनुमान', '(d) केवल वजन', 'a'),
        Questions('Derived Units क्या हैं?',
                  '(a) मूलभूत मात्राओं से बने यूनिट', '(b) किसी भी यूनिट', '(c) केवल समय की इकाई', '(d) कोई यूनिट नहीं', 'a'),
        Questions('मापन में Significant Figures किसे कहते हैं?',
                  '(a) केवल पहला अंक', '(b) मापन के भरोसेमंद अंक', '(c) कोई भी अंक', '(d) अंतिम अंक', 'b'),
        Questions('मापन के बिना विज्ञान क्यों असंभव है?',
                  '(a) विज्ञान में मापन की जरूरत नहीं', '(b) किसी भी भौतिक तथ्य का सटीक अध्ययन संभव नहीं', '(c) केवल अध्ययन के लिए', '(d) केवल प्रयोगशाला के लिए', 'b'),



                    Questions('एक स्टील की छड़ी की लंबाई 2.345 m है। इसे cm में व्यक्त कीजिए।',
                            '(a) 23.45 cm', '(b) 234.5 cm', '(c) 234.5 m', '(d) 2.345 cm', 'b'),
                    Questions('किसी वाहन की गति 90 km/h है। इसे m/s में व्यक्त कीजिए।',
                            '(a) 25 m/s', '(b) 15 m/s', '(c) 20 m/s', '(d) 30 m/s', 'c'),
                    Questions('किसी वस्तु का द्रव्यमान 0.75 kg है। इसे ग्राम में व्यक्त कीजिए।',
                            '(a) 750 g', '(b) 75 g', '(c) 0.75 g', '(d) 7.5 g', 'a'),
                    Questions('किसी कमरे का तापमान 300 K है। इसे °C में व्यक्त कीजिए।',
                            '(a) 27 °C', '(b) 26.85 °C', '(c) 30 °C', '(d) 273 °C', 'b'),
                    Questions('किसी वस्तु की लंबाई 125 cm है। इसे मीटर में व्यक्त कीजिए।',
                            '(a) 1.25 m', '(b) 12.5 m', '(c) 0.125 m', '(d) 125 m', 'a'),
                    Questions('एक कार 150 km की दूरी 3 घंटे में तय करती है। इसकी औसत गति m/s में बताइए।',
                            '(a) 13.89 m/s', '(b) 50 m/s', '(c) 25 m/s', '(d) 15 m/s', 'a'),
                    Questions('किसी वस्तु का आयतन 2500 cm³ है। इसे m³ में व्यक्त कीजिए।',
                            '(a) 0.0025 m³', '(b) 0.025 m³', '(c) 2.5 m³', '(d) 0.00025 m³', 'a'),
                    Questions('पाइप से 0.5 m³ पानी 10 सेकंड में निकलता है। पानी का बहाव m³/s में बताइए।',
                            '(a) 0.05 m³/s', '(b) 0.5 m³/s', '(c) 0.025 m³/s', '(d) 5 m³/s', 'a'),
                    Questions('किसी वस्तु का द्रव्यमान 2 kg और आयतन 0.001 m³ है। सघनता (Density) ज्ञात कीजिए।',
                            '(a) 2000 kg/m³', '(b) 2 kg/m³', '(c) 20 kg/m³', '(d) 0.002 kg/m³', 'a'),
                    Questions('किसी यंत्र से मापा गया समय 120 सेकंड है। इसे मिनट में व्यक्त कीजिए।',
                            '(a) 2 min', '(b) 12 min', '(c) 0.2 min', '(d) 20 min', 'a'),
    ]

    # If student submits the test
    if request.method == "POST":
        score = 0
        detailed_result = []

        for i, q in enumerate(questions, 1):
            selected_option = request.POST.get(f'option{i}')  # user's selected option

            # Score increase
            if selected_option == q.correct:
                score += 1

            # Store detailed question review
            detailed_result.append({
                'question': q.que,
                'options': [q.a, q.b, q.c, q.d],
                'correct': q.correct,
                'selected': selected_option
            })

        total = len(questions)
        percentage = round((score / total) * 100, 1)

        context = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'result': detailed_result
        }
        return render(request, 'result.html', context)

    # First time load
    return render(request, 'question.html', {'questions': questions})