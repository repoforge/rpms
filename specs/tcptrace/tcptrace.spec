# $Id$

# Authority: dag

Summary: Performs analysis of tcp flows from packet dumps
Name: tcptrace
Version: 6.0.1
Release: 0
License: Modified GPL
Group: Applications/Internet
URL: http://tcptrace.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://tcptrace.org/download/tcptrace.%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 tcptrace versnum xpl2gpl %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc ARGS CHANGES COPYING COPYRIGHT FAQ README* THANKS WWW output_finger.snoop.gz input/
%{_bindir}/*

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 6.0.1-0
- Initial package. (using DAR)
