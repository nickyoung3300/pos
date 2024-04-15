from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Menu, OrderItem, Order
import json
from django.db.models import Sum
from datetime import datetime, timedelta



def postest1(request):

	if request.method == 'POST':
		


		items = []
		for key, value in request.POST.items():
			if key.startswith('items-'):
				try:
					items.append(json.loads(value))
				except json.JSONDecodeError:
            # 處理無效的 JSON 資料 (可選)
					pass
		order = Order.objects.create()
		total_price = 0
		for item_data in items:
			order_item = OrderItem.objects.create(
                order=order,
                name=item_data['name'],
                suger=item_data['suger'],
                temp=item_data['temp'],
                quantity=item_data['quantity'],
                unit_price=item_data['unip'],
                price=item_data['price']
				
            )
			print('1') 
			print(type(total_price)) 

			total_price += int(order_item.calculate_total_price()) #要改 int()*int()

			print(total_price) 

		print('3') 
		print(type(total_price)) 
		order.total_price = int(total_price)
        
		order.save()

		print(type(items)) 
		print(items) 
		
     
        

	posMenu = Menu.objects.select_related('category').all()

	
	context = {
		"Menu":posMenu
	}

	
	return render(request, "pos/posbase.html", context=context)



def dashBoard(request):
	today = datetime.today().date()
	seven_days_ago = today - timedelta(days=7)
	revenue = []
	
	# 查詢美意天的訂單，按照日期分組(Group By) 計算 總和
	orders_summary = Order.objects.filter(created_at__date__gte=seven_days_ago).values('created_at__date').annotate(total_price_sum=Sum('total_price')).order_by('created_at__date')
	for summary in orders_summary:
		revenue
		print("日期:", summary['created_at__date'], "总销售额:", summary['total_price_sum'])
	
	revenue = [
    {
        "date": summary["created_at__date"],
        "total_price_sum": summary["total_price_sum"],
    }
    for summary in orders_summary
	]
	print(revenue)
	#print(orders_summary)
	context = {}
	context  = {
		"obj":revenue
	}

	#<QuerySet [{'created_at__date': datetime.date(2024, 3, 31), 'total_price_sum': Decimal('5350.00')},
	# {'created_at__date': datetime.date(2024, 4, 1), 'total_price_sum': Decimal('4010.00')},
	# {'created_at__date': datetime.date(2024, 4, 2), 'total_price_sum': Decimal('2615.00')}]>
	# SQL 為
	# SELECT CAST(created_at AS DATE) AS created_at_date, SUM(total_price)
	# FROM post_order
	# GROUP BY created_at_date;
	# 轉換日期類型資料：可以使用 CAST 函數將一種日期類型資料轉換為另一種日期類型資料。
	return render(request, "pos/dashBoard.html", context=context)

