# $Id$
# Authority: dag

Summary: Create connections through HTTP-proxy's and SOCKS-servers
Name: connect
Version: 1.95
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://zippo.taiyo.co.jp/~gotoh/ssh/connect.html

#Source: %{name}-%{version}.tar.bz2
Source0: http://www.taiyo.co.jp/~gotoh/ssh/connect.c
Source1: http://zippo.taiyo.co.jp/~gotoh/ssh/connect.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Small program that lets you create connections through HTTP-proxy's
and SOCKS-servers.

%prep
#setup -n %{name}
%setup -c -T
%{__cp} -avx %{SOURCE0} connect.c
%{__cp} -avx %{SOURCE1} connect.html

%build
%{__cc} %{optflags} -o connect connect.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 connect %{buildroot}%{_bindir}/connect

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc connect.html
%{_bindir}/connect

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.95-1.2
- Rebuild for Fedora Core 5.

* Fri Dec 23 2005 Dag Wieers <dag@wieers.com> - 1.95-1
- Updated to release 1.95.

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 1.41-0
- Initial package. (using DAR)
