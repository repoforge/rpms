# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Sam Creasey <sammy@sammy.net>

Summary:  TCP port redirector
Name: redir
Version: 2.2.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://sammy.net/~sammy/hacks/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://sammy.net/~sammy/hacks/redir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tcp_wrappers

%description
redir is a port redirector, used to forward incoming connections
to somewhere else. by far the cleanest piece of code here, because
someone else liked it enough to fix it.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -DUSE_TCP_WRAPPERS" \
	LDFLAGS="-s -lwrap"
%{__mv} -f redir redir.orig

%{__mv} -f contrib/redir-ha.c redir.c
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -DUSE_TCP_WRAPPERS" \
	LDFLAGS="-s -lwrap"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 redir.orig %{buildroot}%{_bindir}/redir
%{__install} -D -m0755 redir %{buildroot}%{_bindir}/redir-ha
%{__install} -D -m0644 redir.man %{buildroot}%{_mandir}/man1/redir.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README transproxy.txt contrib/README* contrib/redir-wrapper*
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Apr 25 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Initial package. (using DAR)
