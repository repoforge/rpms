# Authority: dag
# Upstream: Derek Martin <code@pizzashack.org>, rssh-discuss@lists.sourceforge.net

Summary: A restricted shell for use with OpenSSH, allowing only scp and/or sftp.
Name: rssh
Version: 2.1.1
Release: 0
License: BSD
Group: Applications/Internet
URL: http://www.pizzashack.org/rssh/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pizzashack.org/rssh/src/rssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: openssh-server
Requires: openssh-server

%description
rssh is a restricted shell for use with OpenSSH, allowing only scp
and/or sftp. For example, if you have a server which you only want
to allow users to copy files off of via scp, without providing shell
access, you can use rssh to do that.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CHROOT COPYING NEWS README SECURITY TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/rssh.conf
%{_bindir}/*
%attr(4755, -, -) %{_libexecdir}/rssh_chroot_helper

%changelog
* Mon Jul 21 2003 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1.

* Thu Jul 10 2003 Dag Wieers <dag@wieers.com> - 2.1.0-0
- Updated to release 2.1.0.

* Sat Jun 07 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Initial package. (using DAR)
