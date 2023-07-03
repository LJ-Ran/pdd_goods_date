import start

if __name__ == '__main__':
    """
    简要说明！！！！
    
    @:param access_token   此参数必须设置 请求的接口钥匙
    @:param number: 进行检索的数量, 阈值 10000
    @:param search_param 需要进行搜索的内容条件， 必填
    @:param anti_content 必须填写 请求参数密钥
    @:param get_type 需要查询的类型 1 搜索 2 分类
    @:param verify_auth_token 接口校验的参数
    @:param file_path 文件保存的位置记得
    @:param pdd_uid 拼多多用户ID 打开f12 随便一个接口就可以找到
    @:param class_number 分类的时候这个是必须填写的 这个在分类的接口中抽取出来就行了
    """
    # ====================================
    start = start.Start(access_token="FEO7GYWUU4QR5ZRQOQBQGIIK64ETX4W3RELWIWC7A24Z5EGVQ6HQ113701d",
                        number=100,
                        search_param="感冒药",
                        anti_content="0apWfqzFdioyy9ex1Q5dP5l9DM5hVMjvS6hboRvI48cpDaLOvnpbMe3EkqHub1i3Y16smnwnpgZfnDQE_FwgxvdpfJb4KYa9zZkDDGGSEALCOtYonorJ5IEpMhrLitEHq1ortRKEBrNHK4THiiA7eoq_n1OiIZDdu7Pfzw14PRSATx4GfsPIY-l5B_SsnA4UBCG_GmfXOk3ZU-fDEjBp_3lugdFGODpU2LPdBP8HcOM_ghlzH9uDbMjC85oMSgA-mblToJD7iqihlJuwsKlBpHvXAowA95lZNUw0nJ7XnhK77Da89ot3ftTpuBGCQJSoB5f-qxfpszEPlZOFeZxG7Dd6W2qp_lamw4t4yG9PgeLlHC9C1e-Ag26_yx7AAzvz9lO6UzrX7NmfBxGwelBvrgs05D3pBSzcZpKDGkhGwUDKgcQpn3hjZDmeWeuuYyR0oERTPpiQmCxXBILYLlSXpCKILA25aLxDP_om1Ki58A8F7dZG_WbpJvUywy6imo17uGBguxNNYJNJyRuJYgj07FMjBIjLbcAJ0heIFRjVEcqWgUwP6rpzI6mJKtHiwt-qtGHbACcLkC6nCBNcch_ZWcLIWifSyoTAjGJwxH4X3UVUcNVE007ic5K4Tq9uAtSx6sgyTFXCuT9ix9Fnpat",
                        get_type=1,
                        verify_auth_token='ea43sLu7XEcTVF609o2LDg7ae35239f7aad258a',
                        file_path="/Users/sixuncle/Desktop/test/",
                        pdd_uid=7441470422896,
                        class_number=9701,
                        )
    # =====================================
    start.start()

"""
异常说明：
KeyError: 'items' =》》》 请到浏览器中刷新一下重新去获得一次 verifyauthtoken 这个参数的值

"""
