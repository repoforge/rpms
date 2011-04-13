# $Id$
# Authority: dag

%define real_version 20031202

Summary: Standard netcat enhanced with twofish encryption.
Name: cryptcat
Version: 1.2.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://cryptcat.sourceforge.net/

Source: http://dl.sf.net/project/cryptcat/cryptcat-unix-1.2/cryptcat-unix-1.2.1/cryptcat-unix-%{version}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Cryptcat is the standard netcat enhanced with twofish encryption.
netcat was origianally written by the l0pht (hobbit and weld pond).

%prep
%setup -c %{name}-%{version}

%build
%{__perl} -pi -e 's|STATIC=-static||g;' unix/Makefile
%{__make} -C unix linux

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 unix/cryptcat %{buildroot}%{_bindir}/cryptcat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc unix/Changelog unix/Credits unix/README*
%{_bindir}/cryptcat

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.0.20031202-1
- Initial package. (using DAR)
