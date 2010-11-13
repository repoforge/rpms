# $Id$
# Authority: dag

Summary: Utility for switching the LCD and external VGA displays on and off
Name: i810switch
Version: 0.6.5
Release: 1%{?dist}
License: GPL
Group: User Interface/X Hardware Support
URL: http://www16.plala.or.jp/mano-a-mano/i810switch.html

Source: http://www16.plala.or.jp/mano-a-mano/i810switch/i810switch-0.6.5.tar.gz
Patch0: i810switch-0.6.2.makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: pciutils

%description
i810switch is a utility for switching the LCD and external VGA
displays on and off under Linux. It was originally written by Antonino
Daplas, and is now maintained by Ken Mano.

%prep
%setup
%patch0 -p1 -b .buildroot
%{__make} clean

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/i810rotate.1*
%doc %{_mandir}/man1/i810switch.1*
%{_bindir}/i810rotate
%{_bindir}/i810switch

%changelog
* Sat Feb 24 2007 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Initial package. (using DAR)
