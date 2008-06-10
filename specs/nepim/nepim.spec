# $Id$
# Authority: dag

Summary: Network pipemeter is a network benchmark utility
Name: nepim
Version: 0.48
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/nepim/

Source: http://download.savannah.gnu.org/releases/nepim/nepim-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: liboop-devel

%description
nepim stands for network pipemeter, a tool for measuring available
bandwidth between hosts. nepim is also useful to generate network
traffic for testing purposes.

nepim operates in client/server mode, is able to handle multiple
parallel traffic streams, reports periodic partial statistics along the
testing, and supports IPv6.

%prep
%setup

%build
%{__make} %{?_smp_mflags} -C src

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/nepim %{buildroot}%{_bindir}/nepim

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_bindir}/nepim

%changelog
* Tue Jun 10 2008 Dag Wieers <dag@wieers.com> - 0.48-1
- Updated to release 0.48.

* Fri Aug 17 2007 Dag Wieers <dag@wieers.com> - 0.40-1
- Initial package. (using DAR)
