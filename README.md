### 项目结构

| 目录       | 描述                               |
| ---------- | ---------------------------------- |
| libs       | 存放一些自定义的公共类库           |
| ProductApi | 主要用于业务接口调用的实现         |
| ProductWeb | 主要用于 web 自动化逻辑的实现      |
| settings   | 包含各业务的配置信息和测试固化数据 |
| test_cases | 各业务的用例                       |

- libs：
    - models 存放数据库表 ORM 模型类
        - StoreWeb.py 业务 ORM 模型文件
    - Database.py 公共方法类, 供所有业务调用
    - ...
    
- ProductApi：
    - StoreWeb 业务线目录
        - api.py 业务接口实现（若接口较多，api 可拆分多个类）
        - config.py 业务接口配置，如 url, 密钥等，实现 Test/Uat/Production 类
    - ...

- ProductWeb：
    - 保留目录，web 自动化相关

- settings：
    - BaseConfig.py 比较基础的、多个业务线可共用的、不用区分环境的配置
    - TestData.py 固化的默认数据(如常用的账号，接口的默认参数等)，供测试临时使用, 测试用例数据不要放这
    - ...

- test_cases:
    - store_web 业务线目录， 明明方式遵循 PEP8， 与 ProductApi 业务线目录区分
        - data 测试用例数据，为了保持用例整洁，参数化数据可以放这个目录下
        - test_v1_store_products 接口测试用例，原则上一个接口一个用例文件，命名取 path 中部分
    - ...
    
### 约定
1. 公共库类使用大驼峰法命名，用例一律使用小写+下划线
2. 所有类型中按业务划分，当某个业务只包含单个 py 文件时可以写，包含多个文件时，需创建一个包
3. 用例编写 按环境、级别区分，当前运行环境由环境变量 `env` 决定
4. 用例编写框架统一用 `pytest`，原因统计、执行灵活性更大
5. `ProductApi`   `ProductWeb` 只用于逻辑的实现，测试代码一律不要写在此处


### 分支
项目分 `master` 和 `develop` 分支，平时我们在 `develop` 编写、修改自己的脚本，
当一个需求发版，且测试用例稳定后再合并到 `master` 分支，作为常规用例维护


### 随手记生意场景业务线（新增注意维护）

- 零售 | Store
- 零售web | StoreWeb | store_web



### 域名：
（1）生意账本域名：

    测试环境：bizbook.feidee.cn
    生产环境：bizbook.feidee.net
    
（2）收单模块域名：

    测试环境：acquiring.test.sui.internal
    生产环境：acquiring.produce.sui.internal

（3）对外收款设备API域名：

    测试环境：bizapi.feidee.cn
    生产环境：bizapi.feidee.com

















