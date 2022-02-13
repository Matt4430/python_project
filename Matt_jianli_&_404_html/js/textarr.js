let textArr = [{
    name: 'h2',
    class: 'inten',
    text: '岗位：Python爬虫工程师'
}, {
    name: 'h4',
    class: 'text-title',
    text: '个人信息'
}, {
    name: 'div',
    class: 'base-info',
    children: [{
        name: 'div',
        children: [{
            name: 'div',
            text: '姓名：杨开群'
        }, {
            name: 'div',
            text: '现居：江北区-五里店'
        }, {
            name: 'div',
            text: '学历：专科'
        }
		]
    }, {
        name: 'div',
        children: [{
            name: 'div',
            text: '年龄：25'
        }, {
            name: 'div',
            text: '意向城市：重庆'
        }]
    },{
        name: 'div',
        children: [{
            name: 'div',
            text: '电话：18072567851'
        }, {
            name: 'div',
            text: '邮箱：3458888444@qq.com'
        }]
    }
	]
}, {
    name: 'h4',
    class: 'text-title',
    text: '教育背景'
}, {
    name: 'div',
    class: 'school',
    children: [{
        name: 'span',
        class: 'mr',
        text: '学历：专科'
    }, {
        name: 'span',
        text: '专业：电气自动化技术'
    }, {
        name: 'div',
        text: '主修课程：HTML、CSS、EcmaScript、Python、MySQL',
    }]
}, {
    name: 'h4',
    class: 'text-title',
    text: '专业技能'
}, {
    name: 'ul',
    class: 'ul-list',
    children: [{
        name: 'li',
        text: '熟练掌握',
        children: [{
            name: 'span',
            class: 'tag',
            text: 'H5、CSS3、JS'
        }]
    }, {
        name: 'li',
        text: '掌握前端主流',
        children: [{
            name: 'span',
            class: 'tag',
            text: 'Vue、React框架'
        }]
    }, {
        name: 'li',
        text: '熟练掌握',
        children: [{
            name: 'span',
            class: 'tag',
            text: 'Python数据处理，熟悉tornado、django、web.py等网络开发框架'
        }, {
            name: 'span',
            text: '，熟悉Git、Nexus、Docker、Kubernetes等工具或技术'
        }]
    }, {
        name: 'li',
        text: '熟悉后端语言Java、node.js'
    }, {
        name: 'li',
        text: '熟悉',
        children: [{
            name: 'span',
            class: 'tag',
            text: 'MySQL数据库'
        }, {
            name: 'span',
            text: '熟悉索引工作原理，有丰富的mysql性能优化经验以及高可用、集群实战经验'
        }]
    }]
}, {
    name: 'h4',
    class: 'text-title',
    text: '生涯履历'
}, {
    name: 'div',
    class: 'work',
    children: [{
        name: 'span',
        class: 'mr',
        text: '2014.02 — 2018.06'
    }, {
        name: 'span',
        text: 'web全栈开发'
    }]
}, {
    name: 'ul',
    class: 'ul-list',
    children: [{
        name: 'li',
        text: '从普通开发人员，升任到子非鱼公司Web技术部主管，负责',
        children: [{
            name: 'span',
            class: 'tag',
            text: '带领新人、项目安排、产品优化'
        }, {
            name: 'span',
            text: '，定期组织开展BUG研讨技术会，为公司奠定了技术基础'
        }]
    }, {
        name: 'li',
        text: '负责公司Web项目全周期，后期负责AI类查询项目，参与产品线核心功能的架构设计，技术方案调研工作'
    }]
}, {
    name: 'h4',
    class: 'text-title',
    text: '高级项目'
}, {
    name: 'div',
    class: 'item-lv',
    children: [{
        name: 'ul',
        class: 'ul-list',
        children: [{
            name: 'li',
            class: 'project-title',
            text: '项目一：图书商城（混合APP开发）'
        }, {
            name: 'li',
            text: '使用技术栈：Gap框架、',
            children: [{
                name: 'span',
                class: 'tag',
                text: 'Vue全家桶、 Express/Koa框架'
            }]
        }, {
            name: 'li',
            text: '项目描述：基于vue-cli搭建的web应用，海量商城。功能主要包括商家入驻平台上传个人身份信息、发布图书信息、会员商家一对一聊天、商城买卖、城市筛选。其中包含收货地址、搜索记录、图书和商家店铺收藏的CRUD操作'
        }]
    }, {
        name: 'ul',
        class: 'ul-list',
        children: [{
            name: 'li',
            class: 'project-title',
            text: '项目二：智慧租房'
        }, {
            name: 'li',
            text: '使用技术栈：',
            children: [{
                name: 'span',
                class: 'tag',
                text: 'Vue全家桶、'
            }, {
                name: 'span',
                text: '高德官方'
            }, {
                name: 'span',
                class: 'tag',
                text: 'cube-ui'
            }, {
                name: 'span',
                text: '框架、'
            }, {
                name: 'span',
                class: 'tag',
                text: 'BeautifulSoup多端打包'
            }]
        }, {
            name: 'li',
            text: '项目描述：使用Python脚本爬取某租房网站的房源信息，利用高德的jsAPI在地图上标出房源地点，找到距离工作地点1小时车程的房源。在项目实现的过程中将熟悉requests、BeautifulSoup、csv等库的简单使用'
        }]
    }, {
        name: 'ul',
        class: 'ul-list',
        children: [{
            name: 'li',
            class: 'project-title',
            text: '项目三：基于Flask与MySQL实现番剧推荐系统'
        }, {
            name: 'li',
            text: '使用技术栈：',
            children: [{
                name: 'span',
                class: 'tag',
                text: 'Vue、Vue-Router、Flas、Django'
            }, {
                name: 'span',
                text: '、YDUI、神经网络'
            }]
        }, {
            name: 'li',
            text: '项目描述：因为随着每日数据分析量的加大，对引物设计这种工作变成了工作效率的阻碍，遂提出了设计软件以达到自动化设计的目的。而且引物设计主要费时在于多种验证操作，可以通过软件自动验证减少人力成本，推荐优质内容'
        }]
    }]
}, {
    name: 'h4',
    class: 'text-title',
    text: '自我评价'
}, {
    name: 'ul',
    class: 'ul-list',
    children: [{
        name: 'li',
        text: '具有',
        children: [{
            name: 'span',
            class: 'tag',
            text: '团队管理经验'
        }, {
            name: 'span',
            text: '，拥有良好的'
        }, {
            name: 'span',
            class: 'tag',
            text: '团队协调能力'
        }, {
            name: 'span',
            text: '，与同事配合极其默契'
        }]
    }, {
        name: 'li',
        text: '有很强的',
        children: [{
            name: 'span',
            class: 'tag',
            text: '自学及动手能力'
        }, {
            name: 'span',
            text: '，善于接受新事物，精通'
        }, {
            name: 'span',
            class: 'tag',
            text: '全栈'
        }, {
            name: 'span',
            text: '开发'
        }]
    }, {
        name: 'li',
        text: '性格随和、诚恳稳重、身体素质较好、适应环境能力强'
    }]
}]
let style = `
    /*
    * 面试官您好，我是杨开群
    * 特此准备了一份在线简历
    * 先准备一些样式
    */
    *{
        transition: all .8s;
    }
    /* 容器中要添加点样式 */
    #codeEdit{
        color: #fff;
        background: #1E1E1E;
    }
    #resume{
        box-shadow: -1px 4px 9px 3px rgba(0, 0, 0, .15);
    }
    /* 再来点代码高亮 */
    pre#codeEdit{
        color: #CE9e78;
    }
    .token.selector{
        color: rgb(230, 155, 43);
    }
    .token.comment{
        color: #2eb996;
        font-size: 14px;
    }
    .token.property{
        color: #60C8FE;
    }
    .token.function {
        color: #DD4A68;
    }
    /* 好啦,右边就是我的简历，望查阅指正 */
`
let balloon = `
    <div class="balloon-wrap">
        <img src="img/balloon.png" id="bg-balloon-small">
        <img src="img/balloon.png" id="bg-balloon-large">
        <img src="img/logo.png" id="bg-balloon-logo">
    </div>
    <div class="connect" style="width: 100%; display: flex;"></div>`
let line = `
    <div class="line-wrap">
        <div class="line-left"></div>
        <div class="line-right">
            <p class="line-defColor line-item1"></p>
            <p class="line-darkColor line-item2"></p>
            <p class="line-defColor line-item3"></p>
            <p class="line-midColor line-item4"></p>
            <p class="line-darkColor line-item5"></p>
            <p class="line-midColor line-item6"></p>
            <p class="line-darkColor line-item7"></p>
            <p class="line-midColor line-item7"></p>
        </div>
    </div>
    <div class="connect"></div>`
let text = `
    <div class="text-wrap"></div>
`
