# $Id$
# Authority: dag
# Upstream: Zeljko Vrba <zvrba$globalnet,hr>

Summary: Secure password generator
Name: secpwgen
Version: 1.3
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.core-dump.com.hr/?q=node/28

Source: http://www.core-dump.com.hr/software/secpwgen-%{version}.tar.gz
Patch0: secpwgen-1.3_build_config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
secpwgen is a utility for generating secure passphrases. It implements several
methods for passphrase generation, including the Diceware method with
8192 word dictionary compiled in the executable.

%prep
%setup
%patch0 -p0

%build
%{__make} -f Makefile.proto OPTFLAGS="%{optflags} -DDISABLE_MLOCKALL"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 secpwgen %{buildroot}%{_bindir}/secpwgen
%{__install} -Dp -m0644 secpwgen.1 %{buildroot}%{_mandir}/man1/secpwgen.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man1/secpwgen.1*
%{_bindir}/secpwgen

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.3-2
- Fix group tag.

* Mon May 07 2007 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
