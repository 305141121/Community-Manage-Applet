// pages/userInfo/userInfo.js
Page({
  data: {
    genderArray:['男','女'],
    gender:0,
    collegeArray: [
      {
        id: 1,
        name: '材料学院'
      },
      {
        id: 2,
        name: '传播学院'
      },
      {
        id: 3,
        name: '创业学院'
      },
      {
        id: 4,
        name: '电子科学与技术学院'
      },
      {
        id: 5,
        name: '法学院'
      },
      {
        id: 6,
        name: '高等研究院'
      },
      {
        id: 7,
        name: '高尔夫学院'
      },
      {
        id: 8,
        name: '管理学院'
      },
      {
        id: 9,
        name: '光电工程学院'
      },
      {
        id: 10,
        name: '国际交流学院'
      },
      {
        id: 11,
        name: '化学与环境工程学院'
      },
      {
        id: 12,
        name: '机电与控制工程学院'
      },
      {
        id: 13,
        name: '计算机与软件学院'
      },
      {
        id: 14,
        name: '继续教育学院'
      },
      {
        id: 15,
        name: '建筑与城市规划学院'
      },
      {
        id: 16,
        name: '金钟音乐学院'
      },
      {
        id: 17,
        name: '经济学院'
      },
      {
        id: 18,
        name: '马克思主义学院'
      },
      {
        id: 19,
        name: '南特商学院'
      },
      {
        id: 20,
        name: '人文学院'
      },
      {
        id: 21,
        name: '生命与海洋科学学院'
      },
      {
        id: 22,
        name: '师范学院'
      },
      {
        id: 23,
        name: '数学与统计学院'
      },
      {
        id: 24,
        name: '体育部'
      },
      {
        id: 25,
        name: '土木工程学院'
      },
      {
        id: 26,
        name: '外国语学院'
      },
      {
        id: 27,
        name: '物理与能源学院'
      },
      {
        id: 28,
        name: '心理与社会学院'
      },
      {
        id: 29,
        name: '信息工程学院'
      },
      {
        id: 30,
        name: '研究生院'
      },
      {
        id: 31,
        name: '医学部'
      },
      {
        id: 32,
        name: '艺术设计学院'
      }
    ],
    collegeID: 0,
    gradeArray:[{
        id: 2015,
        name: '2015届'
      },
      {
        id: 2016,
        name: '2016届'
      },
      {
        id: 2017,
        name: '2017届'
      },
      {
        id: 2018,
        name: '2018届'
      }
     ],
    gradeID: 0,
  },

  /**
  * 生命周期函数--监听页面加载
   */
  usernameInput: function (e) {
    console.log('我的姓名是', e.detail.value)
    this.setData({
      username: e.detail.value
    })
  },
  genderBindChange: function (e) {
    console.log('我的性别是', e.detail.value)
    this.setData({
      gender: e.detail.value
    })
  },
  collegeBindChange: function (e) {
    console.log('我的学院是', e.detail.value)
    this.setData({
      collegeID: e.detail.value
    })
  },
  gradeBindChange: function (e) {
    console.log('我的年级是', e.detail.value)
    this.setData({
      gradeID: e.detail.value
    })
  },
  phoneInput: function (e) {
    console.log('我的手机号是', e.detail.value)
    this.setData({
      phone: e.detail.value
    })
  },

  /**
   * 页面的初始数据
   */

formSubmit: function(e){
  var that = this;
  console.log('出现啊', e.detail.value.gradeID, 'ddd', e.detail.value.username),
  wx.request({
    url: 'http://172.29.25.121:8000/test/updateUserInfo/',
    data: {
      token: wx.getStorageSync("token"),
      name: e.detail.value.username,
      sex: e.detail.value.usergender,
      grade: e.detail.value.gradepicker,
      major: e.detail.value.collegepicker,
      phone: e.detail.value.phone,
    },
    header: {
      'content-type': 'application/json'
    },
    method: 'POST',
    dataType: 'json',
    responseType: 'text',
    success: function(res) {},
    fail: function(res) {},
    complete: function(res) {
    console.log('aaaaaaaasuccess')
    },
  })
},


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})