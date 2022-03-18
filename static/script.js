
let clock = document.getElementById("clock-isip").textContent

// sample output from source:
// - 25:01:20
// - 22:10:40
// - 10:40:23
// let clock = "01:02:03"

clock = clock.split(':')

let hour = parseInt(clock[0])
if (hour > 23) hour -= 24 // handle error hour from clock source (aditiawan)

let minute = parseInt(clock[1])
let second = parseInt(clock[2])

let h, m, s

// load every 1 second
setInterval(function () {
    second++
    if (second >= 60) {
        second = 0
        minute++
        if (minute >= 60) {
            minute = 0
            hour++
            if (hour >= 24) {
                hour = 0
            }
        }
    }

    // plus "0" if only 1 digit in clock

    s = (second < 10) ? '0' + second : second
    m = (minute < 10) ? '0' + minute : minute
    h = (hour < 10) ? '0' + hour : hour

    display_clock = [h, m, s]
    document.getElementById("clock-display").innerHTML = display_clock.join(":")
}, 1000)
