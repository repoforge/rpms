# $Id$
# Authority: dag

Summary: Tool to become root with one's own password
Name: calife
%define real_version 2.8.6-p5
Version: 2.8.6p5
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://frmug.org/mutt/calife/

Source: ftp://ftp.frmug.org/pub/calife/calife-%{real_version}.tar.gz
Patch1: calife-2.8.6p5-config.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Calife is small program that enable a system administrator to become root (or
another user) on his/her machines without giving the root password but his/her
own.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<'EOF' >calife.auth
### calife.auth
###
### Format:
###    name[:shell_to_be_run][:user1,user2,...,usern]

### Examples:
#fcb
#roberto:/bin/tcsh
#pb::guest,blaireau
EOF

%build
%configure --with-etcdir="%{_sysconfdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m4755 calife %{buildroot}%{_bindir}/calife
%{__install} -D -m0644 calife.1 %{buildroot}%{_mandir}/man1/calife.1
%{__install} -D -m0644 calife.auth.5 %{buildroot}%{_mandir}/man5/calife.auth.5
%{__install} -D -m0600 calife.auth-dist %{buildroot}%{_sysconfdir}/calife.auth

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/calife.1*
%doc %{_mandir}/man5/calife.auth.5*
%config(noreplace) %{_sysconfdir}/calife.auth
%defattr(4755, root, root, 0755)
%{_bindir}/calife

%changelog
* Mon Apr 24 2006 Dag Wieers <dag@wieers.com> - 2.8.6p5-1
- Initial package. (using DAR)
