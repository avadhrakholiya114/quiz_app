//it return all the buttons means list of button which we have quizes if we have 5 quiz than it return 5


//for perform for each we need to conver into the array that's why we use ... '
const modelButton=[...document.getElementsByClassName('modal-button')]
const modelBody=document.getElementById('modal-body-confirm')
const start_btn=document.getElementById('start-button')
//console.log(modelButton)

const url=window.location.href
modelButton.forEach(modelButton=>modelButton.addEventListener('click',()=>{

/* it display all the detail which is available in button in short it loop all elemtnt from button bcz we conver it into array
 ex :<button class="btn btn-link modal-button" data-pk="1" data-quiz="simple math" data-question="3" data-difficulty="easy" data-time="obj.time" data-pass="obj.requierd_score_to_pass" data-bs-toggle="modal" data-bs-target="#quizeModal"> simple math </button>
  console.log(modelButton)*/
  const pk =modelButton.getAttribute('data-pk')
  console.log(pk)
  const name =modelButton.getAttribute('data-quiz')

  const total_question =modelButton.getAttribute('data-question')
  const difficulty =modelButton.getAttribute('data-difficulty')
  const time =modelButton.getAttribute('data-time')
  const pass =modelButton.getAttribute('data-pass')

    modelBody.innerHTML=`
        <div class="h5 mb-3">Are you sure you want to start "<b>${name}</b>"?</div>
        <div class="text-muted">
    <ul>
        <li>
            difficulty: <b>${difficulty}</b>
        </li>
        <li>
            num_of_question: <b>${total_question}</b>
        </li><li>
            score_for_pass: <b>${pass}</b>
        </li><li>
            time: <b>${time} Min</b>
        </li>
     </ul>
</div>`
    start_btn.addEventListener('click',()=>{
//    set window.location.href to our url
//    console.log(window.location.href)
    window.location.href=url+pk
    })

}))