import tkinter.filedialog as fl
import pandas as pd
import os

def get():
    ds_name = [
    "お客様管理番号",
    "送り状種類",
    "クール区分",
    "伝票番号",
    "出荷予定日",
    "お届け予定日",
    "配達時間帯",
    "お届け先コード",
    "お届け先電話番号",
    "お届け先電話番号枝",
    "お届け先郵便番号",
    "お届け先住所",
    "お届け先建物名",
    "お届け先会社・部門１",
    "お届け先会社・部門２",
    "お届け先名",
    "お届け先名略称カナ",
    "敬称",
    "ご依頼主コード",
    "ご依頼主電話番号",
    "ご依頼主電話番号枝",
    "ご依頼主郵便番号",
    "ご依頼主住所",
    "ご依頼主建物名",
    "ご依頼主名",
    "ご依頼主名略称カナ",
    "品名コード１",
    "品名１",
    "品名コード２",
    "品名２",
    "荷扱い１",
    "荷扱い２",
    "記事",
    "コレクト代金引換額",
    "コレクト内消費税",
    "営業所止置き",
    "営業所コード",
    "発行枚数",
    "個数口枠の印字",
    "ご請求先顧客コード",
    "ご請求先分類コード",
    "運賃管理番号",
    ]
    fTyp = [("B2クラウドファイル", "*.csv")]
    iDir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'DownLoads')
    path=fl.askopenfilename(filetypes=fTyp, initialdir=iDir)
    df = pd.read_csv(path, encoding='cp932', header=None, names=ds_name, index_col=None)
    df.fillna({'クール区分': '1'}, inplace=True)
    df.fillna({'配達時間帯': '0812'}, inplace=True)
    df.replace({'配達時間帯': {"午前中": "0812", "14時～16時": "1416", "16時～18時": "1618", "18時～20時": "1820", "19時～21時": "1921", "午前10時まで": "0010", "午後5時まで": "0017"}}, inplace=True)
    df.replace({"品名１": {"\（大豆.*\）": ""}}, inplace=True, regex=True)
    df.replace({"品名１": {"\（種類.*\）": ""}}, inplace=True, regex=True)
    df.replace({"品名１": {"大きさ：": ""}}, inplace=True, regex=True)
    df.replace({"品名１": {"（特ア28不使用）": ""}}, inplace=True, regex=True)
    df.replace({"品名２": {"\（大豆.*\）": ""}}, inplace=True, regex=True)
    df.replace({"品名２": {"\（種類.*\）": ""}}, inplace=True, regex=True)
    df.replace({"品名２": {"大きさ：": ""}}, inplace=True, regex=True)
    df.replace({"品名２": {"（特ア28不使用）": ""}}, inplace=True, regex=True)
    df['品名１'] = df['品名１'].str[:25]
    df['品名２'] = df['品名２'].str[:25]
    df2 = df.drop(0)
    df2.to_csv(iDir +"\output.csv", encoding='cp932', quotechar='"', quoting=1, index=False)


if __name__ == "__main__":
    get()
    