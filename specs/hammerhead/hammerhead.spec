# $Id$

# Authority: dag

Summary: Web server stress testing tool
Name: hammerhead
Version: 2.1.3
Release: 0
License: GPL
Group: Applications/Internet
URL: http://hammerhead.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/hammerhead/hammerhead-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
Hammerhead 2 is a stress testing tool designed to test out your web server
and web site. It can initiate multiple connections from IP aliases and
simulated numerous (256+) users at any given time. The rate at which
Hammerhead 2 attempts to pound your site is fully configurable, there
are numerous other options for trying to create problems with a web site
(so you can fix them). It can be used to test the behaviour of the port
under load, or the ability of the port to service a set of requests. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall

%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_sysconfdir}/hammerhead/ \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 src/hammerhead %{buildroot}%{_bindir}
%{__install} -m0644 doc/*.conf doc/*.scn %{buildroot}%{_sysconfdir}/hammerhead/
%{__install} -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG Copying README bin/* doc/hammerhead.html doc/hammerhead.txt
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/hammerhead/
%{_bindir}/*

%changelog
* Tue Jun 10 2003 Dag Wieers <dag@wieers.com> - 2.1.3-0
- Initial package. (using DAR)
