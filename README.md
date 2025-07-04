# TronLink 开发者文档

这是 TronLink 钱包的官方开发者文档，提供完整的开发指南和 API 参考。

## 📖 文档内容

- **介绍** - TronLink 和波场生态介绍
- **HD 钱包** - HD 钱包相关文档
- **移动端开发** - 移动端集成指南
  - 资产管理
  - DeepLink 集成
  - DApp 浏览器支持
- **插件钱包** - 浏览器插件开发
  - 主动请求功能
  - 被动消息接收
- **DApp 开发** - 去中心化应用开发
  - 多签转账
  - 消息签名
  - 普通转账
  - Stake2.0

## 🚀 快速开始

### 本地开发

1. 克隆仓库
```bash
git clone https://github.com/fentiaoflutter/tronlink-docs.git
cd tronlink-docs
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动本地服务器
```bash
mkdocs serve
```

4. 访问 http://localhost:8000 查看文档

### 构建文档

```bash
mkdocs build
```

构建后的文件将保存在 `site/` 目录中。

## 📝 贡献指南

我们欢迎社区贡献！请按照以下步骤：

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 🔧 技术栈

- [MkDocs](https://www.mkdocs.org/) - 静态站点生成器
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - 主题
- [GitHub Pages](https://pages.github.com/) - 托管服务
- [GitHub Actions](https://github.com/features/actions) - 自动部署

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🤝 联系我们

- 官方网站：https://www.tronlink.org/
- GitHub Issues：https://github.com/fentiaoflutter/tronlink-docs/issues
- 开发者社区：https://github.com/fentiaoflutter/tronlink-docs/discussions

## 📚 相关链接

- [TronLink 官网](https://www.tronlink.org/)
- [波场 TRON 官网](https://tron.network/)
- [波场开发者中心](https://developers.tron.network/)

*   上线检查点：

    *   -- IRequest 是否是正式接口
    *   -- DappJs 是否是正式JS地址
    *   -- IRequest.HTML_Dapp是否是正确的dapp列表




*   v3.3.1已检查
###################################################
*   v3.3.1
发版日志：
1. 修复多签已知问题，提升稳定性
*   v3.5.0
发版日志：
1. 新增支持尼罗河网络下的 TRONZ 隐私协议，升级之后，您可以通过 TronLink 进行创建匿名地址，查看资产，匿名转账以及查看交易记录等操作。
2. 增加了服务器选择功能，您可手动切换到速度更快的服务器。
3. 支持了尼罗河网和主网间的切换。
4. 调整了资源中带宽和能量的顺序。
5. 优化了部分转账和投票的提示文案。
6. 修复已知问题，提高稳定性。

*   v3.7.0
发版日志：
    1.行情页面优化，增加顶部轮播，自选交易，trx,usdt交易对展示
    2.投票优化：新增批量投票取消页面，超级代表详情页面，批量投票购物车
    3.超级代表列表排序；新增我的投票页面
    4.钱包管理，更新卡片功能和UI
    5.投票首页UI; 收益领取未超过24小时提示。
    6.投票方式细分，单个投票、修改、取消，批量投票，取消全部
    7.超级代表搜索改为在线搜索
    8.列表接口增加分页查询



###################################################
# TronLink-Android：
##  基本说明：
*   开发工具：Android-Studio
*   当前版本：3.7.0
*   开发分支：develop
*   基于TRON 网络的去中心化钱包，通过RPC与TRON整个网络通信，严密的加密措施，保证私钥存储的绝对安全性，通过关闭打开网络来实现冷热钱包的动态切换，保证账户和数据的绝对安全。
##  基础功能：
*   创建钱包
    *   随机seed，Tron的签名算法为ECDSA，选用曲线为SECP256K1。其私钥为一个随机数，公钥为椭圆曲线上一个点。生成过程为，首先生成一个随机数d作为私钥，再计算P=d*G作为公钥；其中G为椭圆曲线的基点，从而创建密钥对
*   导入钱包
    *   可以通过助记词导入
    *   可以通过KeyStore导入
    *   可以通过私钥导入
    *   可以直接通过地址导入，从而观察这个钱包
*   导出钱包
    *   与导入钱包功能相对应：可以导出私钥，助记词，KeyStore
*   功能：
    *   提供查看TRX TRC-10 TRC-20余额展示功能
    *   转账功能：TRX TRC-10 TRC-20
    *   收款功能：TRX TRC-10 TRC-20
    *   提供交易历史记录查询功能
    *   实时计算价格显示，TRX TRC-10 TRC-20
    *   冻结TRX获取能量及波场权，并提供解冻功能
    *   冻结TRX获取带宽及波场权，并提供解冻功能
    *   实时显示剩余带宽，能量，波场权
    *   提供给超级代表投票功能
    *   Dapp嵌入，及提供对应的API接入规范，支持波场大多数DApp完美运行
    *   提供TRC-10,TRC-20项目详情页面，查看项目方发币数量等
    *   链接交易所，实时更新币种的行情
    *   提供中英文切换，人民币与美元的切换
    *   提供节点切换
    *   提供钱包密码修改
    *   提供钱包名称自定义
    *   提供问题帮助和反馈页面
    *   提供加入社群功能
    *   帮助开发者进入开发者模式，进入shasta测试网络进行测试。
    *   行情功能，实时查询最新Token币价
    *   提供usdt收益展示
    *   提供冷钱包功能
    *   提供Dapp测试工具
    *   提供助记词转换工具
    *   委员会提议功能
    *   多重签名功能
    *   匿名账户创建
    *   匿名转账

##  下一个版本
*   开发中
###################################################


# 三种环境如下环境切换

          RELEASE        -- 线上环境
          PRE_RELEASE    -- 预发布环境
          TEST           -- 测试环境

    *  打包时候需要根据需求 切换IRequest 的 ENVIRONMENT 为相应环境：

    例如：
    public static final NET_ENVIRONMENT ENVIRONMENT = NET_ENVIRONMENT.TEST;//测试环境

# 上线需要检查的文件：
    *   -- IRequest 是否是正式接口
    *   -- DappJs 是否是正式JS地址

====================================================================================================


# TronLink 测试包打包流程

    *  切换IRequest 的 ENVIRONMENT 为  TEST 环境
        例如：
        public static final NET_ENVIRONMENT ENVIRONMENT = NET_ENVIRONMENT.TEST;//测试环境

    *   app - build.gradle 修改 渠道包为 tronTest

    *    Build -- Generate Signed apk -- 选择 new_wallet.jks 签名文件 -- 渠道选择 tronTest 打包即可

====================================================================================================

# TronLink 预发布包打包流程

    *  切换IRequest 的 ENVIRONMENT 为  PRE_RELEASE 环境
            例如：
            public static final NET_ENVIRONMENT ENVIRONMENT = NET_ENVIRONMENT.PRE_RELEASE;//预发布环境

    *   app - build.gradle 修改 渠道包为 tronTest

    *    Build -- Generate Signed apk -- 选择 new_wallet.jks 签名文件 -- 渠道选择 tronTest 打包即可

====================================================================================================

# TronLink 线上包打包流程

     *  切换IRequest 的 ENVIRONMENT 为  RELEASE 环境
                例如：
                public static final NET_ENVIRONMENT ENVIRONMENT = NET_ENVIRONMENT.RELEASE;//线上环境

     *   app - build.gradle 修改 渠道包为 official

     *   -- IRequest 是否是正式接口

     *   -- DappJs 是否是正式JS地址

     *    Build -- Generate Signed apk -- 选择 new_wallet.jks 签名文件 -- 渠道选择 tron_official 打包即可


========================================================================================================
TronLink Pro 打包所需修改文件及打包：

    1. app - build.gradle 修改
       (1) 替换包名：applicationId "com.tronlinkpro.wallet"/"com.tronlink.global"
       (2) 注释掉TronLink 的 bugly,打开TronLink Pro 的 bugly
           此为Tronlink Pro 的bugly 账号
          bugly {
            appId = '7b9957a11f' // 注册时分配的App ID
            appKey = '90c13dbd-aafc-47dd-8939-02e88e921e7e' // 注册时分配的App Key
            }
       (3) 替换签名文件，TronLink  签名文件为 new_wallet.jks ,TronLink Pro 签名文件为 wallet_pro.jks
           打包TronLink Pro 包的时候 注释掉 TronLink 签名设置， 打开 TronLink Pro 签名设置

           此为 TronLink Pro 签名设置
               signingConfigs {
                   myConfig {
                       storeFile file('wallet_pro.jks')
                       storePassword 'tron1234'
                       keyAlias 'tronlink'
                       keyPassword 'tron1234'
                   }

                   debug {
                       storeFile file('wallet_pro.jks')
                       storePassword 'tron1234'
                       keyAlias 'tronlink'
                       keyPassword 'tron1234'
                   }
                   global {
                        storeFile file('global_upload.jks')
                        storePassword 'TronLink.@#$Global'
                        keyAlias 'global'
                        keyPassword 'TronLink.@#$Global'
                   }
               }

       (4) 打开 google 渠道设置
               googleplay {
                   manifestPlaceholders = [UMENG_CHANNEL_VALUE: "googleplay", UMENG_APP_KEY: "5dc51a5f570df3c184000b7c"]
                   buildConfigField("boolean", "IS_GOOGLEPLAY", "true")
               }

    2.  AndroidManifest.xml 修改

       (1) 替换应用图标和应用名称

           此为TronLink Pro 应用设置
              android:icon="@mipmap/ic_launcher_pro"
              android:label="@string/app_pro_name"
              android:roundIcon="@mipmap/ic_launcher_round_pro"

       (2) 替换 provider
            此为 TronLink Pro provider 设置
               <provider
                   android:name="android.support.v4.content.FileProvider"
                   android:authorities="com.tronlinkpro.wallet.fileprovider" / "android:authorities="com.tronlink.global.fileprovider"
                   android:exported="false"
                   android:grantUriPermissions="true">
                   <meta-data
                       android:name="android.support.FILE_PROVIDER_PATHS"
                       android:resource="@xml/file_paths_pro" />
               </provider>

               可注释掉 TronLink 的 provider, 打开 TronLink Pro 的 provider


    3.  打包

       检查环境：
            *   -- IRequest 是否是正式接口

            *   -- DappJs 是否是正式JS地址

            *   IRequest 的 ENVIRONMENT 是否为所需环境（线上/预发布/测试）

       以上检查无问题，打包
       Build -- Generate Signed apk -- 选择 wallet_pro.jks 签名文件 -- 渠道选择 googleplay 打包即可

====================================================================================================

# 打渠道包

   当测试人员测试完毕，告知可打渠道包时，android 开发人员 需打两个渠道包：
        （1）TronLink 的 tron_official 的渠道包  （此包名为 com.tronlink.wallet）
        （2）TronLink Pro 的 googleplay 的 渠道包 （此包名为 com.tronlinkpro.wallet）
        （2）TronLink Global 的 googleplay 的 渠道包 （此包名为 com.tronlink.global）

   slack 发送到 测试群（现为 tronlink_android）,等待验证是否有问题

====================================================================================================

##	冷热钱包交互说明：
###	交互过程：
*	观察钱包发起交易，并生成二维码
*	冷钱包扫描二维码，输入密码后，生成签名后的二维码
*	观察钱包再次扫描冷钱包产生的签名后的二维码，并广播
*	交易完成

###	多二维码交互：
*	为减小二维码产生的数量以及最大化利用二维码的存储容量，设置每个二维码最大存储为1000字节。我们只会拆分交易Json 中的hexList字段，把它填充到n个二维码中，且每个二维码的其它字段保证完整性（具体填充见下方字段说明）。

###	冷钱包交易字段说明：
*	type
	*	类型：int
	*	级别：必须
	*	描述：用于标记当前该笔交易的合约类型,需要在最后一个二维码中添加该字段。
	*	详细字段见最后
*	hexList
	*	类型：数组
	*	级别：必须
	*	描述：用于装载多个 TransactionHex
	*	["hex","hex"]
*	address
	*	类型：String
	*	描述：用于标记该笔交易需要签名的钱包地址，需要在第一个及最后一个二维码中添加该字段
*	alpha
	*	类型：String
	*	级别：非必须
	*	描述：用于匿名钱包转账的字段，正常交易无需添加该字段
*	tokenId
	*	类型：String
	*	级别：非必须
	*	描述：用于匿名钱包标记匿名币的tokenId，,需要在最后一个二维码中添加该字段。正常交易无需添加该字段
*	cN
	*	类型：int
	*	级别：必须
	*	描述：用于标记当前二维码的index ,从1开始，每个二维码都需要添加该字段
*	tN
	*	类型：int
	*	级别：必须
	*	描述：用于标记该笔交易共产生几个二维码，每个二维码都需要添加该字段



```
	//多重签名的转账from other
     int TRANSFER_OTHER_TYPE = 6;
    //多重签名的转账from  my
     int TRANSFER_MY_TYPE = 7;
     int FREEZE_TYPE = 4;
     int DEPOSIT_TYPE = 8;
     int WITHDRAW_TYPE = 9;
     int TRANSFER_TYPE = 1;
     int UPDATE_TYPE = 5;
     int UNFREEZE_TYPE = 2;
     int VOTE_TYPE = 3;
     int VOTE_INCOME_TYPE = 10;
     int MAKEPROPOSAL_TYPE = 11;
     int APPROVALSPROPOSAL_TYPE = 12;
     int PARTICIPATEMULTISIGN_TYPE = 13;


{
	"address": "TGjdouJUAuCLbtf8dJtDHuQGfhuPfWcuGo",
	"hexList": ["0a85010a02385d2208b3e91e60471fbf0640c08fcea7922e5a67080112630a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412320a15414a37c3f16f61604bd1bd7d8f7438ceafda23626d121541ceedd7eade5222c95d478d2952deb0b971344cd21880897a70e7c9caa7922e"],
	"type": 1,
	"cN": 1,
	"tN": 1,
	"tokenId":"12345"
}

```








  
    

 





