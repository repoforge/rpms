# $Id$
# Authority: dag

Summary: Non-interactive SSH authentication utility
Name: sshpass
Version: 1.05
Release: 1%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://sshpass.sourceforge.net/

Source: http://dl.sf.net/sshpass/sshpass-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Tool for non-interactively performing password authentication with so called
"interactive keyboard password authentication" of SSH. Most users should use
more secure public key authentication of SSH instead.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%doc %{_mandir}/man1/sshpass.1*
%{_bindir}/sshpass

%changelog
* Fri Nov 23 2012 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
