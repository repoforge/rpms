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
Release: 3%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.eggheads.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.eggheads.org/pub/eggdrop/GNU/stable/eggdrop%{version}.tar.bz2
Patch0: eggdrop-1.6.17-langdir.patch
Patch1: eggdrop-1.6.21-no_libdns.patch
Patch2: eggdrop-1.6.21-suzi_sp0011.patch
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
%patch0 -p1 -b .langdir
%patch1 -p1 -b .no_libdns
%patch2 -p1 -b .suzi_sp0011

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

%{__install} -D -m 755 eggdrop %{buildroot}%{_bindir}/eggdrop
%{__install} -Dp -m0644 doc/man1/eggdrop.1 %{buildroot}%{_mandir}/man1/eggdrop.1

# Fix paths of example eggdrop.conf
%{__sed} -e '2d' -e '1s@^.*@#!%{_bindir}/%{name}@' \
	-e 's@scripts/@%{_datadir}/%{name}/scripts/@g' \
	-e 's@help/@%{_datadir}/%{name}/help/@g' \
	-e 's@modules/@%{_libdir}/%{name}/@g' \
	eggdrop.conf > eggdrop.conf.mod
touch -c -r eggdrop.conf eggdrop.conf.mod
%{__mv} -f eggdrop.conf.mod eggdrop.conf
%{__install} -Dp -m0644 eggdrop.conf %{buildroot}%{_libdir}/eggdrop/eggdrop.conf

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o doc/KNOWN-PROBLEMS.utf8 doc/KNOWN-PROBLEMS
touch -c -r doc/KNOWN-PROBLEMS doc/KNOWN-PROBLEMS.utf8
%{__mv} -f doc/KNOWN-PROBLEMS.utf8 doc/KNOWN-PROBLEMS

iconv -f iso-8859-1 -t utf-8 -o doc/Changes1.6.utf8 doc/Changes1.6
touch -c -r doc/Changes1.6 doc/Changes1.6.utf8
%{__mv} -f doc/Changes1.6.utf8 doc/Changes1.6

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/eggdrop/{doc,filesys,README}
%{__rm} -rf doc/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING FEATURES NEWS README SUZI doc/* eggdrop.conf
%{_bindir}/eggdrop
%{_libdir}/eggdrop
%doc %{_mandir}/man1/eggdrop.1*

%changelog
* Sat Sep 29 2012 Denis Fateyev <denis@fateyev.com> - 1.6.21-3
- Some spec cleanup

* Wed Jun 20 2012 David Hrbáč <david@hrbac.cz> - 1.6.21-2
- a few Fedora patches

* Mon Jun 18 2012 Shawn Sterling <shawn@systemtemplar.org> - 1.6.21-1
- Updated to release 1.6.21.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.6.19-1
- Updated to release 1.6.19.

* Thu Nov 11 2004 Dag Wieers <dag@wieers.com> - 1.6.17-1
- Updated to release 1.6.17.

* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 1.6.15-1
- Initial package. (using DAR)
