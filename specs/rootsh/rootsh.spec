# $Id$
# Authority: dag
# Upstream: Gerhard Lausser <gerhard.lausser$consol,de>

Summary: Shell wrapper to log activity
Name: rootsh
Version: 0.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://sourceforge.net/projects/rootsh/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/rootsh/rootsh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rootsh is a wrapper for shells which logs all echoed keystrokes and terminal
output to a file and/or to syslog. It's main purpose is the auditing of users
who need a shell with root privileges. They start rootsh through the sudo
mechanism.

%prep
%setup

%build
%configure \
%{!?_without_syslog:--enable-syslog="local5.notice"} \
%{?_without_syslog:--disable-syslog} \
	--with-logdir="%{_localstatedir}/log/rootsh"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0700 %{buildroot}%{_localstatedir}/log/rootsh/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/rootsh
%defattr(0700, root, root)
%{_localstatedir}/log/rootsh

%changelog
* Fri Sep 14 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
