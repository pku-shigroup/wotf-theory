% mynotes.cls
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mynotes}[2026/06/11 Simple physics notes class]

% 继承 article 类，默认 11pt, a4paper
\LoadClass[11pt,a4paper]{article}

% 页面边距
\RequirePackage[top=2.5cm, bottom=2.5cm, left=2.5cm, right=2.5cm]{geometry}

% 核心数学包
\RequirePackage{amsmath, amssymb, amsthm, physics}

% 颜色与超链接
\RequirePackage{xcolor}
\RequirePackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}

% 常用自定义命令
\RequirePackage{amsfonts}
\newcommand{\ee}{\mathrm{e}}
\newcommand{\ii}{\mathrm{i}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}

% 页眉
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\nouppercase{\leftmark}}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% 章节标题格式
\RequirePackage{titlesec}
\titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\large\bfseries}{\thesubsection}{1em}{}

\endinput
