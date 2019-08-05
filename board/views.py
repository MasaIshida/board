from django.shortcuts import render, redirect
from .models import BoardBase
from .forms import PostForm, MakeBoard
from django.core.mail import send_mail

# Create your views here.


#--------------------------TopView----------------------------------------

def topview(request):
    #トップページ表示する場合viewステータスが一番多い記事を6つ抽出
    object_list = BoardBase.objects.order_by('-board_view')
    object_list2 = []
    n = 0
    for i in object_list:
        object_list2.append(i)
        n += 1
        if n == 6:
            break
    return render(request, 'top.html', {'object_list': object_list2})

#--------------------------------------------------------------------------








#--------------------------掲示板detaiView----------------------------------

def detail(request, pk):
    if request.method == 'POST':
        #投稿リクエストが入った場合
        form = PostForm(request.POST)
        if form.is_valid():
            object = BoardBase.objects.get(pk=pk)
            form.post_category = object
            form.save()
    else:
        form = PostForm()
        object = BoardBase.objects.get(pk=pk)
        #ユーザーが訪問した場合viewステータスを更新する
        object.board_view += 1
        object.save()
    object2 = object.serch_title.all()
    return render(request, 'detail.html', {'object_list': object2, 'objects': object, 'form': form})

#--------------------------------------------------------------------------






#--------------------------一覧View-----------------------------------------

def list(request):
    if request.GET.get('q') is not None:
        #検索機能を利用した場合
        search_query = request.GET.get('q')
        object_list = BoardBase.objects.filter(board_title__icontains=search_query)
        page_context = {
            'title': '掲示板検索',
            'title_about': '検索結果が表示されます。',
        }
        return render(request, 'list.html',{'page_context': page_context, 'object_list': object_list})
    else:
        page_context = {
            'title': '新着掲示板',
            'title_about': '最新の掲示板を確認してみよう！新しい情報が手に入るかも。',
        }
        object_list = BoardBase.objects.all()
        object_list2 = []
        for i in reversed(object_list):
            object_list2.append(i)
        return render(request, 'list.html',{'page_context': page_context, 'object_list': object_list2})

#--------------------------------------------------------------------------






#--------------------------掲示板作成View------------------------------------

def make_board(request):
    if request.method == 'POST':
        #入力値がある場合確認画面へ遷移
        form = MakeBoard(request.POST)
        if form.is_valid():
            request.session['form_data'] = request.POST
            return redirect('board_ascertain')
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        # セッションデータがない場合は作成ページへ
        return render(request, 'make_board.html')
    else:
        # セッションデータがる場合は作成ページにセッションデータ反映
        form_data = {
            'board_title': session_form_data.get('board_title'),
            'board_about': session_form_data.get('board_about'),
        }
        return render(request, 'make_board.html', {'ascertain_data': form_data})


def board_ascertain(request):
    #確認画面
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        #セッションがない場合は作成画面へ戻す
        return redirect('create')
    else:
        #セッションがある場合は確認内容を表示
        form_data = {
            'board_title': session_form_data.get('board_title'),
            'board_about': session_form_data.get('board_about'),
        }
        return render(request, 'board_ascertain.html', {'ascertain_data': form_data})


def finish_board_make(request):
    #確認画面から作成するを押した場合はDBへ作成内容保存
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        return redirect('make_board')
    form = MakeBoard(session_form_data)
    if form.is_valid():
        form.save()
        object = BoardBase.objects.last()
        return redirect('detail', object.pk)

#---------------------------------------------------------------------------







#--------------------------問い合わせView------------------------------------

def contact(request):
    if request.method == 'POST':
        if request.POST != "":
            select_type = request.POST.get('contacter_need')
            content_join = '返信先：' + request.POST.get('contacter_address') + '\n' + '内容：' + request.POST.get('contacter_content')
            content = content_join
            this_address = 'board@info.mail'
            send_address = ['masa.mail0517@gmail.com']
            send_mail(select_type, content, this_address, send_address)
            return render(request, 'contact_finish.html',{'title':'問い合わせ'})
    return render(request, 'contact.html')

#---------------------------------------------------------------------------






#--------------------------利用規約View--------------------------------------

def terms(request):
    return render(request, 'terms.html')

#---------------------------------------------------------------------------






#--------------------------プライバシーポリシーView-----------------------------

def policy(request):
    return render(request, 'policy.html')

#---------------------------------------------------------------------------






