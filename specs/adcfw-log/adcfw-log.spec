# $Id$
# Authority: dag
# Upstream: Alessandro Dotti Contra <alessandro.dotti@iperbole.bologna.it>
# Upstream: <adcfw-log-devel@lists.sourceforge.net>

Summary: Tool for analyzing firewall logs
Name: adcfw-log
Version: 0.9.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://adcfw-log.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/adcfw-log/adcfw-log-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.6.1
Requires: perl >= 1:5.6.1

%description
adcfw-log is a tool for analyzing firewall logs in order to extract
meaningful information. It is designed to be a standalone script
with very few requirements that can generate different kinds of
reports, such as fully formatted reports of what had been logged,
with summaries by source or destination host, the type of service,
or protocol. There are also options to filter the input data by date,
host, protocol, service, and so on.

Only netfilter log format (linux kernel 2.4.x) is supported at this time.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
