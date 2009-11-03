# $Id$
# Authority: dag
# Upstream: <noisy$gmx,net>

Summary: Read, parse, merge and write RSS (and Atom) feeds
Name: rsstool
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://rsstool.berlios.de/

Source: http://download.berlios.de/rsstool/rsstool-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel

%description
rsstool is a utility to read, parse, merge and write RSS (and Atom) feeds.

%prep
%setup -n %{name}-%{version}-src

%build
cd src
%configure
cd -
%{__make} -C src %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} -C src install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 src/rsstool %{buildroot}%{_bindir}/rsstool

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc VERSION *.html
%{_bindir}/rsstool

%changelog
* Mon Feb 04 2008 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sun Dec 10 2006 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Updated to release 0.9.10.

* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Updated to release 0.9.9.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.

* Sat Oct 21 2006 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sun Oct 15 2006 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Sun Oct 08 2006 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Initial package. (using DAR)
