﻿/* Chinese initialisation for the jQuery UI date picker plugin. */
/* Written by Ressol (ressol@gmail.com). */
(function($) {
	$.datepick.regional['zh-TW'] = {
		clearText: '清除', clearStatus: '清除已選日期',
		closeText: '關閉', closeStatus: '不改變目前的選擇',
		prevText: '&#x3c;上個月', prevStatus: '顯示上個月',
		prevBigText: '&#x3c;&#x3c;', prevBigStatus: '顯示上一年',
		nextText: '下個月&#x3e;', nextStatus: '顯示下個月',
		nextBigText: '&#x3e;&#x3e;', nextBigStatus: '顯示下一年',
		currentText: '今天', currentStatus: '顯示本月',
		monthNames: ['一月','二月','三月','四月','五月','六月',
		'七月','八月','九月','十月','十一月','十二月'],
		monthNamesShort: ['一','二','三','四','五','六',
		'七','八','九','十','十一','十二'],
		monthStatus: '選擇月份', yearStatus: '選擇年份',
		weekHeader: '周', weekStatus: '年內周次',
		dayNames: ['星期日','星期一','星期二','星期三','星期四','星期五','星期六'],
		dayNamesShort: ['周日','周一','周二','周三','周四','周五','周六'],
		dayNamesMin: ['日','一','二','三','四','五','六'],
		dayStatus: '設定 DD 為一周起始', dateStatus: '您選擇了 m月 d日, DD',
		dateFormat: 'yy/mm/dd', firstDay: 1,
		initStatus: '請選擇日期', isRTL: false,
		showMonthAfterYear: false, yearSuffix: ''};
	$.datepick.setDefaults($.datepick.regional['zh-TW']);
})(jQuery);
