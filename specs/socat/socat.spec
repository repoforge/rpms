# $Id: _template.spec 130 2004-03-17 10:51:35Z dude $

# Authority: dag
# Upstream: <socat@dest-unreach.org>

Summary: Relay for bidirectional data transfer between 2 channels.
Name: socat
Version: 1.3.2.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.dest-unreach.org/socat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.dest-unreach.org/socat/download/socat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel, openssl-devel
Requires: tcp_wrappers

%description
socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor, a program, or a combination of two of these. 

%prep
%setup -n %{name}-1.3

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\@bindir\@|\$(bindir)|;
		s|\@mandir\@|\$(mandir)|;
	' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/

%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGREPORTS CHANGES COPYING* DEVELOPMENT EXAMPLES FAQ FILES PORTING README SECURITY
%doc xio.help socat.html
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
