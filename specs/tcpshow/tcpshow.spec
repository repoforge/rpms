# $Id$
# Authority: dag

Summary: Prints dump files created by tcpdump
Name: tcpshow
Version: 1.0
Release: 1%{?dist}
License: distributable; see tcpshow.c for details
Group: Applications/Internet
URL: http://www.cs.berkeley.edu/~daw/mike/

Source0: http://www.cs.berkeley.edu/~daw/mike/tcpshow.c
Source1: http://www.cs.berkeley.edu/~daw/mike/tcpshow.1
Patch0: tcpshow.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: tcpdump

%description
Utility to print raw packet dumps from tcpdump(8).

%prep
%setup -c -T
%{__cp} -av %{SOURCE0} %{SOURCE1} .
%patch0 -p0

%build
#%{__cc} -static %{optflags} -o tcpshow tcpshow.c
%{__cc} %{optflags} -o tcpshow tcpshow.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 tcpshow %{buildroot}%{_sbindir}/tcpshow
%{__install} -Dp -m0644 tcpshow.1 %{buildroot}%{_mandir}/man1/tcpshow.1

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/tcpshow.1*
%{_sbindir}/tcpshow

%clean
%{__rm} -rf %{buildroot}

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
