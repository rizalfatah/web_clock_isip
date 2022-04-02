let clock = document.getElementById("clock-isip").textContent

clock = clock.split(':')

if (clock != "null") {
    let hour = parseInt(clock[0])

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

        document.getElementById("second").innerHTML = s
        document.getElementById("minute").innerHTML = m
        document.getElementById("hour").innerHTML = h
    }, 1000)
} else {
    document.getElementById("clock-container").innerHTML = "Server sedang bermasalah"
    document.getElementById("second").setAttribute("class", "visually-hidden")
    document.getElementById("minute").setAttribute("class", "visually-hidden")
    document.getElementById("hour").setAttribute("class", "visually-hidden")
}
