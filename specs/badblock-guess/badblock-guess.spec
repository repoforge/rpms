# $Id$
# Authority: dag
# Upstream: Jan Kratochvil <web$jankratochvil,net>

%define real_version cvs20030610

Summary: Data recovery from a damaged disk
Name: badblock-guess
Version: 0.0
Release: 0.cvs20030610%{?dist}
License: GPL
Group: Applications/System
URL: http://www.jankratochvil.net/project/badblock_guess/

Source: http://cvs.jankratochvil.net/viewcvs/badblock-guess/badblock-guess.tar.gz?tarball=1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel

%description
badblock-guess will recover all readable sectors of the disk in minimal time
while trying to prevent disk read retrying head recalibrations.

%prep
%setup -n %{name}

%{__perl} -pi -e 's|-O2 -Wall -static|%{optflags} -shared -fPIC|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 badblock-guess %{buildroot}%{_bindir}/badblock-guess

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/badblock-guess

%changelog
* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 0.0-0.cvs20030610
- Initial package. (using DAR)
