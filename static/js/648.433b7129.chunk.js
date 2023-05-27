"use strict";(self.webpackChunkfrontend=self.webpackChunkfrontend||[]).push([[648],{6648:function(e,s,n){n.r(s),n.d(s,{default:function(){return j}});var t=n(9439),c=n(2791),i=n(1392),r=n(4925),l=["title","titleId"];var a=c.forwardRef((function(e,s){var n=e.title,t=e.titleId,i=(0,r.Z)(e,l);return c.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true",ref:s,"aria-labelledby":t},i),n?c.createElement("title",{id:t},n):null,c.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M22 10.5h-6m-2.25-4.125a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zM4 19.235v-.11a6.375 6.375 0 0112.75 0v.109A12.318 12.318 0 0110.374 21c-2.331 0-4.512-.645-6.374-1.766z"}))})),d=n(474),o=n(1402),h=n(7689),u=n(6718),x=n(9085),f=n(184);var j=function(){var e=(0,i.zQ)(),s=(0,h.s0)(),n=(0,i.I1)(),c=(0,t.Z)(n,1)[0],r=(0,i.kD)(),l=(0,t.Z)(r,1)[0],j=(0,i.wi)(),m=function(e){c(e).unwrap().then((function(e){b("Successfully Deleted the user")})).catch((function(e){console.error(e),v("Error  when Deleteing the user")}))},b=function(e){return(0,x.Am)(e,{type:"success"})},v=function(e){return(0,x.Am)(e,{type:"error"})},w=function(e,s){l({id:e,is_active:s}).unwrap().then((function(e){b("Successfully changed is active for the user")})).catch((function(e){console.error(e),v("Error  when changeing is active for the user")}))};if(e.isSuccess&&j.isSuccess){var N=e.data.filter((function(e){return"STUDENT"===e.type})).map((function(e,n){var t=j.data.filter((function(s){return s.user==e.id}))[0];return(0,f.jsxs)("tr",{children:[(0,f.jsx)("th",{children:n}),(0,f.jsxs)("td",{children:[e.first_name," ",e.last_name]}),(0,f.jsx)("td",{children:e.email}),(0,f.jsx)("td",{children:null!==t&&void 0!==t&&t.is_group_leader?"Leader":""}),(0,f.jsx)("td",{children:e.is_active?(0,f.jsx)(u.Z,{color:"green",width:32}):(0,f.jsx)(u.Z,{color:"red",width:32})}),(0,f.jsx)("td",{children:(0,f.jsxs)("div",{className:"btn-group",children:[(0,f.jsx)("button",{title:"Delete Student",className:"btn btn-error ",onClick:function(){m(e.id)},children:(0,f.jsx)(a,{className:"h-6 w-6"})}),(0,f.jsx)("button",{title:"Edit Student Info",className:"btn btn-info ",onClick:function(){s("/app/students/edit/".concat(e.id))},children:(0,f.jsx)(o.Z,{className:"h-6 w-6"})}),(0,f.jsx)("button",{title:"Confirm/uncofirm account",onClick:function(){w(e.id,!e.is_active)},className:"btn btn-warning ",children:(0,f.jsx)(u.Z,{className:"h-6 w-6"})})]})})]},n)})),p=e.data.filter((function(e){return"SUPERVISOR"===e.type})).map((function(e,n){return(0,f.jsxs)("tr",{children:[(0,f.jsx)("th",{children:n}),(0,f.jsxs)("td",{children:[e.first_name," ",e.last_name]}),(0,f.jsx)("td",{children:e.email}),(0,f.jsx)("td",{children:e.is_active?(0,f.jsx)(u.Z,{color:"green",width:32}):(0,f.jsx)(u.Z,{color:"red",width:32})}),(0,f.jsx)("td",{children:(0,f.jsxs)("div",{className:"btn-group",children:[(0,f.jsx)("button",{title:"Delete Supervisor",className:"btn btn-error ",onClick:function(){m(e.id)},children:(0,f.jsx)(a,{className:"h-6 w-6"})}),(0,f.jsx)("button",{title:"Edit Supervisor Info",onClick:function(){s("/app/supervisors/edit/".concat(e.id))},className:"btn btn-info ",children:(0,f.jsx)(o.Z,{className:"h-6 w-6"})}),(0,f.jsx)("button",{title:"Confirm/uncofirm account",onClick:function(){w(e.id,!e.is_active)},className:"btn btn-warning ",children:(0,f.jsx)(u.Z,{className:"h-6 w-6"})})]})})]},n)}));return(0,f.jsxs)("div",{className:"w-full p-4 h-full bg-base-200 overflow-y-scroll",children:[(0,f.jsxs)("div",{className:"flex flex-col m-4 ",children:[(0,f.jsx)("div",{className:"card bg-base-100 shadow-xl mb-4",children:(0,f.jsxs)("div",{className:"card-body items-center flex flex-row",children:[(0,f.jsx)("h1",{className:"font-semibold ",onClick:function(){return b("Hello")},children:"Students"}),(0,f.jsx)("button",{onClick:function(){console.log("add student click"),s("/app/students/add")},className:"btn btn-success btn-circle",children:(0,f.jsx)(d.Z,{className:"h-6 w-6"})})]})}),(0,f.jsx)("div",{className:"card bg-base-100 shadow-xl",children:(0,f.jsx)("div",{className:"card-body",children:(0,f.jsxs)("table",{className:"table w-full",children:[(0,f.jsx)("thead",{children:(0,f.jsxs)("tr",{children:[(0,f.jsx)("th",{}),(0,f.jsx)("th",{children:"ful name"}),(0,f.jsx)("th",{children:"email"}),(0,f.jsx)("th",{children:"Groupe Leader"}),(0,f.jsx)("th",{children:"Active"}),(0,f.jsx)("th",{children:"Actions"})]})}),(0,f.jsx)("tbody",{children:N})]})})})]}),(0,f.jsxs)("div",{className:"flex flex-col m-4 ",children:[(0,f.jsx)("div",{className:"card bg-base-100 shadow-xl mb-4",children:(0,f.jsxs)("div",{className:"card-body items-center flex flex-row",children:[(0,f.jsx)("h1",{className:"font-semibold ",children:"Supervisor"}),(0,f.jsx)("button",{onClick:function(){console.log("add supervisor click"),s("/app/supervisors/add")},className:"btn btn-success btn-circle",children:(0,f.jsx)(d.Z,{className:"h-6 w-6"})})]})}),(0,f.jsx)("div",{className:"card bg-base-100 shadow-xl",children:(0,f.jsx)("div",{className:"card-body",children:(0,f.jsxs)("table",{className:"table w-full",children:[(0,f.jsx)("thead",{children:(0,f.jsxs)("tr",{children:[(0,f.jsx)("th",{}),(0,f.jsx)("th",{children:"ful name"}),(0,f.jsx)("th",{children:"email"}),(0,f.jsx)("th",{children:"Active"}),(0,f.jsx)("th",{children:"Actions"})]})}),(0,f.jsx)("tbody",{children:p})]})})})]})]})}}}}]);
//# sourceMappingURL=648.433b7129.chunk.js.map