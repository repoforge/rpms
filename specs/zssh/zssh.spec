# $Id$

# Authority: dries

%define real_version 1.5c

Summary: Zmodem SSH
Name: zssh
Version: 1.5
Release: 0.c.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://zssh.sourceforge.net/

Source: http://dl.sf.net/zssh/zssh-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel

%description
zssh (Zmodem SSH) is a program for interactively transferring files to a
remote machine while using the secure  shell (ssh).  It  is intended to be a
convenient alternative to scp , allowing to transfer files without  having
to  open another session and re-authenticate oneself.

zssh  is an interactive wrapper for ssh used to switch the ssh connection
between the remote shell  and  file  transfers.  This  is  achieved  by
using  another tty/pty pair between the user and the local ssh process to
plug  either the  user's  tty  (remote  shell  mode) or another process
(file transfer mode) on the ssh connection.

%prep
%setup -n zssh-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dpp -m0711 zssh %{buildroot}%{_bindir}/zssh
%{__ln_s} %{_bindir}/zssh  %{buildroot}%{_bindir}/ztelnet
%{__install} -Dpp -m0644 zssh.1 %{buildroot}%{_mandir}/man1/zssh.1
%{__install} -Dpp -m0644 ztelnet.1 %{buildroot}%{_mandir}/man1/ztelnet.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README TODO
%doc %{_mandir}/man1/zssh.1*
%doc %{_mandir}/man1/ztelnet.1*
%{_bindir}/zssh
%{_bindir}/ztelnet

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-0.c.2
- Rebuild for Fedora Core 5.

* Thu Jan 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-0.c
- Initial package.
