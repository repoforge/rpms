# $Id$

%define gkrellmpluginver 2.5

Summary: Dell laptop (Inspiron 8000 and others) SMM BIOS support tools.
Name: i8kutils
Version: 1.17
Release: 7.fr
License: GPL
Group: System Environment/Base
Source0: http://people.debian.org/~dz/i8k/i8kutils-%{version}.tar.bz2
Source1: http://www.coding-zone.com/i8krellm-%{gkrellmpluginver}.tar.gz
Source2: i8kbuttons.init
URL: http://people.debian.org/~dz/i8k/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gkrellm >= 2.0.0
BuildRequires: gkrellm-devel >= 2.0.0
# Stock Red Hat / Fedora gkrellm-devel should require these
BuildRequires: gtk2-devel, pkgconfig

%description
This package contains a user-space programs for accessing the SMM BIOS of
Dell Inspiron and Latitude laptops. The SMM BIOS is used on many recent
laptops to implement APM functionalities and to access custom hardware,
for example cooling fans and volume buttons.

Also provided is a cool and useful plugin for gkrellm.
Note that you need the "Inspiron 8000" option compiled into your kernel
(included in the main kernel tree since 2.4.14-pre8).

%prep
%setup -q -a 1

%build
make %{?_smp_mflags}
pushd i8krellm-%{gkrellmpluginver}
    make %{?_smp_mflags} i8krellm
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
cp -a i8kbuttons i8kctl i8kmon i8kfan %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
cp -a *[a-z].1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_libdir}/gkrellm2/plugins/
pushd i8krellm-%{gkrellmpluginver}
    cp -a i8krellm.so %{buildroot}%{_libdir}/gkrellm2/plugins/
popd

install -D -m 755 %{SOURCE2} %{buildroot}%{_initrddir}/i8kbuttons

%post
/sbin/chkconfig --add i8kbuttons

%preun
if [ $1 -eq 0 ]; then
    /sbin/service i8kbuttons stop >/dev/null 2>&1
    /sbin/chkconfig --del i8kbuttons
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README.i8kutils i8kmon.conf
%doc i8krellm-%{gkrellmpluginver}/AUTHORS i8krellm-%{gkrellmpluginver}/README
%doc i8krellm-%{gkrellmpluginver}/Changelog
%{_initrddir}/i8kbuttons
%{_bindir}/*
%{_libdir}/gkrellm2/plugins/*
%{_mandir}/man1/*

%changelog
* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.17-7.fr
- Rebuild for Fedora Core 1.
- Update gkrellm plugin to 2.5, change in the plugin name.

* Mon Sep 15 2003 Matthias Saou <http://freshrpms.net/>
- Added the i8kbuttons init script contributed by Jeremy Brand.

* Fri Aug 29 2003 Matthias Saou <http://freshrpms.net/>
- Updated i8krellm to 2.4.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Updated i8krellm to 2.3.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Updated i8krellm to 2.2.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Updated i8krellm to 2.1.

* Tue Oct  8 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Update to 1.17.
- Disabled the gkrellm plugin until it gets compatible with gkrellm2.

* Thu Jun 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.13.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.11.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Jan 21 2002 Matthias Saou <http://freshrpms.net/>
- Updated the gkrellm plugin to 1.3.

* Sun Jan 13 2002 Matthias Saou <http://freshrpms.net/>
- Updated to 1.8 and gkrellm plugin to 1.2.
- Fix for i8krellm docs that were getting installed with the man pages.

* Tue Dec  4 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

