function echo() {
    document.getElementById('Echoalexa').classList.toggle('active');
}
function echo1() {
    document.getElementById('Echoalexa1').classList.toggle('active');
}
function echo2() {
    document.getElementById('Echoalexa2').classList.toggle('active');
}
function echo3() {
    document.getElementById('Echoalexa3').classList.toggle('active');
}
function echo4() {
    document.getElementById('Echoalexa4').classList.toggle('active');
}
function echo5() {
    document.getElementById('Echoalexa5').classList.toggle('active');
}
function echo6() {
    document.getElementById('Echoalexa6').classList.toggle('active');
}
function echo7() {
    document.getElementById('Echoalexa7').classList.toggle('active');
}
function echo8() {
    document.getElementById('Echoalexa8').classList.toggle('active');
}
function echo9() {
    document.getElementById('Echoalexa9').classList.toggle('active');
}
function echo10() {
    document.getElementById('Echoalexa10').classList.toggle('active');
}
function echo11() {
    document.getElementById('Echoalexa11').classList.toggle('active');
}
function echo12() {
    document.getElementById('Echoalexa12').classList.toggle('active');
}
function echo13() {
    document.getElementById('Echoalexa13').classList.toggle('active');
}
function echo14() {
    document.getElementById('Echoalexa14').classList.toggle('active');
}
function echo15() {
    document.getElementById('Echoalexa15').classList.toggle('active');
}
function echo16() {
    document.getElementById('Echoalexa16').classList.toggle('active');
}
function echo17() {
    document.getElementById('Echoalexa17').classList.toggle('active');
}
function echo18() {
    document.getElementById('Echoalexa18').classList.toggle('active');
}
function echo19() {
    document.getElementById('Echoalexa19').classList.toggle('active');
}
function All() {
    document.getElementById('All').classList.toggle('active');
}
function updateyourlocat() {
    document.getElementById('updateyourlocation').classList.toggle('active');   
}

function allshows() {
    document.getElementById('allshows').classList.toggle('active');
}
function allshowsR() {
    document.getElementById('allshows').classList.remove('active');
}

function showarrow(clickedElement) {
    // clickedElement is the <p> tag
    const downArrow = clickedElement.querySelector('.arrow-down');
    const upArrow = clickedElement.querySelector('.arrow-up');

    if (downArrow && upArrow) {
        // Toggle visibility
        if (downArrow.style.display !== 'none') {
            downArrow.style.display = 'none';
            upArrow.style.display = 'inline';
        } else {
            downArrow.style.display = 'inline';
            upArrow.style.display = 'none';
        }
    }
}



