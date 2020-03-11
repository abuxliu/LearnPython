
// formData
// 将表单内的所有表单项，根据name形成js Object
var data = jqu.formData('ff');

// formItem
// 根据name获得表单项，进行jquery操作
var code = jqu.formItem('code','ff')
code.val('123456');

// formVal
// 获得表单项的值，字符型
var str = jqu.formVal('code','ff');
alert(str);

// formInt
// 将字符型的值转为整数类型
var num = jqu.formInt('code','ff');
alert(num);

// formLoad
// 将js object 整体加载到表单项中
var obj = {
	'code':'123456',
	'name':'张三'
};
jqu.formLoad('ff',obj);

// obj2json
// 将js object 转成字符型，一般查看内容
var obj = {
	'code':'123456',
	'name':'张三'
};
alert(jqu.obj2json(obj))

// hasAttr
// 判断是否有某个属性
var code = jqu.formItem('code','ff');
alert(jqu.hasAttr(code,'id'));

// inArray
// 判断值是否在数组中
var array = ['香蕉','苹果','哈密瓜'];
alert(jqu.inArray('西瓜',array));

// loadHtml
// 将局部html的内容获取过来，可以放入到某个div中
jqu.loadHtml('html_part1.html',function(result){
	// result 就已经是html字符串了
	$('#div1').append(result);
});

// loadJson
// 获得服务端的json格式数据
jqu.loadJson('/admin/list.do',{'keyword':'张'},function(result){
	// result 是js 的object
	alert(jqu.obj2json(result));
});

// loadJs
// 加载脚本，替代 <script> 方式
jqu.loadJs('/js/j1.js');
jqu.loadJs(['/js/j2.js','/js/j3.js']);



