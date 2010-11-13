# $Id$
# Authority: dag

Summary: Display dBase III and IV (.dbf) files
Name: dbview
Version: 1.0.3
Release: 0.2%{?dist}
License: GPL
Group: Applications/Databases
URL: ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/

Source: ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/dbview-%{version}.tar.gz
Patch0: dbview-patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Dbview is a little tool that will display dBase III and IV files.
You can also use it to convert your old .dbf files for further use
with Unix.

%prep
%setup
%patch

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dbview %{buildroot}%{_bindir}/dbview
%{__install} -Dp -m0644 dbview.1 %{buildroot}%{_mandir}/man1/dbview.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc dBASE README
%doc %{_mandir}/man1/dbview.1*
%{_bindir}/dbview

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.3-0.2
- Rebuild for Fedora Core 5.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Initial package. (using DAR)
