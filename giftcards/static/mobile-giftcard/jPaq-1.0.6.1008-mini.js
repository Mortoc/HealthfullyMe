/*
 jPaq - A fully customizable JavaScript/JScript library
 http://jpaq.org/

 Copyright (c) 2011 Christopher West
 Licensed under the MIT license.
 http://jpaq.org/license/

 Version: 1.0.6.1008
 Revised: April 6, 2011
*/
(function(){function i(a,e){a._=function(a){if(h===a)return e}}var h={};jPaq={toString:function(){return"jPaq - A fully customizable JavaScript/JScript library created by Christopher West."}};(Color=function(){i(this,{r:0,g:0,b:0});this.setTo.apply(this,arguments)}).prototype={setTo:function(a,e,c){if(arguments.length==1){var d=/^#?(([\dA-F]{3}){1,2})$/i.exec(a+"");d?(d=d[1],d.length==3&&(d=d.replace(/(.)/g,"$1$1")),this.r(parseInt(d.substring(0,2),16)).g(parseInt(d.substring(2,4),16)).b(parseInt(d.substring(4,
6),16))):(d=/^rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/i.exec(a+""))?this.r(d[1]).g(d[2]).b(d[3]):this.r(a)}else this.r(a).g(e).b(c);return this},getHexCode:function(){return"#"+[this.r().toString(16),this.g().toString(16),this.b().toString(16)].join(",").replace(/\b(\w)\b/gi,"0$1").toUpperCase().replace(/,/g,"")},combine:function(a,e){if(isNaN(e=+e))e=50;var c=Math.max(Math.min(e,100),0)/100,d=1-c;return new Color(this.r()*d+a.r()*c,this.g()*d+a.g()*c,this.b()*d+a.b()*c)},getSafeColor:function(){var a=
this.getLuminance()<128?255:0;return new Color(a,a,a)},getLuminance:function(){with(this)return 0.299*r()+0.587*g()+0.114*b()},toGrayscale:function(){var a=Math.round(this.getLuminance());return new Color(a,a,a)},getOpposite:function(){with(this)return new Color(255-r(),255-g(),255-b())},getLighter:function(a){return this.combine(j,a!=null?a>>>0:30)},getDarker:function(a){return this.combine(k,a!=null?a>>>0:30)}};for(var l=["r","g","b"],f=0;f<3;f++)(function(a){Color.prototype[a]=function(e){var c=
this._(h);if(!arguments.length)return c[a];c[a]=Math.min(Math.max(e>>>0,0),255);return this}})(l[f]);var k=new Color,j=new Color(255,255,255);Color.prototype.toString=Color.prototype.getHexCode;Color.random=function(a,e,c){for(var a=[[a||0,0],[e||0,1],[c||0,2]].sort(function(a,c){return a[0]<=c[0]?a[0]<c[0]?-1:0:1}),e=[],d,f,c=0;c<3;c++)if(a[c][0]instanceof Array)e[a[c][1]]=a[c][0].length==1?a[c][0][0]:Math.randomIn.apply(null,a[c][0]);else{if(a[c][0]!=d||d==0)f=Math.round(Math.randomIn(d>0?f:0,255));
d=a[c][0];e[a[c][1]]=f}return new Color(e[0],e[1],e[2])};Math.randomIn=function(a,e){a=a==null?0:a;return Math.random()*((e==null?1:e)-a)+a}})();
