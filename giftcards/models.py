from django.db import models
from django.utils.timezone import now

from store.models import Transaction
class Giftcard(models.Model):
	
	#ex. TRADERJOES = 'TJS'
	WHOLEFOODSMARKET = 'WFM'
	ORGANIZATION_CHOICES = (
	# ex. (TRADERJOES, "Trader Joe's"),
		(WHOLEFOODSMARKET, 'Whole Foods Market'),
	)
	
	organization = models.CharField( max_length=4, choices=ORGANIZATION_CHOICES)
	card_id = models.BigIntegerField(unique=True, db_index=True)
	remaining_value = models.DecimalField(decimal_places=2, max_digits=16)
	created_date = models.DateTimeField(default=now)
	transaction = models.ForeignKey(Transaction, null=True, blank=True)
	
	def is_sold(self):
		return self.transaction is not None
    
	is_sold.boolean = True
	is_sold.short_description = 'Is Sold?'
	
	
	
	''' 
	Giftcard Request Info:
	    Request URL:https://app.giftango.com/GiftCardPortal/GiftCardProcessorService/BalanceCheck.asmx/BalanceInquiry
        Request Method:POST
        Status Code:200 OK
        Request Headersview source
        Accept:application/json, text/javascript, */*; q=0.01
        Accept-Charset:ISO-8859-1,utf-8;q=0.7,*;q=0.3
        Accept-Encoding:gzip,deflate,sdch
        Accept-Language:en-US,en;q=0.8
        Connection:keep-alive
        Content-Length:82
        Content-Type:application/json; charset=UTF-8
        Host:app.giftango.com
        Origin:https://app.giftango.com
        Referer:https://app.giftango.com/GiftCardPortal/WholeFoods/GiftCardPortal.aspx?wmode=transparent
        User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22
        X-Requested-With:XMLHttpRequest
        Request Payload
        {"alias": "wholefoods", "giftCardNumber": "6362640027436239" , "giftCardPin": "" }
        Response Headersview source
        Cache-Control:private, max-age=0
        Content-Length:13
        Content-Type:application/json; charset=utf-8
        Date:Wed, 27 Mar 2013 16:57:23 GMT
        P3P:CP="CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR"
        Server:Microsoft-IIS/7.5
        X-AspNet-Version:4.0.30319
        X-Powered-By:ASP.NET
        
    Giftcard Response:
        { d: "50.00" }
	
	'''