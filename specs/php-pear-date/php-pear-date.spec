# $Id$
# Authority: matthias

%define pear_dir %(pear config-get php_dir 2>/dev/null || echo %{_datadir}/pear)
%define xml_dir  %{peardir}/.pkgxml

Summary: PEAR package containing date and time zone classes
Name: php-pear-date
Version: 1.4.6
Release: 1%{?dist}
License: BSD
Group: Development/Languages
URL: http://pear.php.net/package/Date
Source0: http://pear.php.net/get/Date-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php-pear
BuildRequires: php-pear

%description
This package provides generic classes for representation and manipulation of
dates, times and time zones without the need of timestamps, which is a huge
limitation for php programs. Includes time zone data, time zone conversions
and many date/time conversions.


%prep


%install
%{__rm} -rf %{buildroot}
pear install -R %{buildroot} -n %{SOURCE0}
# Remove these hidden files, we don't want to include those
%{__rm} -rf %{buildroot}%{pear_dir}/{.channels,.depdb*,.filemap,.lock,.registry}

%{__mkdir_p} %{buildroot}%{xml_dir}
%{__tar} -xzvf %{SOURCE0} package.xml
%{__cp} -a package.xml %{buildroot}%{xml_dir}/Date.xml


%clean
%{__rm} -rf %{buildroot}


%post
pear install --nodeps --soft --force --register-only \
    %{xmldir}/Date.xml &>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        Date &>/dev/null || :
fi


%files
%defattr(0644, root, root, 0755)
%{pear_dir}/*


%changelog
* Tue Jun 27 2006 Matthias Saou <http://freshrpms.net/> 1.4.6-1
- Initial RPM release.

