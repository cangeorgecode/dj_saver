const canvas = document.querySelector('#confetti')
const button = document.querySelector('#button')

const jsConfetti = new JSConfetti({ canvas })

button.addEventListener('click', () => {
    jsConfetti.addConfetti({
        confettiRadius: 6,
    })
    console.log('clicked')
})