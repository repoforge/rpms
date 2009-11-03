# $Id$
# Authority: dag
# Upstream: <tcptrace$tcptrace,org>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Performs analysis of tcp flows from packet dumps
Name: tcptrace
Version: 6.6.7
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tcptrace.org/

Source: http://tcptrace.org/download/tcptrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
tcptrace is a tool for performing analysis on network packet dumps and
extracting various statistics on the captured traffic as well as generating
several types of graphs.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -Dp -m0755 tcptrace %{buildroot}%{_bindir}/tcptrace
%{__install} -Dp -m0755 versnum %{buildroot}%{_bindir}/versnum
%{__install} -Dp -m0755 xpl2gpl %{buildroot}%{_bindir}/xpl2gpl
%{__install} -Dp -m0644 tcptrace.man %{buildroot}%{_mandir}/man1/tcptrace.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARGS CHANGES COPYING COPYRIGHT FAQ README* THANKS WWW input/
%doc %{_mandir}/man1/tcptrace.1*
%{_bindir}/tcptrace
%{_bindir}/versnum
%{_bindir}/xpl2gpl

%changelog
* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 6.6.7-1
- Updated to release 6.6.7.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 6.0.1-0
- Initial package. (using DAR)
