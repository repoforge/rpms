# $Id$

# Authority: dag

Summary: Display dBase III and IV (.dbf) files
Name: dbview
Version: 1.0.3
Release: 0
License: GPL
Group: Applications/Databases
URL: ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/%{name}-%{version}.tar.gz
Patch: dbview-patch
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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 dbview %{buildroot}%{_bindir}
%{__install} -m0644 dbview.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc dBASE README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Initial package. (using DAR)
