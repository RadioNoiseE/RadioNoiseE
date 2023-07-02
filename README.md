```TeX
\let\+\let\+\a\advance\+\c\catcode\+\d\def\+\f\fam\+\m\mag\+\u\uccode \m
13\c\m9\+\p\uppercase\d\i{\a\f7 \ifnum\f>125 \a\f-93 \fi}\d~{\u\f\m \c\m
12 \a\m1 \i \ifnum\m>125 \+~\1\fi~}\d\0#1{\ifnum`#1>"D \if#1 !\else "\fi
\else\string~\fi}\u`9"20\p{\d\1#19}{\newlinechar13\d\3{\immediate\write1
6}\+~\0\p{\3{}\3{#1}\batchmode\end}}\f"55\u\f\m\i\m32\u\f\m\c\m12\i\m35~
:J\]|Bn\OsDBnE\D-DSE\8DY|IyI|e`:UTJ\F`bOE\k|eP8E\MB|+kU{J\[Ak{\V%L3*Uq\l
u`\@!F`bNKII-E\lu`\k|ll4`\?Ru`;`^SUq\d2I{B|~\ 8E\MB|+kU{J\[Ak{\V%L3*Uq\l
```

## R.N.E？
RadioNoiseE，启发来源于『某魔法的禁书目录』。<br/>
初三，马上就高一。这不中考刚考完（2023·6·19）。<br/>
语文一直不太好，对组版有超扭曲的执着。<br/>
青春期（aka，思春期☆）。<br/>
觉得在C里用`goto`有点宏语言的感觉，（自然）喜欢也滥用宏。<br/>
因为在看『The Little Schemer』，导致最近特别喜欢用尾递归。<br/>
喜欢TeX丧心病狂的宏展开（当然仅限于某些特定时候）；仰视NFSS的魔鬼尾递归瑟瑟发抖。<br/>
只用mpv听歌，用curl／aria2c荡东西。<br/>
有时候（iPad没有计算器）会把Lua的独立解释器当计算器用。

## 言语支持
- TeX　［plain-TeX、LaTeX3］
- C-Class　［C、C艹、Swift］　（Swift是附带的，没太大开发iOS应用的动力）
- Lua　（相信我真的不是因为游戏，而是，LuaTeX）
- JavaScript　（为什么不归在C那类啊，哦，DOM啊）
- Scheme　（这个吧，还在学：『The Little Schemer』阅读中）

![言語支持](https://github-readme-stats.vercel.app/api/top-langs/?username=RadioNoiseE&layout=compact)

## 番剧支持
〈EVA神教〉<br/>
『彻夜之歌』后，在看『放课后失眠的你』。<br/>
### 刚看完：
- 『TARI，TARI』『孤独摇滚』『紫罗兰的秘密花园・あい与自动手记人偶』
### 在看：
- 『学园孤岛』『真实之泪』『花开物语』『真物究竟是什么・终』

## 项目
- Eva-JFM　致敬EVA！「进阶」的字体矩阵　〔LuaTeX〕
- Nian-Class　年文档类！基于expl3的完全可定制、支持中日文组版的文档类　〔LuaTeX〕　［未完成］
- JSTML　用来写同学录的简易标记语言　〔C、TeX、Lua〕
- Aria2Curl　将Aria2c输入文件转换为Curl输入文件　〔C〕　［还有部分Option未适配、或是Curl根本就不支持那个特性］

## 计画
- ~~Jing Structured Markup Language　用来写同学录的标记语言　〔TeX、C、Lua、XML〕~~
- ~~Aria2Curl　把给Aria2c用的输入文件扔给Curl用的　〔C／C艹〕~~
- DocStrip Comp　自定义的文式程序设计用辅助　〔C、TeX〕
- Bilibili BangDown　扫荡小破站上的番剧　〔JavaScript、Lua、Curl〕
- Aria2Curl　让curl支持aria2c格式的输入文件　〔C〕
- Qi CJK　「うけい」中日文LuaTeX支持宏集（感觉LuaTeX-ja还是有点重）　〔TeX、Lua〕
- MetaFBd　基于MetaPost的造字系统　〔C、MetaPost…〕
- JSTML-ng　真正可用的自定义结构化标记语言（目前的想法是给TeX封装一个类Lisp的语法？）　〔C、TeX…〕

## `\expandafter`⁇
```TeX
\def\colon{:}\def\arrow{->}
\let\isx\message
\def\setup{%
    \def\notilde{}%
    \def\encodeone{%
        \catcode\fam\active\lccode126\fam\lccode 48\mag
        \lowercase{\edef~{\notilde 0}%
                   \isx{[\string~\colon \notilde 0\space\number\fam\arrow\number\mag]}%
        }%
        \advance\mag7 \ifnum\mag>125\advance\mag-93 \fi
        \advance\fam1
    }%
    \def\do{\encodeone \csname do\ifnum\fam>125 stop\fi\endcsname
    }%
    \fam13 \encodeone
    \fam32 \encodeone
    \fam35 \let\dostop\relax \do
    \edef\notilde{\string ~}
    \encodeone \fam33 \encodeone \encodeone
}
\def\outwrite{\immediate\write15{\outline}%
    \expandafter\ifx\csname 73\endcsname\relax
                \else
                    \expandafter\let\expandafter\1\csname 73\endcsname
                    \expandafter\let\csname 73\endcsname\relax
                    \charnum 1
                \fi
    \checkeof}
\begingroup
\let\0\catcode \0`\0 11 \0`\2 11 \0`\3 11 \0`\4 11 \0`\5 11
               \0`\6 11 \0`\7 11 \0`\8 11 \0`\9 11 \0`\1 11
\gdef\outline{\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26
              \27\28\29\30\31\32\33\34\35\36\37\38\39\40\41\42\43\44\45\46\47\48\49
              \50\51\52\53\54\55\56\57\58\59\60\61\62\63\64\65\66\67\68\69\70\71\72}
\endgroup
\newcount\charnum
\def\checkeof{\futurelet\next\encodemore}
\def\tildecheck#1#2{\if \string~#1%
    \expandafter\def\csname\number\charnum\endcsname{#1}%
    \advance\charnum 1
    \expandafter\def\csname\number\charnum\endcsname{#2}%
\fi}
\def\encodemore{%
    \ifx\next\EOF
        \let\next\outwrite \let\checkeof\relax
        \global\tracingcommands2\global\tracingmacros2\global\tracingonline0
               \ifnum\charnum<72
                     \expandafter\def\csname\number\charnum\endcsname{ }%
               \else
                     \def\1{ }%
               \fi
    \else
        \advance\charnum 1
        \ifnum\charnum>72
              \charnum 0 \let\next\outwrite
        \else
              \let\next\getnextchar
        \fi
    \fi
    \next}
\def\getnextchar#1{%
    \edef\0{#1}%
    \expandafter\let\csname\number\charnum\endcsname\0\relax
    \expandafter\tildecheck\0\relax\relax
    \checkeof}%
\def\EOF{\relax\relax}
\def\writefile#1{\expandafter\checkeof\input#1 \EOF}%
\begingroup
\def\0#1XXX#2^^JZZZ^^J{\endgroup
    \def\writepreamble##1{\begingroup
        \newlinechar=10 \chardef\0=##1\def\1####1"{"}%
        \immediate\write15{#1\expandafter\1\meaning\0#2}\endgroup}}%
\catcode`\{=12 \catcode`\}=12 \catcode`\#=12
\catcode`\~=12 \catcode`\@=12 \catcode`\$=12
\catcode`\^=12 \catcode`\&=12 \catcode`\_=12 \catcode`\|=12
\catcode`\%=12 \endlinechar=10 \afterassignment\0 \catcode`\\=12
\let\+\let\+\a\advance\+\c\catcode\+\d\def\+\f\fam\+\m\mag\+\u\uccode \m
13\c\m9\+\p\uppercase\d\i{\a\f7 \ifnum\f>125 \a\f-93 \fi}\d~{\u\f\m \c\m
12 \a\m1 \i \ifnum\m>125 \+~\1\fi~}\d\0#1{\ifnum`#1>"D \if#1 !\else "\fi
\else\string~\fi}\u`9"20\p{\d\1#19}{\newlinechar13\d\3{\immediate\write1
6}\+~\0\p{\3{}\3{#1}\batchmode\end}}\fXXX\u\f\m\i\m32\u\f\m\c\m12\i\m35~
ZZZ
\def\encodefile#1{%
    \immediate\openout15=encode.out \relax
    \begingroup
    \fam\time \mag\time \divide\fam93 \multiply\fam 93 \advance\mag-\fam
    \advance\mag 33
    \message{======= Code shift: time \number\time\space -->
             mag \number\mag\space ============================}%
    \writepreamble{\number\mag}%
    \setup \charnum=0
    \immediate\write16{(==>./encode.out)}%
    \writefile{#1}%
    \endgroup
    \immediate\closeout15 \relax
    \immediate\write16{(*./encode.out)}%
}
\immediate\write16{> Encode:}
{\catcode\endlinechar=9 \global\read-1 to\filnam}
\encodefile{\filnam}
\end
```
