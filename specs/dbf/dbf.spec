# $Id$
# Authority: dag
# Upstream: Bjoern Berg <clergyman$gmx,de>
# Upstream: <info$anubisnet,de>
# Upstream: <dbf-general$lists,sf,net>

Summary: Fast convert for dBase, Clipper, FoxBase and Visual FoxPro databases
Name: dbf
Version: 0.8.3.1
Release: 1.2%{?dist}
License: LGPL
Group: Applications/Databases
URL: http://dbf.berlios.de/

Source: http://download.berlios.de/dbf/dbf-%{version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Fast convert for dBase, Clipper, FoxBase and Visual FoxPro databases

dbf is an easy-to-use command line tool to show and convert the content
of dBASE III, IV, and 5.0 files. It reads dBASE databases and prints
the content to the screen or converts it to comma-separated (*.csv)
files which can be opened in Excel, StarOffice, and most other spread
sheets. It can also be used to show some statistics about the content.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}" \
	PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog CREDITS FAQ INSTALL MANIFEST README
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.3.1-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 0.8.3.1-1
- Updated to release 0.8.3.1.

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 0.8.3-1
- Initial package. (using DAR)
