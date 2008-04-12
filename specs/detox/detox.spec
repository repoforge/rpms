# $Id$
# Authority: dries
# Upstream: Doug Harple <purgedhalo$users,sourceforge,net>

Summary: Utility for cleaning up filenames
Name: detox
Version: 1.2.0
Release: 1
License: BSD
Group: Applications/Text
URL: http://detox.sourceforge.net/

Source: http://dl.sf.net/detox/detox-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Detox is a utility designed to clean up filenames. It replaces difficult to 
work with characters, such as spaces, with standard equivalents. It will 
also clean up filenames with UTF-8 or Latin-1 (or CP-1252) characters in them.

%prep
%setup

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
%doc CHANGES LICENSE README
%doc %{_mandir}/man1/detox.1*
%doc %{_mandir}/man5/detox*.5*
%{_bindir}/detox
%{_bindir}/inline-detox
%{_datadir}/detox/
%{_sysconfdir}/detoxrc*

%changelog
* Sat Apr 12 2008 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1
- Initial package.
