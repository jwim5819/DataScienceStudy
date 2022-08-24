library(shiny)
library(ggplot2)
library(gapminder)

server <- function(input, output){
  output$plot <- renderPlot({
    ggplot(subset(gapminder, year == 2007), aes(x = gdpPercap,
                                 y = lifeExp)) + 
      geom_point(aes(color = continent)) +
      scale_x_log10() + 
      geom_smooth()
  })
  
  output$data <- renderTable({
    req(input$plot_click)
    nearPoints(gapminder, input$plot_click)
  })
}

ui <- fluidPage(
  tags$h1('Gapminder 따라해보기:'),
  tags$h3('이것은 그림 그리기:'),
  plotOutput('plot', click = 'plot_click'),
  tags$h3('사용자 클릭에 반응하기:'),
  tableOutput('data')
)

shinyApp(ui, server)

