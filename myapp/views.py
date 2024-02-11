from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import myapp.recipe
import csv

# Create your views here.
def input(request):
    # GETリクエストの処理: 初期フォームを表示
    return render(request, 'myapp/input.html')

def response(request):
    # POSTリクエストの処理: フォームデータを変数に格納
    textbox1_value = request.POST.get('textbox1')
    textbox2_value = request.POST.get('textbox2')
    
    # ここで変数の値を使って何かする
    csv_data = myapp.recipe.think_flower_recipe("3000円", "素朴")
    lines = csv_data.splitlines()
    reader = csv.reader(lines)
    parsed_csv = list(reader)  # パースされたCSVデータをリストに変換

    # テンプレートにデータを渡す
    context = {'data': parsed_csv}
    return render(request, 'myapp/response.html', {
        'textbox1_value': textbox1_value + "わわわ",
        'textbox2_value': context,
    })