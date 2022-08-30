library(shiny)
library(palmerpenguins)

pg <- penguins
pg <- pg[complete.cases(pg),]

ui <- pageWithSidebar(
  headerPanel(h1("팔머펭귄 데이터셋")),
  sidebarPanel(
    selectInput("indvar", 
                "독립변수는",
                list("종류별" = "species",
                     "섬별" = "island",
                     "성별" = "sex")),
    selectInput("depvar", 
                "종속 변수는",
                list("부리 길이" = "bill_length_mm",
                     "부리 깊이" = "bill_depth_mm",
                     "날개 길이" = "flipper_length_mm",
                     "체질량" = "body_mass_g")),
    
    checkboxInput("outliers",
                  "이상치도 보여주까?",
                  FALSE)),
  mainPanel(
    h3("formula: "),
    h3(textOutput("caption")),
    plotOutput("mpgPlot"))
)

server <- function(input, output) {
  formulaText <- reactive({
    paste(input$depvar, " ~ ", input$indvar)
  })
  output$caption <- renderText({
    formulaText()
  })
  output$mpgPlot <- renderPlot({
    boxplot(as.formula(formulaText()),
            data <- pg,
            outline = input$outliers,
            col = "lightyellow")
  })
}


# web server를 구동 시켜줌
shinyApp(ui = ui, server = server)