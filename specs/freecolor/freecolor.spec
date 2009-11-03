# $Id$
# Authority: dries
# Upstream: <phm$rkeene,org>

Summary: Disk free stats with colors
Name: freecolor
Version: 0.8.7
Release: 2.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.rkeene.org/oss/freecolor/

Source: http://www.rkeene.org/files/oss/freecolor/freecolor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
freecolor adds color and bargraphs to the "free" command.

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
%doc ChangeLog README
%{_bindir}/freecolor

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.7-2.2
- Rebuild for Fedora Core 5.

* Wed Dec 07 2005 Dag Wieers <dag@wieers.com> - 0.8.7-2
- Fixed RPM Group.

* Wed Oct 19 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.7-1
- Initial package.
