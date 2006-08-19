# $Id$
# Authority: dag

Summary: Universal backup system
Name: synbak
Version: 1.0.7
Release: 1
License: GPL
Group: Applications/File
URL: http://www.initzero.it/products/opensource/synbak/

Source: http://www.initzero.it/products/opensource/synbak/download/synbak-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl-XML-Parser
Requires: bash >= 2.0, bc, gawk, mktemp >= 1.5, netcat, rsync, sed, tar

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

### FIXME: Installer puts x86_64 in /usr/lib64 despite being a noarch package !
%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README THANKS TODO examples/
%{_bindir}/synbak
%{_libdir}/synbak/

%changelog
* Sun Aug 20 2006 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Initial package. (using DAR)
