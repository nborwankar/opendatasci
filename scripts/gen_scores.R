sort(round(runif(12, min=23, max=47)))
# [1] 27 29 30 33 35 36 37 39 40 42 44 45
set.seed(10)
sort(round(runif(12, min=23, max=47)))
# [1] 25 28 30 30 30 33 33 35 37 38 39 40
sort(round(runif(12, min=23, max=47)))
# [1] 24 26 29 32 32 33 33 37 38 42 43 44
sort(round(runif(12, min=5, max=32)))
# [1]  8 10 11 15 16 16 19 24 25 26 28 29

loss <- sort(round(runif(12, min=5, max=32)))
win <- sort(round(runif(12, min=23, max=47)))
lossout <- c(rep(0,12))
winout <- c(rep(1,12))
alloutcomes <- append(lossout, winout)
rawscores <- append(loss,win)
data <- data.frame("scores"=rawscores, "outcomes"=alloutcomes)

names(data)
#[1] "scores"   "outcomes"

plot(data$outcomes ~ data$scores)