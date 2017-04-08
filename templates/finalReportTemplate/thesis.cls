
%---------------------------------------------------------------
% thesis class for writing a PhD thesis  by Mohammed Ahmed (mnourgwad@gmail.com), 2014
% Based on the thesis document from Philipp A. Baer (philipp.baer@dfki.de), 2008
%---------------------------------------------------------------


%-------------------------- identification ---------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesis}[2010/07/23 v1 PhD thesis class]

%-------------------------- PhD Thesis is build on Koma script book
\DeclareOption{a4paper}{\PassOptionsToClass{\CurrentOption}{scrbook}}
\DeclareOption{11pt}{\PassOptionsToClass{\CurrentOption}{scrbook}}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{scrbook}}
\ProcessOptions\relax
\LoadClass{scrbook}
%:-------------------------- packages for fancy things -----------------------
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{fancyhdr}
\pagestyle{fancy}
\setcounter{secnumdepth}{3}
\setlength{\parskip}{\medskipamount}
\setlength{\parindent}{0pt}
\usepackage{xcolor}
\usepackage{pdfcolmk}
\usepackage[ngerman,british]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathptmx}
\usepackage{array}

\usepackage{bibentry}
\nobibliography*

\usepackage{graphicx}
%\usepackage{algpseudocode}
%\usepackage{algorithm}
\usepackage[linesnumbered,ruled,vlined]{algorithm2e}
\usepackage{lmodern, charter}
\usepackage{textcomp}
\usepackage[charter]{mathdesign}
\usepackage{footmisc}
\usepackage{booktabs}
\usepackage{listings}
\usepackage{varioref}%
\usepackage{microtype}
\usepackage{pifont}
\usepackage{calc}
\usepackage{ellipsis}
\usepackage{multirow}
\usepackage[pagebackref,
  %bookmarks         = false,
  bookmarksopen      = false,
  bookmarksnumbered  = true,
  %pdftex,pdfhighlight= /N,
  %hypertexnames     = true,
  unicode            = true,
  breaklinks         = true,
  %pdffitwindow      = true,
  %pdfstartview      = {FitV},
  pdfstartview       = Fit, %to show the whole page; FitH, to fit the width of the page in the window; or FitB, to fit the width of the contents to the window.
  linktoc            = all, %none,section,page,all : defines which part of an entry in the table of contents is made into a link
  %linkcolor         = blue!60!black,
  %urlcolor          = blue!60!black,
  %colorlinks        = true,
  %citecolor         = green!25!black,
  %pdfborder          = {0 0 0},
  pdftitle           = {An Intelligent Architecture for Legged Robot Terrain Classification Using Proprioceptive and Exteroceptive Data},
  pdfsubject         = {PhD Thesis},
  pdfkeywords        = {University of Bremen 2015},
  pdfauthor          = {Mohammed Nour Abdelgwad Ahmed},
  pageanchor,
  pdfa]{hyperref}
  
\renewcommand*{\backref}[1]{[#1]}

%\usepackage{threeparttable} %for table with footnotes directly below the table

%:-------------------------- make index and glossary  -----------------------
\usepackage{makeidx}
\usepackage[intoc,refpage]{nomencl}
%\def\pagedeclaration#1{, \hyperlink{page.#1}{page\nobreakspace#1}}
\def\pagedeclaration#1{, \hyperlink{page.#1}{[\nobreakspace#1]}}
\makenomenclature
\makeindex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% User specified LaTeX commands.

\AfterFile{t1lmss.fd}{%
  \DeclareFontShape{T1}{lmss}{b}{n}
  {<->ssub*lmss/bx/n}{}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%the space before chapter title
%\renewcommand*\renewcommand*\chapterheadstartvskip{\vspace*{-10\baselineskip}}{\vspace*{10\baselineskip}}
\renewcommand*{\chapterheadstartvskip}{\vspace*{8\baselineskip}}
%---------------------------------------------------------------------
%the fancy rule after the chapter title
\newcommand*{\ORIGchapterheadendvskip}{}%
\let\ORIGchapterheadendvskip=\chapterheadendvskip
\renewcommand*{\chapterheadendvskip}{%
    {%
        \setlength{\parskip}{0pt}%
        \noindent\rule{.3\textwidth}{3pt}\rule[2.5pt]{.7\linewidth}{.5pt}\par%
    }%
    \vskip2em
}
\newcommand{\norm}[1]{\lVert#1\rVert}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\makeatletter
\providecommand{\toclevel@lstlisting}{0}
\makeatother

% KOMA: Smaller caption font; Looks better, thanks fh!
\addtokomafont{caption}{\small}
\setkomafont{captionlabel}{\sffamily\bfseries}
\setcapindent{1em}
\renewcommand \theparagraph {(\arabic{paragraph})}

\definecolor{dissdarkgray}{gray}{.5}

\labelformat{chapter}{Chapter~#1}%
\labelformat{section}{Section~#1}%
\labelformat{subsection}{Section~#1}%
\labelformat{subsubsection}{Section~#1}%
\labelformat{paragraph}{Paragraph~#1}%
\labelformat{subparagraph}{Paragraph~#1}%
\labelformat{equation}{Equation~#1}%
\labelformat{figure}{Figure~#1}%
\labelformat{subfigure}{Figure~\thefigure~#1}%
\labelformat{table}{Table~#1}%
\labelformat{lstlisting}{Listing~#1}%
\labelformat{listing}{Listing~#1}%
\labelformat{item}{Item~#1}%


\setlength{\nomlabelwidth}{.20\hsize}
\renewcommand{\nomlabel}[1]{#1 \dotfill}


%Hyperref with makeindex: required
\newcommand*{\main}[1]{\textbf{\hyperpage{#1}}}

%\fancyheadoffset[LE,RO]{\marginparsep+\marginparwidth}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}
%\fancyfoot[LE,RO]{\bfseries\thepage}
\fancyhf{}%
\fancyfoot[RO]{\rightmark\quad{\bfseries\thepage}}
\fancyfoot[LE]{{\bfseries\thepage}\quad\leftmark}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[RO]{{\bfseries\thepage}}
  \fancyfoot[LE]{{\bfseries\thepage}}
  \renewcommand{\headrulewidth}{0pt}
}

\renewcommand{\footnotemargin}{1em}