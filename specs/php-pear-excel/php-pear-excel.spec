# $Id$

%define php_dir %(eval "`pear config-get php_dir`"; echo $php_dir)

Summary: PEAR package for generating Excel spreadsheets
Name: php-pear-excel
Version: 0.7
Release: 1
License: LGPL
Group: Development/Languages
URL: http://pear.php.net/package/Spreadsheet_Excel_Writer/
Source1: http://pear.php.net/get/Spreadsheet_Excel_Writer-%{version}.tgz
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
rm -rf %{buildroot}
pear install -R %{buildroot} -n %{SOURCE1}
# Remove .filemap and .lock, we don't want to include those
rm -f %{buildroot}%{php_dir}/{.filemap,.lock}


%clean
rm -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{php_dir}


%changelog
* Thu Mar 11 2004 Matthias Saou <http://freshrpms.net/> 0.7-1
- Initial RPM release.

