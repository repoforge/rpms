# $Id$

# Authority: dag
# Upstream: <graeme$rillion,net>

Summary: Interactive program which monitors squid logs and displays them in a nice fashion
Name: squidview
Version: 0.63
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.rillion.net/squidview/

Source: http://www.rillion.net/squidview/squidview-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gcc-c++

%description
Squidview is an interactive program which monitors squid logs and
displays them in a nice fashion. It has searching and reporting
functions.

%prep
%setup

#%{__perl} -pi.orig -e '
#		s|PREFIX|prefix|g;
#		s|BINDIR|bindir|g;
#		s|DATADIR|datadir|g;
#		s|DOCDIR|docdir|g;
#	' Makefile

%build
%configure
%{__make} %{?_smp_mflags} \
	CXXFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/squidview/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING HOWTO NEWS README example.log
%{_bindir}/*

%changelog
* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.63-0
- Updated to release 0.63.

* Sun Sep 21 2003 Dag Wieers <dag@wieers.com> - 0.51-0
- Initial package. (using DAR)
