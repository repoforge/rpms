# $Id$
# Authority: dag

Summary: Let ordinary users mount an encrypted file system
Name: cryptmount
Version: 3.1
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://cryptmount.sourceforge.net/

Source: http://dl.sf.net/cryptmount/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgcrypt-devel
Requires: libgcrypt
Requires: device-mapper

%description
cryptmount is a utility for the GNU/Linux operating system which allows
an ordinary user to mount an encrypted filing system without requiring
superuser privileges. Filesystems can reside on raw disk partitions or
ordinary files, with cryptmount automatically configuring 
device-mapper and loopback devices before mounting.

%prep
%setup

%{__perl} -pi.orig -e '
        s|chown|echo|g;
        s|/etc/init.d|%{_initrddir}|g;
    ' Makefile.in

%build
%configure --enable-delegation --enable-fsck
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_initrddir}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/default/
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* RELNOTES ToDo
%doc %{_mandir}/man5/cmtab.5*
%doc %{_mandir}/man8/cryptmount.8*
%doc %{_mandir}/man8/cryptmount-setup.8*
%doc %{_mandir}/*/man5/cmtab.5*
%doc %{_mandir}/*/man8/cryptmount.8*
%config(noreplace) %{_sysconfdir}/cryptmount
%config %{_initrddir}/cryptmount
%config %{_initrddir}/cryptmount-early
%config %{_sysconfdir}/default/
%{_sbindir}/cryptmount-setup
%{_libdir}/cryptmount/

%defattr(4751, root, root, 0755)
%{_bindir}/cryptmount

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 3.1-1
- Initial package. (using DAR)
