# git-ksk GitHub Pages

公開サイト: https://git-ksk.github.io/

## トップページ

`index.html` は**App Storeで一般公開中のiOSアプリのみ**を掲載する静的ポートフォリオです。TestFlight限定、審査準備中、審査待ちなどの未公開アプリは掲載しません。

2026-10-12時点でApp Store Connectの `READY_FOR_SALE` と日本のApp Store公開lookupで照合済みのアプリは6本です。

| アプリ | App Store ID | 検証時の公開バージョン |
|---|---:|---|
| Monokura | 6765764522 | 2.6.0 |
| そろそろ | 6764752127 | 1.13.1 |
| 走景 | 6777344136 | 1.2.0 |
| Oh!薬 | 6777269341 | 1.10.1 |
| ツミカブ | 6770018631 | 1.3.2 |
| かるぴく | 6813254279 | 1.1.0 |

一覧の機械可読版は `data/released-apps.json` に保存しています。これは**検証時点の記録**です。サイトにはバージョン番号を固定表示せず、最新版はApp Storeの各掲載ページを参照してください。

アプリアイコンとカードのスクリーンショットは公開中の日本のApp Store掲載素材を取得し、`assets/images/store/{slug}/` に保存しています。外部CDNに依存せず自サイトから画像を配信します。

### アプリ追加・更新

1. App Store Connectで該当アプリに `READY_FOR_SALE` の公開バージョンがあることを確認し、日本の公開lookupでも一般公開を確認する。
2. `data/released-apps.json` を更新する。
3. 最新の公開商品説明に合わせて `index.html` のカードを更新し、App Store掲載中の公式アイコン・スクリーンショットを `assets/images/store/` に保存する。
4. `python3 scripts/check-portfolio.py` で一覧、画像、App Storeリンクの整合性を確認する。PC/スマホ両幅でも表示を確認する。
5. 別ブランチ・PRで `main` に統合し、GitHub Pagesの配信後に公開URLで確認する。

このポートフォリオは静的HTML/CSSです。アプリへの新たなトラッキングSDK、外部データ取得スクリプト、サイト内アナリティクスはありません。

## その他の公開コンテンツ

- `karupic/photo-under-500kb/`: かるぴくの「iPhoneの写真を500KB以下にする方法」ガイド。トップページから直接リンク。
- `karupic/support/`, `karupic/privacy/`: かるぴくのサポート・プライバシー。
- `karumovie/support/`, `karumovie/privacy/`: 将来の配信向けに独立管理するヘルプページ（未公開アプリをトップページには載せない）。
- `app-ads.txt`: AdMob所有権確認用ファイル（既存内容を保持）。
