{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 const form = document.querySelector("form");\
\
form.addEventListener("submit", event => \{\
  event.preventDefault();\
\
  const title = form.elements["title"].value;\
  const content = form.elements["content"].value;\
\
  fetch("/blog-posts", \{\
    method: "POST",\
    headers: \{\
      "Content-Type": "application/json"\
    \},\
    body: JSON.stringify(\{\
      title,\
      content\
    \})\
  \})\
    .then(response => response.json())\
    .then(post => \{\
      // Handle the success response\
    \})\
    .catch(error => \{\
      // Handle the error response\
    \});\
\});\
}