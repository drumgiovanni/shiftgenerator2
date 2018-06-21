# Shiftgenerator2

This app can help you generating the work shift and work report for parttimeworker in yomiuri hensei department.
読売編成部バイトのシフト作成と勤務報告書作成を手助けするアプリです。

## Login


初めてアクセスすると、ログイン画面が出てきます。


![ログイン画面](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss1.png)


所定の項目を埋めて、ログインしてください。


ログインするとこのような画面が見えているはずです。

![TOP画面](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss2.png)


**初めてこのシステムを利用する際は、まず初めに、一番上の「従業員情報を登録する」をクリックし、従業員情報を登録してください！！**



「○月分のシフト作成」を選択すると来月分のシフトの作成、「シフトアーカイブ」を選択すると今までに作成したシフトのダウンロード、「勤務報告書作成」を選択すると勤務報告書の作成ができます。

## シフト作成
最初の画面

![画面の写真](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss1.png)

シフトを組み始めるには「**始めよう**」 , 使い方がわからない場合は「**使い方**」 をクリック！



### シフトの組み方


「始めよう」をクリックすると、以下のような画面になります。

![画面の写真](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss2.png)


画面上部に翌月のカレンダー、及び、祝日・休刊日が表示されます。

画面下部に所属する従業員 ***全員分*** の情報を入力していきます。
手順としては、

1. 名前を入力

1. 属性を選択（平日勤務 or 土日勤務）

1. 休み希望を入力（出勤できない日を **半角数字をコンマ区切り** で入力してください。）  
        ※土日要員は、土日祝の中から出勤できない日を入力してください。(平日は自動的に休みになるようになってます。)

        例） 1,8,15,22
        なお、出勤できない日が無い場合は、何も入力しなくてokです。

1. 一従業員分の情報の記入が完了したら、「登録する」をクリック  
        「登録する」をクリックすると、登録された従業員の情報が表示されます。  
        ※ ミスした場合は、再読み込みしてください。リセットされます。

1. 全従業員の情報の記入が完了したら、「従業員の登録を完了する」をクリック(画面が遷移します。)  
     ![画面の写真](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss10.png)

1. 「ダウンロード」をクリック  
        好きな場所に生成されたエクセルシートを保存できます。  


ここまでの流れを動画にするとこんな感じ⬇︎

![再現映像](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/mv1.gif)



### 完成したエクセルシートについて

ダウンロードしたエクセルファイルを開いてみましょう。  
※MicrosoftExcelが無い場合、[googleスプレッドシート](https://www.google.com/intl/ja_jp/sheets/about/)が無料で使えて便利（スマホでもアプリをダウンロードすることで使える）

![完成したエクセルシートの画像](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss4.png)

☝︎これが完成したシフトです（全体写すために縮小したら見づらくなっちゃった）。  
見たらわかる通り、土曜日は緑、日曜日・祝日は赤、休刊日は黒塗りになっています。  


画面の下の方を見てもらうと、現在"5月"というタブにいることがわかります。  
このタブでは、完成したシフトを表示しています。  

"workerlist"というタブでは、従業員の勤務可能日が表示されています。  
万が一シフトを変更するとなった際に、参考にできるかと思います。  

"workingday"というタブでは、従業員の出勤日が○・×で表示されています。  
 好きに使ってください。  

![エクセル動画](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/mv2.gif)

なお、ダウンロードしたエクセルファイルは好きに編集していただいて大丈夫です。  
手入力でシフトの微調整等の柔軟に対応していただければと思います。  


ちなみに、スマホでも使えます。  
スマホで使用する際は、Excelやgoogle spreadsheet等のアプリをインストールしてから使ってください。  

---

あ、もし、土日要員が平日入るシフトを組む場合、以下２通りの方法で対応してください。  

1. 手入力で修正  

1. 属性の項目で平日勤務を選択し、平日・土日祝の中から出勤できない日を休み希望として記入する。  


---  



## シフトアーカイブ  

このページでは、今までに作成したシフトをダウンロードできます。

<br>

最初の画面  


![最初の画面](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss3.png)  


今まで作成したシフトが、ページ中央付近に表示されます。  
 

![シフト表示](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss4.png)  


そして下のセレクトボックスからダウンロードしたいシフトを選択し、ダウンロードするをクリック！  

![ダウンロード方法](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss5.png)  


## TOP画面に戻るには

左上の**Shift-generatorへようこそ**をクリックするとTOP画面に戻ることができます。


---  



## 勤務報告書作成

このページでは勤務報告書を作成し、ご希望のメールアドレスに送信することができます。  


最初の画面  


![最初の画面](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss6.png)  



「始めよう」をクリック！！  
するとこのような画面になります。  

![次の画面](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss7.png)

### 初めて利用する場合  

このシステムを初めて利用する人は、所定の項目を埋めてください。　　
　　※なお、作成する勤務報告書の月は、今までに作成されたシフトと紐付けられているため、シフトが存在しない月は選択することができません。また、メールアドレスは読売のアドレスをお勧めします。  

全て入力できたら、「登録する」を押してください。入力された情報がデータベースに保存され、次回以降情報を入力する手間が省けます。

### ２回目以降の人

上のセレクトボックスから、自分の名前を選択してください。  
そして、「セットする」をクリックすると、データベースに登録されているデータが呼び出され、欄を埋めてくれます。  


![名前選択](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss8.png)


最後に、「入力完了」をクリックしてください。


これで、勤務報告書の作成および、希望のメールアドレスへ送信が完了しました。  


![完了](https://github.com/drumgiovanni/shiftgenerator2/blob/master/assets/ss9.png)



