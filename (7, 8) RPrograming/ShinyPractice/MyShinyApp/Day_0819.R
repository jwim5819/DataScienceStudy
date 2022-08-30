# 라이브러리 로딩
library(shiny)

ui <- fluidPage(
  tags$h1('Hello Shiny!'),
  selectInput('dataset',
              label = 'Dataset',
              choices = ls('package:datasets')),
  verbatimTextOutput('summary'),
  tableOutput('table')
)

server <- function(input, output){
  dataset <- reactive({
    get(input$dataset, 'package:datasets')
  })
  output$summary <- renderPrint({
    cat(input$dataset)
    summary(dataset())
  })
  output$table <- renderTable({
    head(dataset(), 10)
  })
}

shinyApp(ui = ui, server = server)