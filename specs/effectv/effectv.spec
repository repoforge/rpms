# $Id$
# Authority: dag
# Upstream: <effectv-developers$lists,sf,net>

Summary: Real-time video effector
Name: effectv
Version: 0.3.11
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://effectv.sourceforge.net/

Source: http://dl.sf.net/effectv/effectv-%{version}.tar.bz2
Patch0: effectv-0.3.11-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: nasm, SDL-devel

%description
EffecTV is a real-time video effector. You can watch TV or video through
amazing effectors.

%prep
%setup
%patch0 -p1

%build
%{__make} %{?_smp_mflags} CFLAGS.opt="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING CREWS FAQ README* TODO
%doc %{_mandir}/man1/effectv.1*
%{_bindir}/effectv

%changelog
* Sat Feb 18 2006 Dag Wieers <dag@wieers.com> - 0.3.11-1
- Updated to release 0.3.11.

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 0.3.10-1
- Updated to release 0.3.10.

* Tue Jan 13 2004 Dag Wieers <dag@wieers.com> - 0.3.9-0
- Updated to release 0.3.9.

* Sat Aug 10 2002 Dag Wieers <dag@wieers.com> - 0.3.7-0
- Initial package.
