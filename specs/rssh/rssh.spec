# $Id$
# Authority: dag
# Upstream: Derek Martin <code$pizzashack,org>
# Upstream: <rssh-discuss$lists,sf,net>

Summary: Restricted shell for use with OpenSSH, allowing only scp and/or sftp
Name: rssh
Version: 2.3.3
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.pizzashack.org/rssh/

Source: http://dl.sf.net/rssh/rssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssh-server, openssh-clients
Requires: openssh-server

%description
rssh is a restricted shell for use with OpenSSH, allowing only scp
and/or sftp. For example, if you have a server which you only want
to allow users to copy files off of via scp, without providing shell
access, you can use rssh to do that.

%prep
%setup

# Temporary fix for non-root compilation (submitted upstream)
sed -i 's|chmod u+s $(libexecdir)/rssh_chroot_helper|chmod u+s $(DESTDIR)$(libexecdir)/rssh_chroot_helper|g' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CHROOT COPYING NEWS README SECURITY TODO
%doc %{_mandir}/man1/rssh.1*
%doc %{_mandir}/man5/rssh.conf.5*
%config(noreplace) %{_sysconfdir}/rssh.conf
%{_bindir}/rssh
%attr(4755, root, root) %{_libexecdir}/rssh_chroot_helper

%changelog
* Mon Aug 09 2010 Yury V. Zaytsev <yury@shurup.com> - 2.3.3-1
- Updated to release 2.3.3.
- Thanks to Nico Kadel-Garcia <nkadel@gmail.com>!

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 2.3.2-1
- Updated to release 2.3.2.

* Thu Jan 27 2005 Dag Wieers <dag@wieers.com> - 2.2.3-1
- Updated to release 2.2.3.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 2.2.1-2
- Fixed ownership of rssh_chroot_helper, defattr is ignored. (Robin Green)

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Mon Jul 21 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1.

* Thu Jul 10 2003 Dag Wieers <dag@wieers.com> - 2.1.0-0
- Updated to release 2.1.0.

* Sat Jun 07 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Initial package. (using DAR)
