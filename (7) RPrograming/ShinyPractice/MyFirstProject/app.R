library(shiny)
library(gapminder)
library(ggplot2)

server <- function(input, output){
  output$distPlot <- renderPlot({
    ggplot(subset(gapminder, year == input$year), aes(x = gdpPercap, y = lifeExp)) + 
    geom_point(aes(color = continent)) +
    scale_x_log10() + 
    geom_smooth()
  })
}

ui <- pageWithSidebar(
  headerPanel(
    h1('우리는 악마곰 조입니다: 정윤, 재원, 재환, 한수')
  ),
  
  sidebarPanel(
    selectInput('year',
                '년도 선택',
                seq(1952, 2007, 5))
  ),
  
  mainPanel(
    h3('해당 연도의 GDP대비 기대수명 그래프:'),
    plotOutput('distPlot')
  )
)

shinyApp(ui, server)