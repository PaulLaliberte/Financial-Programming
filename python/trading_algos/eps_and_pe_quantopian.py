#NOTE: THese algorithms only run on the Quantopian IDE.

"""
    Goal: Minimize risk, i.e. only take a position with highest probability
          of succedding.

    Strategy: Short stocks with a low p/e and a high eps.
              Get out of positions if stocks no longer pass screening.

    See, https://goo.gl/4KSlfk ,for results. Result time period: ~ 2011 - 2012.
    Similiar backtesting results for any dates
"""

from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline import CustomFactor
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.data import morningstar
 
class peRatio(CustomFactor):
    inputs = [morningstar.valuation_ratios.pe_ratio]
    window_length = 1

    def compute(self, today, assets, out, pe_ratio):
        print("Computing p/e ratio")
        out[:] = pe_ratio[-1]
    
class eps(CustomFactor):
    inputs = [morningstar.earnings_report.basic_eps]
    window_length = 1
    
    def compute(self, today, assests, out, basic_eps):
        print('Computing eps')
        out[:] = basic_eps[-1]
        
def initialize(context):
    context.limit = 10

    schedule_function(my_rebalance, date_rules.every_day(), time_rules.market_open(hours=1))
    schedule_function(my_record_vars, date_rules.every_day(), time_rules.market_close())
     
    attach_pipeline(pline(context), 'pline')
      
def pline(context):
    pipe = Pipeline()
 
    pe_ratio = peRatio()
    eps_ = eps()
    
    pipe.add(pe_ratio, 'pe_ratio')
    pipe.add(eps_, 'eps_')
    
    #Valuation screen
    isValue = (pe_ratio < 15) & (eps_ > 20)
    
    pipe.set_screen(isValue)
     
    return pipe
 
def before_trading_start(context, data):
    """
    Called every day before market open.
    """
    context.output = pipeline_output('pline')
    
    
    context.short = (context.output['pe_ratio'] > 0).to_dict()
    
def my_rebalance(context,data):
    """
    Execute orders according to our schedule_function() timing. 
    """    
    #short positions that pass screening
    for stock in context.short:
        if context.short[stock] & data.can_trade(stock) & (stock not in context.portfolio.positions):
            order_target_percent(stock, -1./context.limit)
    
    for stock in context.portfolio.positions:
        if data.can_trade(stock):
            if stock not in context.output.index:
                order_target_percent(stock, 0)
    
def my_record_vars(context, data):
  record(Leverage = context.account.leverage,
         positions = len(context.portfolio.positions))
