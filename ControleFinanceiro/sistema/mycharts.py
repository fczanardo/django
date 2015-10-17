#	mycharts.py  
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.lib import colors
from reportlab.lib import colors
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label

class MyBarChartDrawing(Drawing):
	def __init__(self, width=800, height=400, *args, **kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.add(HorizontalBarChart(), name='chart')
		self.add(String(220,350,'Grafico Comparativo'), name='title')
		self.chart.x = 20
		self.chart.y = 15
		self.chart.width = self.width - 100
		self.chart.height = self.height - 50
		self.chart.bars[0].fillColor  = colors.red
		self.chart.bars[1].fillColor  = colors.green
		self.title.fontName = 'Helvetica-Bold'
		self.title.fontSize = 30
		self.chart.data = [[0,180,200]]
		self.add(String(25,200,'GANHO'), name='ganho')
		self.add(String(25,150,'DESPESA'), name='despesa')
		self.ganho.fontSize = 15
		self.despesa.fontSize = 15
		self.add(String(550,25,'(considerado MES e ANO)'), name='info')
		self.info.fontSize = 15