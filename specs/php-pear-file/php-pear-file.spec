# $Id$
# Authority: matthias

%define pear_dir %(pear config-get php_dir 2>/dev/null || echo %{_datadir}/pear)
%define xml_dir  %{peardir}/.pkgxml

Summary: PEAR package to read/write files and deal with paths
Name: php-pear-file
Version: 1.2.2
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pear.php.net/package/File
Source0: http://pear.php.net/get/File-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php-pear
BuildRequires: php-pear

%description
This package provides easy access to read/write to files along with some
common routines to deal with paths. Also provides interface for handling
CSV files.


%prep


%install
%{__rm} -rf %{buildroot}
pear install -R %{buildroot} -n %{SOURCE0}
# Remove these hidden files, we don't want to include those
%{__rm} -rf %{buildroot}%{pear_dir}/{.channels,.depdb*,.filemap,.lock,.registry}

%{__mkdir_p} %{buildroot}%{xml_dir}
%{__tar} -xzvf %{SOURCE0} package.xml
%{__cp} -a package.xml %{buildroot}%{xml_dir}/File.xml


%clean
%{__rm} -rf %{buildroot}


%post
pear install --nodeps --soft --force --register-only \
    %{xmldir}/File.xml &>/dev/null

%postun
if [ $1 -eq 0 ]; then
    pear uninstall --nodeps --ignore-errors --register-only File &>/dev/null
fi


%files
%defattr(0644, root, root, 0755)
%{pear_dir}/*


%changelog
* Tue Jun 27 2006 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Initial RPM release.

