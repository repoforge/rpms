# $Id$
# Authority: matthias

%define pear_dir %{_datadir}/pear

Summary: PEAR package for generating Excel spreadsheets
Name: php-pear-excel
Version: 0.9.0
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://pear.php.net/package/Spreadsheet_Excel_Writer/
Source0: http://pear.php.net/get/Spreadsheet_Excel_Writer-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php, php-pear-ole >= 0.5
BuildRequires: php

%description
Spreadsheet_Excel_Writer was born as a porting of the Spreadsheet::WriteExcel
Perl module to PHP.  It allows writing of Excel spreadsheets without the need
for COM objects.  It supports formulas, images (BMP) and all kinds of
formatting for text and cells.  It currently supports the BIFF5 format (Excel
5.0), so functionality appeared in the latest Excel versions is not yet
available.


%prep


%install
%{__rm} -rf %{buildroot}
pear install -R %{buildroot} -n %{SOURCE0}
# Remove .filemap and .lock, we don't want to include those
%{__rm} -f %{buildroot}%{pear_dir}/{.filemap,.lock}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{pear_dir}


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.

* Fri Apr 15 2005 Matthias Saou <http://freshrpms.net/> 0.8-1
- Update to 0.8.
- Change single source from 1 to 0.
- Use %%{_datadir}/pear instead of the eval method, as it's triggering a
  nasty side-effect that prevents building.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 0.7-2
- Rebuild for Fedora Core 2.

* Thu Mar 11 2004 Matthias Saou <http://freshrpms.net/> 0.7-1
- Initial RPM release.

