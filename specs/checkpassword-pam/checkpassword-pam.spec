# Authority: dag

Summary: Provides a simple, uniform password-checking interface using PAM.
Name: checkpassword-pam
Version: 0.98
Release: 0
License: GPL
Group: System Environment/Base
URL: http://checkpasswd-pam.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/checkpasswd-pam/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: pam-devel >= 0.59

%description
checkpassword-pam provides a simple, uniform password-checking
interface to all root applications using PAM. It is suitable for
use by applications such as login, ftpd, and pop3d.

There are checkpassword-compatible tools that support alternate
password databases, secret login names, long passwords, subaccounts,
one-time passwords, detailed accounting, and many other features.

Applications that use the checkpassword interface will work with all
of these tools. Several tools have been specifically designed to
support POP toasters.

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
%doc AUTHORS ChangeLog COPYING interface.html README NEWS
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.98-0
- Updated to release 0.98.

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 0.97-0
- Updated to release 0.97.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Initial package. (using DAR)
