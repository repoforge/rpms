# $Id$
# Authority: dag
# Upstream Ugo Viti <ugo,viti$initzero,it>

Summary: Universal backup system
Name: synbak
Version: 1.2.1
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.initzero.it/products/opensource/synbak/

Source: http://www.initzero.it/products/opensource/synbak/download/synbak-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl-XML-Parser, gettext
Requires: bash >= 2.0, bc, gawk, mktemp >= 1.5, nc, rsync, sed, tar

%description
Synbak is an application designed to unify several backup methods. Synbak
provides a powerful reporting system and a very simple interface for
configuration files.

Synbak is a wrapper for several existing backup programs suppling the
end user with common method for configuration that will manage the
execution logic for every single backup and will give detailed reports
of backups result.

Synbak can make backups using rsync (ssh, rsync, smb, cifs), tar (tar.gz,
tar.bz2), tape, ldap, mysql and oracle databases and removable media
(cdr, dvd-rw, dvr, dvd-rw) and more...

Synbak can make reports using email, html, rss-feeds and more...

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang synbak

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README THANKS TODO examples/
%{_bindir}/synbak
%{_datadir}/synbak/

%changelog
* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Fri Nov 30 2007 Dag Wieers <dag@wieers.com> - 1.0.12-1
- Updated to release 1.0.12.

* Sat Oct 14 2006 Dag Wieers <dag@wieers.com> - 1.0.10-1
- Updated to release 1.0.10.

* Sat Sep 16 2006 Dag Wieers <dag@wieers.com> - 1.0.9-1
- Updated to release 1.0.9.

* Wed Aug 23 2006 Dag Wieers <dag@wieers.com> - 1.0.8-1
- Updated to release 1.0.8.

* Sun Aug 20 2006 Dag Wieers <dag@wieers.com> - 1.0.7-2
- Changed netcat dependency to nc. (Ugo Viti)

* Sun Aug 20 2006 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Initial package. (using DAR)
