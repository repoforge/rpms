# $Id$
# Author: dag

%{?el5:%define _without_docbook5 1}
%{?el4:%define _without_docbook5 1}
%{?el3:%define _without_docbook5 1}
%{?el2:%define _without_docbook5 1}

Summary: RelaxNG Compact Syntax Validator
Name: rnv
Version: 1.7.10
Release: 1%{?dist}
License: BSD
Group: Applications/File
URL: http://www.davidashen.net/rnv.html

Source0: http://dl.sf.net/project/rnv/Sources/%{version}/rnv-%{version}.tar.bz2
Source1: reference.xml
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_docbook5:BuildRequires: docbook-style-xsl}
%{!?_without_docbook5:BuildRequires: docbook5-style-xsl}
BuildRequires: expat-devel
BuildRequires: libxslt
BuildRequires: sgml-common

%description
RNV is an implementation of RELAX NG Compact Syntax.
It is written in ANSI C, the command-line utility uses Expat.

RNV is a part of an on-going work, and the current code can
have bugs and shortcomings; however, it validates documents
against a number of grammars. I use it.

%prep
%setup
xsltproc --nonet http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl %{SOURCE1}
xsltproc --nonet --output reference.html http://docbook.sourceforge.net/release/xsl/current/html/docbook.xsl %{SOURCE1}

%build
%configure

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 arx.1 %{buildroot}%{_mandir}/man1/arx.1
%{__install} -Dp -m0644 rnv.1 %{buildroot}%{_mandir}/man1/rnv.1
%{__install} -Dp -m0644 rvp.1 %{buildroot}%{_mandir}/man1/rvp.1
#%{__install} -Dp -m0644 xsdck.1 %{buildroot}%{_mandir}/man1/xsdck.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ChangeLog COPYING reference.html *.txt tools/
%doc %{_mandir}/man1/arx.1*
%doc %{_mandir}/man1/rnv.1*
%doc %{_mandir}/man1/rvp.1*
#%doc %{_mandir}/man1/xsdck.1*
%{_bindir}/arx
%{_bindir}/rnv
%{_bindir}/rvp
%{_bindir}/xsdck

%changelog
* Thu Nov 10 2011 Dag Wieers <dag@wieers.com> - 1.7.10-1
- Initial package. (using DAR)
