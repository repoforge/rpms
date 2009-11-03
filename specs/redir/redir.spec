# $Id$
# Authority: dag
# Upstream: Sam Creasey <sammy$sammy,net>

Summary:  TCP port redirector
Name: redir
Version: 2.2.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sammy.net/~sammy/hacks/

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
%{__install} -Dp -m0755 redir.orig %{buildroot}%{_bindir}/redir
%{__install} -Dp -m0755 redir %{buildroot}%{_bindir}/redir-ha
%{__install} -Dp -m0644 redir.man %{buildroot}%{_mandir}/man1/redir.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES contrib/README* contrib/redir-wrapper* COPYING README transproxy.txt
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.1-1.2
- Rebuild for Fedora Core 5.

* Sun Apr 25 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Initial package. (using DAR)
