#NOTE: These algos will only run properly on the quantopian IDE

"""
   Updated SMA for simple moving average algorithm
"""

def initialize(context):
    context.security_list = [symbol('SPY')]
    
    #Rebalances every day, one hour after open
    schedule_function(my_rebalance, date_rules.every_day(),
                      time_rules.market_open())
    
    #Record variables that are being tracked at close
    schedule_function(my_record_vars, date_rules.every_day(), 
                      time_rules.market_close())
    
def before_trading_start(context, data):
    prices_200 = data.history(context.security_list, 'price', 200, '1d')
    prices_50 = prices_200[-50:]
    
    context.ma50 = prices_50.mean()
    context.ma200 = prices_200.mean()
    
    context.signal = (context.ma50 > context.ma200).to_dict()
    
def my_rebalance(context, data):
    #Provide orders
    
    s = [i for i in context.signal.values()]
    target = sum(s)
    for stock, signal in context.signal.items():
        if signal == True and stock not in context.portfolio.positions:
            order_target_percent(stock, 1./target)
            log.info('Buying Shares.')
            
        if signal == False and stock in context.portfolio.positions:
            order_target_percent(stock, 0)
            log.info('Selling Shares')
            
def my_record_vars(context, data):
    record(MA1 = context.ma50, MA2 = context.ma200,
           leverage=context.account.leverage)
