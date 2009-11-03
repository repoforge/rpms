# $Id$

Summary: Additional addons for Asterisk: the Open Source Linux PBX
Name: asterisk-addons
Version: 1.2.5
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.asterisk.org/
Source0: http://ftp.digium.com/pub/asterisk/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: asterisk
BuildRequires: asterisk-devel, mysql-devel, zlib-devel

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

This package contains additional addons for asterisk.


%prep
%setup -q
%{__perl} -pi -e's|/lib/|/%{_lib}/|g' Makefile asterisk-ooh323c/Makefile*


%build
export CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}
# Also build the ooh323c module
cd asterisk-ooh323c
%configure
%{__make} %{?_smp_mflags}
cd ..


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_libdir}/asterisk/modules/
%{__make} install INSTALL_PREFIX=%{buildroot}
# Also install the ooh323c module
cd asterisk-ooh323c
%{__make} install DESTDIR=%{buildroot}
cd ..



%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc doc/cdr_mysql.txt format_mp3/README
%{_libdir}/asterisk/modules/*.so


%changelog
* Fri Nov 24 2006 Matthias Saou <http://freshrpms.net/> 1.2.5-1
- Update to 1.2.5.

* Wed Sep 13 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-2
- Also build the asterisk-ooh323c module.

* Thu Sep  7 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.

* Fri Apr  7 2006 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Import Axel's spec file into rpmforge.

* Tue Mar  7 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.2.

* Mon Dec 12 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.1.

* Mon Nov 21 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.0.

* Sat Jul 16 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.9.

* Mon Jun 27 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.0.8.

* Mon Mar 07 2005 Mark Wormgoor <mark@wormgoor.com>
- Initial version

