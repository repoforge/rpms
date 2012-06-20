# $Id$
# Authority: dag


%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}
%{?rh6:%define _without_tcltk_devel 1}

Summary: IRC bot
Name: eggdrop
Version: 1.6.21
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.eggheads.org/

Source: ftp://ftp.eggheads.org/pub/eggdrop/GNU/stable/eggdrop%{version}.tar.bz2
#Patch0: eggdrop1.6.17-lib64.patch
#Patch1: eggdrop1.6.17-64bit-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tcl, perl
%{!?_without_tcltk_devel:BuildRequires: tcl-devel}

%description
Eggdrop is an IRC bot, written in C.  If you don't know what IRC is,
this is probably not whatever you're looking for!  Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN),

to recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc.

%prep
%setup -n %{name}%{version}
#patch0 -p1 -b .lib64
#%patch1 -p1 -b .64bit-fixes

# _smp_mflags removed, compile fails on multiprocessor system  
%build
#reautoconf
%configure \
	--with-tclinc="%{_includedir}/tcl.h" \
	--with-tcllib="%{_libdir}/libtcl.so"
%{__make} config all

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/eggdrop/
%{__make} install prefix="%{buildroot}%{_libdir}/eggdrop"

%{__install} -Dp -m0644 doc/man1/eggdrop.1 %{buildroot}%{_mandir}/man1/eggdrop.1

perl -pi -e 's|/path/to/executable/eggdrop|%{_libdir}/eggdrop/eggdrop|' eggdrop.conf
%{__install} -Dp -m0644 eggdrop.conf %{buildroot}%{_libdir}/eggdrop/eggdrop.conf

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/eggdrop/{doc,filesys,README}
%{__rm} -rf doc/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING FEATURES INSTALL NEWS README doc/* *.conf
%doc %{_mandir}/man1/eggdrop.1*
%{_libdir}/eggdrop/

%changelog
* Mon Jun 18 2012 Shawn Sterling <shawn@systemtemplar.org> - 1.6.21-1
- Updated to release 1.6.21.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.6.19-1
- Updated to release 1.6.19.

* Thu Nov 11 2004 Dag Wieers <dag@wieers.com> - 1.6.17-1
- Updated to release 1.6.17.

* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 1.6.15-1
- Initial package. (using DAR)
