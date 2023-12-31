const url=window.location.href
console.log(url)
const quiz= document.getElementById('quiz_box')
$.ajax({
    type:'GET',
    url:`${url}data`,
    success:function(response)
    {
        console.log(response)
        const data=response.data
        data.forEach(el=>{
        for(const[question,answer] of Object.entries(el)){
//            console.log(question)
//            console.log(answer)

            quiz.innerHTML+=`
            <hr>
            <div class="mb-2">
            <b>${question}</b>

            </div>

            `
            answer.forEach(answer=>{
            quiz.innerHTML+=`
            <div>
                <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                <label for="${question}">${answer}</label>

            </div>
            `
            })
        }
        });
    },
    error:function(error)
    {
    console.log(error)
    }
})