const url = window.location.href
//console.log(url)
const quiz = document.getElementById('quiz_box')
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        console.log(response)
        const data = response.data
        data.forEach(el => {
            for (const [question, answer] of Object.entries(el)) {
                //            console.log(question)
                //            console.log(answer)

                quiz.innerHTML += `
            <hr>
            <div class="mb-2">
            <b>${question}</b>

            </div>

                `
                answer.forEach(answer => {
                    quiz.innerHTML += `
            <div>
                <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}" />
                <label for="${question}">${answer}</label>

            </div>
            `
                })
            }
        });
    },
    error: function (error) {
        console.log(error)
    }
})

const quiz_form = document.getElementById('quiz-form')
const scoreBox=document.getElementById('score_box')
const resultBox=document.getElementById('result_box')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')];
    const data = {};

    // Use csrf.value directly, no need for csrf[0].value
    data['csrfmiddlewaretoken'] = csrftoken;


    //    use else becuase i don't want' change ans every time if wee set question = null it change when checked otherwise it remain as it is
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    });
    //    console.log('Sending data:', data);

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function (response) {
//            if (response.passed) {
                const results = response.results;
                //                const score = response.score
                //                console.log(score)
                                console.log(results);
                quiz_form.classList.add('not-visible');

                scoreBox.innerHTML=`${response.passed ? 'Congratulations!! ' : 'Oops...:'}Your result is ${response.score.toFixed(2)}%`

                results.forEach(res => {
                    const resDiv = document.createElement("div")
                    for (const [question, resp] of Object.entries(res)) {
                        //                console.log(question)
                        //                console.log(resp)
                        //                console.log('')
                        resDiv.innerHTML += question
                        const cls = ['container', 'p-2', 'text-light', 'h6']
                        resDiv.classList.add(...cls)
                        if (resp == 'Not Answerd') {
                            resDiv.innerHtml += 'Not Answerd'
                            resDiv.classList.add('bg-danger')
                        }
                        else {
                            const answer = resp['answerd']
                            const correct = resp['correct_ans']
                            //                         console.log(answer,correct)
                            if (answer == correct) {
                                resDiv.classList.add('bg-success')
                                resDiv.innerHTML += `answerd : ${answer}`
                            }
                            else {
                                resDiv.classList.add('bg-danger')
                                resDiv.innerHTML += `| correct ansewer : ${correct}`
                                resDiv.innerHTML += `| answerd: ${answer}`
                            }
                        }
                    }

//                for testing append in body
//                    const body = document.getElementsByTagName('BODY')[0];
//                    body.append(resDiv);
                    resultBox.append(resDiv)
                })

//            }
//             else {
//                console.log('Quiz not passed. Score:', response.score);
//            }
        },

        error: function (error) {
            console.log(error);
        }

    });
}

quiz_form.addEventListener('submit', e => {
    e.preventDefault();
    //    console.log('Form submitted!');
    sendData();
});