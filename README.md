# 課題 - APIを使ったアプリ -　（サーバーサイド：バックエンド）

## ①課題の内容（どんな作品）
- MVPの部品としてAPIを使ったサーバーサイド(バックエンド)を作った。
  - ![image](https://github.com/seimei-san/wip_srv/assets/53326909/9a2bf896-2f59-4340-8329-b0779b1ec3d7)
    - 赤破線で囲った部分
  - Symphonyのチャットを受信し、そのメッセージをChatGPTで解析して、５W2Hの有無を判定する機能を実装した。　
    - Symphonyのチャットを捉えるチャットボットを、Symphonyが提供するBDKで実装。　後述のWIPサーバーのAPIに捉えたメッセージを伝送。
      -  このコードは、別のレポジトリーに保存した。 https://github.com/seimei-san/wip_symphony_chatbot.git
    - チャットに５W2Hの存在を確認するサーバーサイド（仮称：WIPサーバー）を、Pythonで実装した。
      - チャットボットから送られるメッセージを受信するAPIを、PythonのFlaskを使って実装。
      - 受け取ったメッセージを、ChatGPTのAPIにメッセージを投げて、ChatGPTから帰る結果を受信
      - ChatGPTに送ったメッセージと受信した結果は、MongoDBに保存するようにした。
  - 残念ながら、フロントエンドを作る時間がなかった。

## ②工夫した点・こだわった点
- チャットのメッセージから、５W２Hを抽出できるように、GhatGPTに投げるプロンプトを工夫した。
- チャットボットのWIPサーバーの連携は、拡張性を考えAPIで構築した。

## ③難しかった点・次回トライしたいこと(又は機能)
- 残念ながら、フロントエンドを作る時間がなかった。　しかしながら、サーバーサイドが出来たので、今後のPHPの課題を通じてPHPをベースにしたフロントエンドを作って行く計画。


## ④質問・疑問・感想、シェアしたいtips等なんでも
[質問]
なし

[疑問]　


[感想]　
  

[tips]　
  

[参考記事]
