# $Id$
# Upstream: Daichi GOTO <daichi$FreeBSD,org>

Summary: display command output on the whole screen like ``top''
Name: topless
Version: 1.53
Release: 1%{?dist}
Source0: http://people.freebsd.org/~daichi/src/topless
Source1: http://people.freebsd.org/~daichi/src/topless-1.52.tar.gz
Source2: LICENSE.topless
License: BSD
Group: Applications/Text
Url: http://www.ongs.net/daichi/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
BuildRequires: perl

%description
TOPLESS reads various command output, displays it on the whole screen
(like "less"), and periodically updates it like "top".

TOPLESS can be used with almost every sort of command,
but is particularly useful when used with the command
to monitor the system, such as "ps", "netstat" or "fstat".

%prep
%setup -T -a 1 -c %{name}-%{version}
%{__cp} %{SOURCE2} LICENSE

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%__install -m0755 %{SOURCE0} %{buildroot}%{_bindir}
pod2man topless-1.52/topless.pod > %{buildroot}%{_mandir}/man1/topless.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc LICENSE
%doc %{_mandir}/man1/topless.1*
%{_bindir}/topless

%changelog
* Thu Jun 28 2012 IWAI, Masaharu <iwaim.sub@gmail.com> - 1.53-1
- Initial release.

